from django.db import models


class SpaceOwner(models.Model):
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class Space(models.Model):
    space_name = models.CharField(max_length=100)
    space_description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    square = models.PositiveIntegerField()

    owner = models.ForeignKey(
        SpaceOwner, on_delete=models.CASCADE, related_name="spaces"
    )

    def __str__(self):
        return self.space_name


class Reservation(models.Model):
    start_time = models.DateField()
    end_time = models.DateField()
    space = models.ForeignKey(
        Space, on_delete=models.CASCADE, related_name="reservations"
    )

    def __str__(self):
        return f"{self.space} ({self.start_time} - {self.end_time})"
