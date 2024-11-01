from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from users.views import CustomTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('transactions.urls')),
    path('accounts/', include('accounts.urls')),
    path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
