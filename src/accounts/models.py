from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django_countries.fields import CountryField
from django.urls import reverse
from django.db.models.signals import post_save
import datetime


def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return 'profile/%s.%s' % (instance.id, extension)



class Profile(models.Model):
    user      = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name=_("user"))
    slug      = models.SlugField(null=True,blank=True,verbose_name=_('slug'))
    image     = models.ImageField(_('image'),upload_to=image_upload,null=True,blank=True)
    country   = CountryField()
    address   = models.CharField(max_length=100,verbose_name=_("address"))
    join_date = models.DateTimeField(_('join_date'),default=datetime.datetime.now)


    def save(self,*args,**kwargs):
        if not self.slug :
            self.slug = slugify(self.user.username)
        super(Profile,self).save(*args,**kwargs)    

   
    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')


    def __str__(self):
        return '%s ' %(self.user)    


    def get_absolute_url(self):
        return reverse('accounts:edit_profile',kwargs={'slug':self.slug}) 


def create_profile(sender,**kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile,sender=User)        
