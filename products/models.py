from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator,MaxValueValidator
from taggit.managers import TaggableManager
from django.utils.text import slugify
# Create your models here.



FLAG_OPTION=(
('New','New'),
('Feature','Feature'),
('Sale','Sale'),
)



class Product(models.Model):
    name=models.CharField(_("Name"), max_length=50)
    subtitle=models.CharField(_("Subtitle"),max_length=500)
    sku=models.IntegerField(_("Sku"))
    image=models.ImageField(upload_to='products/')
    desc=models.TextField(_("Description"),max_length=1000)
    price=models.FloatField(_("Price"))
    flag=models.CharField(_('Flag'),max_length=10,choices=FLAG_OPTION)
    quantity=models.IntegerField(_("Quantity"))
    brand=models.ForeignKey('Brand',related_name='product_brand',on_delete=models.SET_NULL,null=True,blank=True )
    category=models.ForeignKey('Category',related_name='product_category',on_delete=models.SET_NULL,null=True,blank=True)
    tags = TaggableManager()
    slug=models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.name

class ProductImages(models.Model):
    product = models.ForeignKey(Product,related_name='product_image',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_image/')

    def __str__(self):
        return str(self.product)

class Brand(models.Model):
    name=models.CharField(_('Name'),max_length=50)
    image=models.ImageField(_('Image'),upload_to='brands/')
    category=models.ForeignKey('Category',related_name='brand_category',on_delete=models.SET_NULL,null=True,blank=True)


    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(_('Name'),max_length=50)
    image=models.ImageField(_('Image'),upload_to='category/')


    def __str__(self):
        return self.name

class ProductReviews(models.Model):
    user=models.ForeignKey(User,related_name='user_reviews',on_delete=models.CASCADE,verbose_name=_('User'))
    product=models.ForeignKey(Product,related_name='product_review',on_delete=models.CASCADE,verbose_name=_('Product'))
    rate=models.IntegerField(verbose_name=_('Rate'),validators=[MaxValueValidator(5),MinValueValidator(0)])
    review=models.TextField(max_length=500,verbose_name=_('Review'))
    created_at=models.DateTimeField(default=timezone.now,verbose_name=_('Created_at'))


    def __str__(self):
        return str(self.user)