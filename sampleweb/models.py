from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=250)    
    is_done = models.BooleanField(default=False)
    added_date = models.DateTimeField(null=True)

    def __str__(self):
        """Returns the string representation of the todo object"""
        return f"Title={ self.title} , Completed = {self.is_done}"

