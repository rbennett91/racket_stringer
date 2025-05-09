from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Order(models.Model):
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    racket = models.ForeignKey(
        "Racket", on_delete=models.CASCADE, null=True, blank=True
    )
    main_string = models.ForeignKey(
        "String", on_delete=models.CASCADE, related_name="+", null=True, blank=True
    )
    main_string_tension = models.PositiveSmallIntegerField(
        default=50,
        validators=[MaxValueValidator(90), MinValueValidator(20)],
        null=True,
        blank=True,
    )
    cross_string = models.ForeignKey(
        "String", on_delete=models.CASCADE, related_name="+", null=True, blank=True
    )
    cross_string_tension = models.PositiveSmallIntegerField(
        default=50,
        validators=[MaxValueValidator(90), MinValueValidator(20)],
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField()
    is_complete = models.BooleanField(default=False)
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    notes = models.TextField(max_length=300, blank=True)

    class Meta:
        ordering = ["due_date"]

    def __str__(self):
        return "{} {} - {}".format(
            self.customer.first_name, self.customer.last_name, self.racket.model
        )


class Racket(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    recommended_tension_lbs = models.CharField(max_length=20)
    string_length = models.CharField(max_length=20)
    string_pattern = models.CharField(max_length=20)
    main_holes_skipped = models.CharField(max_length=40)
    main_holes_tied = models.CharField(max_length=10)
    cross_holes_started = models.CharField(max_length=10)
    cross_holes_tied = models.CharField(max_length=20)

    def __str__(self):
        return "{} {}".format(self.brand, self.model)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["brand", "model"], name="unique_racket_name"
            ),
        ]


class String(models.Model):
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{} {}".format(self.brand, self.name)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["brand", "name"], name="unique_string_name"
            ),
        ]


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["first_name", "last_name"], name="unique_customer_name"
            ),
        ]