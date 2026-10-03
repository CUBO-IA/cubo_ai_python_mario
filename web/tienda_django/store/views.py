from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()[:6]

    context = {
        "categories": categories,
        "products": products,
    }

    return render(request, "store/home.html", context)


def products(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    category_id = request.GET.get("category")

    if category_id:
        products = products.filter(category_id=category_id)

    context = {
        "products": products,
        "categories": categories,
    }

    return render(request, "store/products.html", context)


def product_detail(request, product_id):
    product = get_object_or_404(
        Product,
        id=product_id
    )

    context = {
        "product": product,
    }

    return render(
        request,
        "store/product_detail.html",
        context
    )

