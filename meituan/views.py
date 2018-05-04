from django.shortcuts import render

def home_page(request):

    if request.method == 'POST':
        address = request.POST.get('order')
        order = request.POST.get("address")

        print(address * 10)
        return render(request, 'meituan/home_page.html', {'address': address, 'order': order})

    return render(request, 'meituan/home_page.html')