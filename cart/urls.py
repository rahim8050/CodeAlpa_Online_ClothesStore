from django.urls import  path
from .views import cart_add, cart_detail, cart_remove, cart_count

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', cart_add, name='cart_add'),
    path("remove/<int:product_id>/",cart_remove,name='cart_remove'),
    path('cart/count/', cart_count, name='cart_count'),

]