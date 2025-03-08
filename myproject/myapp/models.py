from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class users(models.Model):
    objects = models.Manager()
    user_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11, unique=True)
    password = models.CharField(max_length=128)
    student_number = models.CharField(max_length=12, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        # 检查密码是否已经被哈希处理
        if self.password and not str(self.password).startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.user_name
    