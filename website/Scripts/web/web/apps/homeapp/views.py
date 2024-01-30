from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.


class HomeView(View):
    def get(self,request):
        return render(request,'homeapp/home.html')

