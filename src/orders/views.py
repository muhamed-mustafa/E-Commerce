from django.shortcuts import render
from .models import OrderItem
from cart.cart import Cart
from .forms import OrderCreateForm

# Create your views here.

def order_create(request):
    
    cart = Cart(request)
    if request.method == 'POST' :
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            
            for item in cart :
                OrderItem.objects.create(
                    order    = order ,
                    product  = item['product'] , 
                    price    = item['price']   ,
                    quantity = item['quantity']
                )
            # Clear The Cart
            cart.clear()
            return render(request,'orders/order/created.html',{'order':order})
        
    else :
            form = OrderCreateForm()

    return render(request,'orders/order/create.html',{'form':form,'cart':cart})
