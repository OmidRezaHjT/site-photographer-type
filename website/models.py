from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

class Meta:
    ordering = ('created_date',) 
    def __str__(self):
        return self.name
