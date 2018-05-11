from django.shortcuts import render
from . models import Order
def home_page(request):
    if request.method == 'POST':
        our_address = request.POST.get('address')
        our_user = request.POST.get("order")
        address_obj = Order.objects.create(
            address=our_address,
            meal=our_user
        )

        return render(request, 'meituan/home_page.html', {'order': address_obj,})
    return render(request, 'meituan/home_page.html')