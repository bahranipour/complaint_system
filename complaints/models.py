from django.db import models
from django.conf import settings

class Complaint(models.Model):
    STATUS_CHOICES = [
        ('در انتظار بررسی','در انتظار بررسی'),
        ('در حال بررسی','در حال بررسی'),
        ('بررسی شده','بررسی شده'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='complaints')
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='در انتظار بررسی')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'شکایت'
        verbose_name_plural = 'شکایت ها'

    def __str__(self):
        return self.title