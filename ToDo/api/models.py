from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    due_date = models.DateField()

    STATUS = (
        ('Done', 'Done'),
        ('Pending', 'Pending'),
        ('Not Started', 'Not Started')
    )
    
    status_of_task = models.CharField(max_length=15, choices=STATUS)


    