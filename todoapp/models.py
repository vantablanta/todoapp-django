from django.db import models


class Category(models.Model):
    type = models.CharField(max_length = 200)

    def __str__(self):
        return self.type

class Todo(models.Model):
    name = models.CharField(max_length = 200)
    category= models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta():
       ordering = ['-created', '-updated']