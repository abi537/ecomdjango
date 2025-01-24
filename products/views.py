from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    fetured_products=Product.objects.order_by('priority')[:4]
    latest_products=Product.objects.order_by('-id')[:4]
    context={
        'fetured_products':fetured_products,
        'latest_products':latest_products
    }

    return render(request,'index.html',context)

def list_product(request):
    pages=1
    if request.GET:
        pages=request.GET.get('pages',1)
        

    produt_list=Product.objects.order_by('priority')
    product_paginator=Paginator(produt_list,8)
    produt_list=product_paginator.get_page(pages)
    context={'product':produt_list}
    return render(request,'product.html',context)

def detail_product(request,pk):
    product=Product.objects.get(pk=pk)
    context={'product':product}

    return render(request,'product_detail.html',context)