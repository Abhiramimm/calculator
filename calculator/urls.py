"""
URL configuration for calculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from operations.views import AddtionView,SubstractionView,MultiplicationView,FactorialView\
    ,PrimeNumberView,BmiView,ReverseDigitView,SignupView,BmrView,EmiCalculatorView,TempConversionView,BmrVersionTwoView,CurrentBillView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',AddtionView.as_view()),
    path('sub/',SubstractionView.as_view()),
    path('multiply/',MultiplicationView.as_view()),
    path('factorial/',FactorialView.as_view()),
    path('prime/',PrimeNumberView.as_view()),
    path('bmi/',BmiView.as_view()),
    path('reverse/',ReverseDigitView.as_view()),
    path('register/',SignupView.as_view()),
    path('bmr/',BmrView.as_view()),
    path('emi/',EmiCalculatorView.as_view()),
    path('temp/',TempConversionView.as_view()),
    path('bmr/v2/',BmrVersionTwoView.as_view()),
    path("currentbill/",CurrentBillView.as_view()),
    
]
