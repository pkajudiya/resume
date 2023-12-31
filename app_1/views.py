from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.views import View


class home(View):
    def get(self, request):
        # <view logic>
        return render(request, "main.html")