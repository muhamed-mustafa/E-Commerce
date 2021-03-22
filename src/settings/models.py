from django.db import models
from django.utils.translation import ugettext_lazy as _

class Brand(models.Model):
    BRDName = models.CharField(max_length=40,verbose_name=_("Brand Name"))
    BRDDesc = models.TextField(null=True,blank=True,verbose_name=_("Brand Description"))

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.BRDName    

class Variant(models.Model):
    VARName = models.CharField(max_length=40,verbose_name=_("Variant Name"))
    VARDesc = models.TextField(null=True,blank=True,verbose_name=_("Variant Description"))

    class Meta:
        verbose_name = _("Variant")
        verbose_name_plural = _("Variants")

    def __str__(self):
        return self.VARName           