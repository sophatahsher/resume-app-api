"""URL mapping for the user API."""
from django.urls import path

from user import views
# from rest_framework_simplejwt import views as jwt_views


app_name = 'user'

urlpatterns = [
    #
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    #
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me')
]
