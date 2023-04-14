from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    
    password = models.CharField(max_length=20, default=None, null=True)  # 열을 추가할 때 default 값을 넣어주는 것이 좋음
    image = models.CharField(max_length=500, default=None, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    point = models.IntegerField()
    comment = models.CharField(max_length=500)
    
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)  # 만약 Restaurant가 삭제된다면 어떻게 처리할 것인가
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)