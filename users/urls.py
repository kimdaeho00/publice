from django.urls import path
from .views import CustomTokenObtainPairView, SignUpView, UserInfoView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('info/<int:pk>/', UserInfoView.as_view(), name='user_info'),
]
