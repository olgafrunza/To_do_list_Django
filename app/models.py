from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=35)
    description = models.TextField()
    PRIORITY_OPTIONS = (
        ('H', "High"),
        ('N','Normal'),
        ('L', 'Low')
    )
    priority = models.CharField(max_length = 1, choices=PRIORITY_OPTIONS, default="N")
    done = models.BooleanField(default=False)
    createAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task