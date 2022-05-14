from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm

from .models import Customer, Order


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
            "is_complete": "Is Complete?",
            "assigned_to": "Assigned to Stringer:",
        }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Submit", css_class="float-right"))


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
        return first_name.capitalize()

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        return last_name.capitalize()

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Submit", css_class="float-right"))
