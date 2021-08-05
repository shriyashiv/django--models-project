from django.shortcuts import render
from django.http import HttpResponse


def home(request):
   return render(request, 'DEMOAPP/home.html')
from.forms import Passenger_detailsForm
def index(request):
   form=Passenger_detailsForm()
   if request.method=='POST':
      form=Passenger_detailsForm(request.POST)
      if form.is_valid():form.save()
   context={"form": form}
   return render(request,'DEMOAPP/Bookflight.html',context)
def value(request):
   return render(request,'DEMOAPP/Aboutus.html')


