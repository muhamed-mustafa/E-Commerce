from django.shortcuts import render,get_object_or_404
from .models import Product , Category
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.db.models import Q , Count

# This is Function about All Products 
def product_list(request,category_slug=None):
    category = None
    
    product_list = Product.objects.all()
    category_list = Category.objects.annotate(total_products=Count('product')).exclude(CATParent__isnull=True)

    if category_slug :
        category = get_object_or_404(Category,CATSlug=category_slug)
        product_list = product_list.filter(PRDCategory=category)

    search_query = request.GET.get('q')
    if search_query :
        product_list = product_list.filter(
            Q(PRDName__icontains = search_query)|
            Q(PRDCategory__CATName__icontains = search_query)
        )
        

    paginator = Paginator(product_list,4)
    page = request.GET.get('page')
    try:
        product_list = paginator.get_page(page)
    except PageNotAnInteger:
        product_list = paginator.get_page(1)
    except EmptyPage:
        product_list = paginator.get_page(paginator.num_pages)

    context = {'product_list':product_list,'category_list':category_list,'category':category}

    return render(request,'product/product_list.html',context)

# This is Function about One or single Product
def product_detail(request,slug):
    product_detail = get_object_or_404(Product,PRDSlug=slug)
    context = {'product_detail':product_detail}
    return render(request,'product/product_detail.html',context)

