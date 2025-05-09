from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path("racket_stringer/admin/", admin.site.urls),
    path(
        "racket_stringer/accounts/",
        include("django.contrib.auth.urls"),
    ),
    path(
        "racket_stringer/",
        RedirectView.as_view(url=reverse_lazy("new_order")),
        name="index",
    ),
    path("racket_stringer/orders", views.Orders.as_view(), name="orders"),
    path("racket_stringer/new_order", views.NewOrder.as_view(), name="new_order"),
    path(
        "racket_stringer/show_order/<int:pk>",
        views.ShowOrder.as_view(),
        name="show_order",
    ),
    path(
        "racket_stringer/update_order/<int:pk>",
        views.UpdateOrder.as_view(),
        name="update_order",
    ),
    path(
        "racket_stringer/delete_order/<int:pk>",
        views.DeleteOrder.as_view(),
        name="delete_order",
    ),
    path(
        "racket_stringer/new_customer", views.NewCustomer.as_view(), name="new_customer"
    ),
    path("racket_stringer/new_string", views.NewString.as_view(), name="new_string"),
    path("racket_stringer/search_rackets", views.search_rackets, name="search_rackets"),
    path("racket_stringer/search_strings", views.search_strings, name="search_strings"),
]