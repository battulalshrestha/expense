#from django.db.models import fields
from rest_framework import serializers
from .models import Login_or_Signup, Group, Group_membership, Bill_detail, Friend, Vender, Expense, Note

# Serializer for Login_or_Signup
class LoginOrSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login_or_Signup
        fields = ['id', 'name', 'username', 'email', 'password', 'phone_number']

# Serializer for Group
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'group_name', 'group_status', 'date']

# Serializer for Group_membership
class GroupMembershipSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(source='user_id', read_only=True)
    group = serializers.StringRelatedField(source='group_id', read_only=True)
    
    class Meta:
        model = Group_membership
        fields = ['id', 'user', 'group']

# Serializer for Bill_detail
class BillDetailSerializer(serializers.ModelSerializer):
    group = serializers.StringRelatedField(source='group_id', read_only=True)
    
    class Meta:
        model = Bill_detail
        fields = ['id', 'bill_name', 'group', 'amount', 'split_type', 'date', 'status']

# Serializer for Friend
class FriendSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(source='user_id', read_only=True)
    friend = serializers.StringRelatedField(source='friend_id', read_only=True)
    group = serializers.StringRelatedField(source='group_id', read_only=True)
    
    class Meta:
        model = Friend
        fields = ['id', 'user', 'friend', 'group', 'status']

# Serializer for Vender
class VenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vender
        fields = ['id', 'name', 'address', 'contact_number', 'email', 'website']

# Serializer for Expense
class ExpenseSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True)
    vendor = VenderSerializer(read_only=True)

    class Meta:
        model = Expense
        fields = ['id', 'amount', 'date', 'description', 'group', 'vendor']

# Serializer for Note
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']