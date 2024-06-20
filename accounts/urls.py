from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, profile_view, edit_profile, customers_view, customer_list_view, customer_detail_view, create_customer, update_customer

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/view/', profile_view, name='profile_view'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('customers/', customers_view, name='customers'),
    path('customer_list/', customer_list_view, name='customer_list'),
    path('customers/<int:id>/', customer_detail_view, name='customer_detail'),
    path('customers/create/', create_customer, name='create_customer'),
    path('customers/update/<int:pk>/', update_customer, name='update_customer'),
]