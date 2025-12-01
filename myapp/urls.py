from django.urls import path
from myapp import views

urlpatterns=[
    path('', views.home, name='my_home'),
    path('about/', views.about, name='my_about'),
    path('service/', views.service, name='my_service'),
    path('event/', views.event, name='my_event'),
    path('team/', views.team, name='my_team'),
    path('contact/', views.contact, name='my_contact'),
    path('donation/', views.donation, name='my_donation'),
    path('testimonial/', views.testimonial, name='my_testimonial'),
    path('feature/', views.feature, name='my_feature'),
]