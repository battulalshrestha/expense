from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Home page
    
    # Login_or_Signup views
    path('users/', views.login_or_signup_list, name="user_list"),
    path('users/<int:pk>/', views.login_or_signup_detail, name="user_detail"),
    
    # Group views
    path('groups/', views.group_list, name="group_list"),
    path('groups/<int:pk>/', views.group_detail, name="group_detail"),
    
    # Group Membership views
    path('groups/add_user/', views.add_user_to_group, name="add_user_to_group"),
    path('groups/user/<int:user_id>/', views.user_groups, name="user_groups"),
    
    # Bill Detail views
    path('bills/', views.bill_list, name="bill_list"),
    
    # Friend views
    path('friends/', views.friend_list, name="friend_list"),
    
    # Vendor views
    path('vendors/', views.vendor_list, name="vendor_list"),
    
    # Expense views
    path('expenses/', views.expense_list, name="expense_list"),
    
    # Note views
    path('notes/', views.note_list, name="note_list"),
]