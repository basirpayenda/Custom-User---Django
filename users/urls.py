from django.urls import path
from .views import SignupView, SignupUpdateView

app_name = 'users'
urlpatterns = [
    path('', SignupView.as_view(), name='sign_up'),
    path('update-account/<int:pk>/',
         SignupUpdateView.as_view(), name='update_users')
]

# users/update-account/
