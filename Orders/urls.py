from django.urls import path, include

from . import views

urlpatterns = [
    path('orders/<int:customer_id>/', views.OrderListView.as_view()),
    path('orders/', views.OrderListView.as_view()),
]
