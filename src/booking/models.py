from django.db import models


class User(models.Model):
    full_name = models.CharField(max_length=70)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    reservations = models.ManyToManyField("Reservation", blank=True)

    def __str__(self):
        return self.full_name


class Space(models.Model):
    space_name = models.CharField(max_length=100)
    space_description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    square = models.PositiveIntegerField()

    def __str__(self):
        return self.space_name


class SpaceOwner(models.Model):
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

    space = models.ForeignKey(Space, on_delete=models.CASCADE)


class Reservation(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    space = models.ForeignKey(
        Space, on_delete=models.CASCADE, related_name="reservations"
    )

    def __str__(self):
        return f"{self.space} ({self.start_time} - {self.end_time})"
