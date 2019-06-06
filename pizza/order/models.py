from django.db import models

# Create your models here.
class student (models.Model):
    username = models.CharField(max_length=64)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=225)

    def __str__(self):
        return f"{self.id} - {self.email} to {self.username}"




class menu (models.Model):
    desh = models.ManyToManyField(order, blank=True, related_name="passengers")
    prise = models.IntegerField()

    def __str__(self):
        return f"  {self.desh} to {self.prise}"


class order (models.Model):
    dish = models.ForeignKey(menu, on_delete=models.CASCADE, related_name="order")
    totle = models.IntegerField()
    note = models.TextField()

    def __str__(self):
        return f"{self.dish} - {self.totle} to {self.note}"
