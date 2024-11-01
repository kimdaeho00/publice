# users/views.py
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class CustomTokenObtainPairView(TokenObtainPairView):
    pass

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer

class UserInfoView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
