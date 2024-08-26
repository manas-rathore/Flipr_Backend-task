from django.urls import path
from .views import OrderListCreateView, AdminOrderListView, UserOrderListView, OrderDetailView

urlpatterns = [
    path('', OrderListCreateView.as_view(), name='order-list-create'),
    path('admin/', AdminOrderListView.as_view(), name='admin-order-list'),
    path('user/', UserOrderListView.as_view(), name='user-order-list'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]
