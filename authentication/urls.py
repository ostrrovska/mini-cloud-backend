from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views
from . import web_views

urlpatterns = [
    # API endpoints
    path('api/register/', views.register_user, name='api_register'),
    path('api/login/', views.CustomTokenObtainPairView.as_view(), name='api_login'),
    path('api/session-login/', views.session_login, name='api_session_login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/profile/', views.user_profile, name='user_profile'),
    path('api/profile/update/', views.update_profile, name='update_profile'),
    path('api/logout/', views.logout_user, name='api_logout'),
    
    # Web interface
    path('register/', web_views.register_view, name='register'),
    path('login/', web_views.login_view, name='login'),
    path('dashboard/', web_views.dashboard_view, name='dashboard'),
    path('logout/', web_views.logout_view, name='logout'),
    path('', web_views.home_view, name='home'),
]
