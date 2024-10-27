from django.contrib import admin
from .models import Login_or_Signup, Group, Group_membership, Bill_detail, Friend, Vender, Expense, Note

# Login or Signup Admin
@admin.register(Login_or_Signup)
class LoginOrSignupAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'phone_number')
    search_fields = ('name', 'username', 'email')
    ordering = ('name',)

# Group Admin
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'group_status', 'date')
    list_filter = ('group_status',)
    search_fields = ('group_name',)

# Group Membership Admin
@admin.register(Group_membership)
class GroupMembershipAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'group_id')
    list_filter = ('group_id',)
    search_fields = ('user_id__name', 'group_id__group_name')

# Bill Detail Admin
@admin.register(Bill_detail)
class BillDetailAdmin(admin.ModelAdmin):
    list_display = ('bill_name', 'group_id', 'amount', 'split_type', 'date', 'status')
    list_filter = ('split_type', 'status', 'group_id')
    search_fields = ('bill_name',)

# Friend Admin
@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'friend_id', 'group_id', 'status')
    list_filter = ('status',)
    search_fields = ('user_id__name', 'friend_id__name', 'group_id__group_name')

# Vendor Admin
@admin.register(Vender)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_number', 'email', 'website')
    search_fields = ('name', 'contact_number', 'email')
    ordering = ('name',)

# Expense Admin
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'date', 'user_id', 'group_id', 'vendor', 'split_type', 'status')
    list_filter = ('status', 'split_type', 'group_id')
    search_fields = ('title', 'user_id__username', 'vendor__name')
    date_hierarchy = 'date'

# Note Admin
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at', 'updated_at')
    search_fields = ('title', 'created_by__username')  # Use the correct field
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'