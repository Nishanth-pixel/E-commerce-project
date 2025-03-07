from django.db import models

# Create your models here.

    
class database(models.Model):
     username=models.CharField(max_length=50,null=True)
     password=models.CharField(max_length=50,null=True)
     phonenumber=models.CharField(max_length=50,null=True)
     email=models.CharField(max_length=100,null=True)


class admin(models.Model):
      productname=models.CharField(max_length=200)
      offerprice=models.IntegerField()
      image=models.ImageField()
      productprice=models.IntegerField()   
      percentage=models.IntegerField()


class men(models.Model):
      productname=models.CharField(max_length=200)
      offerprice=models.IntegerField()
      image=models.ImageField()
      productprice=models.IntegerField()   
      percentage=models.IntegerField()

class women(models.Model):
      productname=models.CharField(max_length=200)
      offerprice=models.IntegerField()
      image=models.ImageField()
      productprice=models.IntegerField()   
      percentage=models.IntegerField()



class addtocart(models.Model):
      cid=models.IntegerField()
      productname=models.CharField(max_length=200)
      offerprice=models.IntegerField()
      image=models.ImageField()
      productprice=models.IntegerField()   
      percentage=models.IntegerField()
            