from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from myShop.models import Category,Product

def category_list(req):
    category_list = Category.objects.all()
    product_list = Product.objects.all()
    return render(
        req,
        template_name='category/category_list.html',
        context={
            'category_list': category_list,
            'product_list': product_list
        }
    )

def category(req,id):
    if req.method == 'GET':
        category = get_object_or_404(Category,id=id)
    return render(
        req,
        template_name='category/category.html',
        context={
            'category' : category
        }
    )

