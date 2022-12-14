from django.shortcuts import render
from .models import Product,Brand,Category
from django.views.generic import ListView,DetailView
# Create your views here.


class ProductList(ListView):
    model=Product



class ProductDetail(DetailView):
    model=Product


class BrandList(ListView):
    model=Brand
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    

class BrandDetail(DetailView):
    model=Brand

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand=self.get_object()
        context["brand_products"] = Product.objects.filter(brand=brand)
        return context
    
class CategoryList(ListView):
    model=Category

    

# class CategoryDetail(DetailView):
#     model=Category
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         category=self.get_object()
#         context["category_brand"] = Brand.objects.filter(category=category)
#         return context