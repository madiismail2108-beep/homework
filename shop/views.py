from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import Paginator


def home(request):
  products = Product.objects.filter(is_active=True) 
  q = request.GET.get('q')
  if q:
   products = products.filter(name__icontains=q)


   paginator = Paginator(products, 9) # 9 products per page
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)


   context = {
   'page_obj': page_obj,
    'query': q or '',
    }
   return render(request, 'shop/home.html', context)
# Create your views here.
