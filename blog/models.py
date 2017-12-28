from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE) # 外键类型
    title = models.CharField(max_length=200) # 普通的文本
    text = models.TextField() # 长文本
    created_date = models.DateTimeField(default=timezone.now()) # 日期时间类型
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title