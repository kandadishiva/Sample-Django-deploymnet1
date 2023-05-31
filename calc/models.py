from django.db import models

# Create your models here.
class Customer (models.Model):
    name=models.CharField(max_length=200, null=True,)
    phone=models.BigIntegerField(max_length=10 , null=True)
    email=models.EmailField(max_length=200, null=True)
    dateCreated=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class product(models.Model):
    CATEGORY=(
        ('Indoor','Indoor'),
        ('OutDoor','OutDoor'),
    )
    name=models.CharField(max_length=200, null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=200, null=True, choices=CATEGORY)
    tags=models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
    
class order(models.Model):
    Status=(
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product =models.ForeignKey(product, null=True, on_delete=models.SET_NULL)
    Status=models.CharField(max_length=200, null=True, choices=Status)
    id=models.AutoField(primary_key=True,auto_created=True)
    
    def __str__(self) -> str:
        return str(self.id)
