from django.db import models

# Create your models here.
class Data(models.Model):
    name=models.CharField(max_length=20,null=True, blank=True)
    mobile_no = models.IntegerField(null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    # birth_date = models.DateField(null=True, blank=True)
    address = models.TextField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField( max_length=100, null=True, blank=True)
    state = models.CharField( max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=12, null=True, blank=True)
    Hightest_qualification = models.CharField(max_length=100, null=True, blank=True)
    Professinal_Experriance = models.CharField(max_length=100, null=True, blank=True)