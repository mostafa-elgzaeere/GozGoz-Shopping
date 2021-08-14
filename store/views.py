from django.shortcuts import render
from store.models import Categorey , Product
from cart.forms   import ProductForm

# Create your views here.

def home(request,slug_categorey = None):
    form= ProductForm()
    categories=Categorey.objects.all()
    products  = Product.objects.filter(avilable=True)
    current_categorey = None
    if slug_categorey:
        current_categorey=Categorey.objects.get(slug=slug_categorey)
        products=current_categorey.products.filter(avilable=True)
    
    return render(request,'home.html',{"categories":categories,"products":products,"current_categorey":current_categorey,"form":form})


def product_detil(request,product_id,product_slug):
    form= ProductForm()
    product=Product.objects.get(id=product_id,slug=product_slug,avilable=True)
    return render(request,"product_detil.html",{"product":product,"form":form})

