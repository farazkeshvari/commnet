from django.views import generic

from .models import Product


class ProductListView(generic.ListView):
    model = Product
    template_name = "product/product_list.html"
    context_object_name = "products"


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "product/product_detail.html"
