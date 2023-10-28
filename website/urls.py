from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    # individual record page
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('products/', views.products, name='products'),
    path('accounts/', views.accounts, name='accounts'),
    path('opportunities/', views.opportunities, name='opportunities'),
    path('add_opp/', views.add_opp, name='add_opp'),
    path('opp_record/<int:pk>', views.opp_record, name='opp_record'),
]
