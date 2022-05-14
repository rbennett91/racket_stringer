from datetime import datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    TemplateView,
    UpdateView,
)

from .forms import CustomerForm, OrderForm
from .models import Customer, Order, Racket, String


class Orders(LoginRequiredMixin, TemplateView):
    http_method_names = ["get"]
    template_name = "racket_stringer/orders.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        incomplete_orders = Order.objects.filter(
            assigned_to=self.request.user, is_complete=False
        ).order_by("-due_date", "created_at",)[:10]

        context["incomplete_orders"] = incomplete_orders
        return context


class NewOrder(LoginRequiredMixin, CreateView):
    http_method_names = ["get", "post"]
    template_name = "racket_stringer/new_order.html"
    model = Order
    form_class = OrderForm

    def get_initial(self):
        initial = {
            "due_date": datetime.now().date() + timedelta(days=7),
            "assigned_to": self.request.user,
        }
        return initial

    def get_success_url(self):
        return reverse("show_order", kwargs={"pk": self.object.id})


class ShowOrder(LoginRequiredMixin, DetailView):
    http_method_names = ["get"]
    template_name = "racket_stringer/show_order.html"
    model = Order


class UpdateOrder(LoginRequiredMixin, UpdateView):
    http_method_names = ["get", "post"]
    template_name = "racket_stringer/update_order.html"
    model = Order
    form_class = OrderForm

    def get_success_url(self):
        return reverse("show_order", kwargs={"pk": self.object.id})


class DeleteOrder(LoginRequiredMixin, DeleteView):
    http_method_names = ["get", "post"]
    template_name = "racket_stringer/delete_order.html"
    model = Order

    success_url = reverse_lazy("orders")


class NewCustomer(LoginRequiredMixin, CreateView):
    http_method_names = ["get", "post"]
    template_name = "racket_stringer/new_customer.html"
    model = Customer
    form_class = CustomerForm

    def get_success_url(self):
        return reverse("new_order")


@login_required
def search_rackets(request):
    search = request.GET.get("search", None)

    # select2 expects a specific response structure:
    # https://select2.org/data-sources/formats.
    # so, we'll annotate Racket objects with the expected 'text' field.
    # this allows us to 1) search by brand or model, and 2) return the output
    # of the orm 'values' function.
    rackets = (
        Racket.objects.annotate(text=Concat("brand", Value(" "), "model"))
        .filter(
            Q(brand__icontains=search)
            | Q(model__icontains=search)
            | Q(text__icontains=search)
        )
        .order_by("brand", "model")
        .values("id", "text")
    )

    response = {"results": list(rackets)}
    return JsonResponse(response, safe=False)


@login_required
def search_strings(request):
    search = request.GET.get("search", None)

    # select2 expects a specific response structure:
    # https://select2.org/data-sources/formats.
    # so, we'll annotate String objects with the expected 'text' field.
    # this allows us to 1) search by brand or name, and 2) return the output
    # of the orm 'values' function.
    strings = (
        String.objects.annotate(text=Concat("brand", Value(" "), "name"))
        .filter(
            Q(brand__icontains=search)
            | Q(name__icontains=search)
            | Q(text__icontains=search)
        )
        .order_by("brand", "name")
        .values("id", "text")
    )

    response = {"results": list(strings)}
    return JsonResponse(response, safe=False)
