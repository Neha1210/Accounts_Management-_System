from django.db import models
from django.urls import reverse

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class product(models.Model):
    Category=(
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor')
    )
    name=models.CharField(max_length=200,null=True)
    Price=models.FloatField(null=True)
    Category=models.CharField(max_length=200,null=True,choices=Category)
    Discription=models.CharField(max_length=200,null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    Tag=models.ManyToManyField(Tag)
    img=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self,):
        return reverse('view_product',args=[self.id],)

class Order(models.Model):
    Customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product=models.ForeignKey(product,null=True,on_delete=models.SET_NULL)

    ###### 'choices' must be an iterable containing (actual value, human readable name) tuples. #######


    status=(
        ('pending','pending'),
        ('out for delivery','out for delivery'),
        ('Delivered','Delivered')
    )
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=200,null=True,choices=status)

    def __str__(self):
        return self.product.name