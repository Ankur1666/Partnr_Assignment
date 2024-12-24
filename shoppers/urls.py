from django.urls import path,include
from .views import ProductViews
urlpatterns = [
    path("add/product/",ProductViews.as_view(),name="add_product")
]