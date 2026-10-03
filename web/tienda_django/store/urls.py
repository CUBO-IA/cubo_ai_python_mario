from django.urls import path

from . import views


app_name = "store"


urlpatterns = [
    path("", views.home, name="home"),
    path("productos/", views.products, name="products"),
    path(
        "producto/<int:product_id>/",
        views.product_detail,
        name="product_detail"
    ),
]
