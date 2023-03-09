from django.urls import path
from frontend import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('discategory/<itemCatg>/', views.discategory, name="discategory"),
    path('details/<int:dataid>/', views.details, name="details"),
    path('form/', views.form, name="form"),
    path('formreg/', views.formreg, name="formreg"),
    path('customerlogin/', views.customerlogin, name="customerlogin"),
    path('customerlogout/', views.customerlogout, name="customerlogout"),
    path('condet/', views.condet, name="condet")


]