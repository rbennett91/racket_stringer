from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm

from .models import Customer, Order, String


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = [
            "customer",
            "racket",
            "main_string",
            "main_string_tension",
            "cross_string",
            "cross_string_tension",
            "due_date",
            "is_complete",
            "assigned_to",
            "notes",
        ]
        labels = {
            "main_string": "Main String",
            "main_string_tension": "Main String Tension",
            "cross_string": "Cross String",
            "cross_string_tension": "Cross String Tension",
            "due_date": "Due Date",
            "is_complete": "Is Order Complete?",
            "assigned_to": "Assigned to Stringer:",
        }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Submit", css_class="float-end"))


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = [
            "first_name",
            "last_name",
            "email_address",
        ]
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email_address": "Email Address",
        }

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        return first_name.title()

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        return last_name.title()

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Create", css_class="float-end"))


class StringForm(ModelForm):
    class Meta:
        model = String
        fields = [
            "brand",
            "name",
        ]

    def clean_brand(self):
        brand = self.cleaned_data["brand"]
        return brand.title()

    def clean_name(self):
        name = self.cleaned_data["name"]
        return name.title()

    def __init__(self, *args, **kwargs):
        super(StringForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Create", css_class="float-end"))
