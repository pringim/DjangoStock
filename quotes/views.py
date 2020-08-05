from django.shortcuts import render, redirect
from .models import StockMarket
from .forms import StockForm
from django.contrib import messages


def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_8fd4d93086094b8c984c33dd2f5c96e2")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above.."})


def about(request):
    return render(request, 'about.html', {})


def add_stock(request):
    import requests
    import json
    if request.method == 'POST':
        form = StockForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Stock Has Been Added !')
            return redirect('add_stock')
    else:
        ticker = StockMarket.objects.all()
        output = []
        for ticker_item in ticker:
            api_request = requests.get(
                "https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_8fd4d93086094b8c984c33dd2f5c96e2")

            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error..."
        return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})


def delete(request, stock_id):
    item = StockMarket.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, "Stock Has Been Deleted !")
    return redirect(delete_stock)


def delete_stock(request):
    ticker = StockMarket.objects.all()
    return render(request, 'delete_stock.html', {'ticker': ticker})