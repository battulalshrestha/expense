from rest_framework import serializers
from .models import CustomUser
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = CustomUser
        fields = ('username','email','password','phone_number', 'address', 'date_of_birth')
        
    def create(self, validated_data):
        # Create a new user with the validated data
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data.get('phone_number'),
            address=validated_data.get('address'),
            date_of_birth=validated_data.get('date_of_birth'),
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user