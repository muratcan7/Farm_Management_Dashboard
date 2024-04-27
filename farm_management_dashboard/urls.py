
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from farm_management_app.views import UserRegistrationView 


# The URL configuration for the project
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    path('api/', include('farm_management_app.urls')),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/registration/', UserRegistrationView.as_view(), name='custom_register'),

]
