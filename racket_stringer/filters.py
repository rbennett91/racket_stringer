import django_filters
from django.contrib.auth import get_user_model
from django_filters import BooleanFilter, DateFilter, ModelChoiceFilter

from .models import Customer, Order, Racket, String

User = get_user_model()


class OrderFilter(django_filters.FilterSet):
    customer = ModelChoiceFilter(label="Customer", queryset=Customer.objects.all())
    racket = ModelChoiceFilter(label="Racket", queryset=Racket.objects.all())
    main_string = ModelChoiceFilter(label="Main String", queryset=String.objects.all())
    cross_string = ModelChoiceFilter(
        label="Cross String", queryset=String.objects.all()
    )
    due_date = DateFilter(label="Due Date")
    is_complete = BooleanFilter(label="Is Order Complete?")
    assigned_to = ModelChoiceFilter(
        label="Assigned to Stringer", queryset=User.objects.all()
    )

    class Meta:
        model = Order
        fields = [
            "customer",
            "racket",
            "main_string",
            "cross_string",
            "due_date",
            "is_complete",
            "assigned_to",
        ]