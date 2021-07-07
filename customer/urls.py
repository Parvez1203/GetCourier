from django.urls import path
from customer import views

urlpatterns = [
    path('' ,views.index),
    path('contact_us/' , views.contact_us),
    path('about/' , views.about),
    path('customer_support/' , views.customer_support),
    path('FAQs/' , views.FAQs),
    path('login/',views.login.as_view()),
    path('logout/',views.logoutUser),
    path('registration/',views.registration),
    path('orders/',views.orders)
]