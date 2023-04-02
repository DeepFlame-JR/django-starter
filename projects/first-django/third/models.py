from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    point = models.IntegerField()
    comment = models.CharField(max_length=500)
    
    Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)  # 만약 Restaurant가 삭제된다면 어떻게 처리할 것인가
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)