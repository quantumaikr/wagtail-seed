from django.db import models

from django.contrib.auth.models import AbstractUser

from wagtail.admin.edit_handlers import (
    FieldPanel, 
)

class User(AbstractUser):
    phone = models.CharField(
        max_length = 11, 
        verbose_name="핸드폰 번호",
        null=True,
        blank=True,
    )
    
    panels = [
        FieldPanel('phone'),
    ]
    
    class Meta:
        verbose_name = "사용자"
        verbose_name_plural = "사용자"


    def __str__(self): # User 모델의 ForeignKey로 선택될 때 쓰임
        return f"{self.username}"
