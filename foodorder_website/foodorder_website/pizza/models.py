from django.db import models

# Create your models here.
class student (models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id} - {self.email} to {self.username}"

class menu (models.Model):
    desh = models.ManyToManyField(orders )
    prise=models.IntegerField()

    def __str__(self):
        return f"  {self.desh} to {self.prise}"

class orders (models.Model):
    order = models.ForeignKey(menu, on_delete=models.CASCADE)
    totle = models.IntegerField()
    note = models.TextField()

    def __str__(self):
        return f"{self.order} - {self.totle} to {self.note}"
