from django.shortcuts import render, redirect


# def index(request):
#     return HttpResponse("this is the equivalent of @app.route('/')!")

from django.shortcuts import render , redirect
from .models import Order, Product


def index(request):

    if 'Cart' not in request.session: 
        request.session['Cart'] = []
    
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "index.html", context)



def checkout(request):

    # To prevent from duplicate the order.
    if 'Cart' not in request.session:
        return redirect('/')

    if request.method == 'POST':
        
        product = Product.objects.get(id=request.POST['product_id'])
        _order = Order.objects.create(
            quantity_ordered = int(request.POST['quantity']),
            total_price = int(request.POST['quantity']) * product.price
        )
        _order.save()

        # For loop to count all quanities in Database => Modal Order  # 
        totalQuantity = 0
        totalPaid = 0
        all_orders = Order.objects.all()
        
        for order in all_orders:
            totalQuantity += order.quantity_ordered
            totalPaid += order.total_price

        context = {
        "lastOrderPrice":int(request.POST['quantity']) * float(product.price),
        "totalQuantity":totalQuantity,
        "totalPaid":totalPaid
        }

        del request.session['Cart'] # delete the cart session to avoid deplication and make the first condition works.

        return render(request, "buy.html",context)

    else:
        return redirect('/')

# def index(request):
#     return render (request, 'index.html')

# def buy(request):
#     return render (request, 'buy.html')


def goBack(request):
    return redirect (request, '')