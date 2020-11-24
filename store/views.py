from django.shortcuts import render
from .models import Entry
from django.db.models import Sum, Min, Max, Avg

# Create your views here.


def index(request):
    entrs = Entry.objects.all()

    summation = list(Entry.objects.aggregate(Sum('price')).values())[0]

    summationPaid = list(Entry.objects.aggregate(Sum('pricePaid')).values())[0]

    balance = list(Entry.objects.aggregate(Sum('price')).values())[
        0] - list(Entry.objects.aggregate(Sum('pricePaid')).values())[0]

    return render(request, "index.html", {'entrs': entrs, 'summation': summation, 'summationPaid': summationPaid, 'balance': balance})


def home(request):

    return render(request, "landing.html")
