from django.urls import path
from store.views import home , product_detil 

urlpatterns = [
    path('',home,name="home"),
    path('<slug:slug_categorey>/',home,name="slug_categorey"),
    path('<int:product_id>/<slug:product_slug>',product_detil,name="product_detil"),
]