from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()  # duration in minutes
    date = models.DateField()

    def __str__(self):
        return f"{self.activity_type} by {self.user.username} on {self.date}"

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    height = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"Progress of {self.user.username} on {self.date}"