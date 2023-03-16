from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()  # 길이 제한이 없음
    
    created_at = models.DateTimeField(auto_now_add=True) # 자동으로 현재시 저장
    updated_at = models.DateTimeField(auto_now=True)
    
    # num_stars = models.IntegerField()