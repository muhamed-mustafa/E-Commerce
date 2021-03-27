from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse

class Product(models.Model):
    PRDName          = models.CharField(max_length=100,verbose_name=_("Name"))
    PRDImage         = models.ImageField(upload_to="product/",null=True,blank=True,verbose_name=_("Image"))
    PRDCategory      = models.ForeignKey('Category',on_delete=models.CASCADE,null=True,blank=True,verbose_name=_("Category"))
    PRDBrand         = models.ForeignKey('settings.Brand',on_delete=models.CASCADE,null=True,blank=True,verbose_name=_("Brand"))
    PRDDesc          = models.TextField(verbose_name=_("Description"))
    PRDPrice         = models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_("Price"))
    PRDDiscountPrice = models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_("Discount Price"),null=True,blank=True)
    PRDCost          = models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_("Cost"))
    PRDCreated       = models.DateTimeField(auto_now_add=True,verbose_name=_("Created At"))
    PRDUpdated       = models.DateTimeField(auto_now=True,verbose_name=_('Updated At'))
    PRDSlug          = models.SlugField(blank=True,null=True,verbose_name=_("Product Slug"))
    PRDISNew         = models.BooleanField(default=True,verbose_name=_("New Product"))
    PRDISBestSeller  = models.BooleanField(default=False,verbose_name=_("Best Seller"))
    PRDAvaliable     = models.BooleanField(default=True,verbose_name=_('Avaliable'))

    def save(self,*args,**kwargs):
        if not self.PRDSlug :
            self.PRDSlug = slugify(self.PRDName)
        super(Product,self).save(*args,**kwargs)        

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


    def get_absolute_url(self):
        return reverse('products:product_detail',kwargs={'slug':self.PRDSlug})
           

    def __str__(self):
        return self.PRDName


class ProductImage(models.Model):
    PRDIProduct = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name=_("Product"))
    PRDIImage   = models.ImageField(upload_to="product/",verbose_name=_("Image"))


    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")


    def __str__(self):
        return str(self.PRDIProduct)


class Category(models.Model):
    CATName   = models.CharField(max_length=50,verbose_name=_("Category Name"))
    CATParent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,limit_choices_to={'CATParent__isnull':True},verbose_name=_("Main Category"))
    CATDesc   = models.TextField(verbose_name=_("Category Description"))
    CATImage  = models.ImageField(upload_to="category/",verbose_name=_("Category Image"))   
    CATSlug   = models.SlugField(blank=True,null=True,verbose_name=_("Category Slug"))  


    def save(self,*args,**kwargs):
        if not self.CATSlug :
            self. CATSlug = slugify(self.CATName)
        super(Category,self).save(*args,**kwargs) 


    def get_absolute_url(self):
        return reverse('products:category_list',args=[self.CATSlug])


    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _(" Categories")

   
    def __str__(self):
        return self.CATName


class Product_Alternative(models.Model):
    PALNProduct      = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='main_product',verbose_name=_('Product'))
    PALNAlternatives = models.ManyToManyField(Product,related_name='alternative_products',verbose_name=_("Alternatives"))


    class Meta:
        verbose_name = _("Product Alternative")
        verbose_name_plural = _("Product Alternatives")


    def __str__(self):
        return str(self.PALNProduct)    


class Product_Accessories(models.Model):
    PACCProduct     = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='mainAccessory_product',verbose_name=_('Product'))
    PACCAccessories = models.ManyToManyField(Product,related_name='accessories_products',verbose_name=_("Accessories"))


    class Meta:
        verbose_name = _("Product Accessory")
        verbose_name_plural = _("Product Accessories")


    def __str__(self):
        return str(self.PACCProduct)            

