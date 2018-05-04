from django.shortcuts import render

def home_page(request):

    if request.method == 'order':
        address = request.order.get('order')
        order = request.order.get("address")

        print(address * 10)
        return render(request, 'meituan/home_page.html', {'address': address, 'order': order})

    return render(request, 'meituan/home_page.html')