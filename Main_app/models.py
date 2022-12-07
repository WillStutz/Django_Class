from django.db import models

# Create your models here.





#make a change here, then do python manage.py makemigrations, then python manage.py migrate, update the admin.py
class Topic(models.Model):
    text = models.CharField(max_length=200)

    data_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'Entries'
        
    def __str__(self):
        return f"{self.text[:50]}..."