from django.urls import path
from accounts import views as accounts_views

urlpatterns = [
    path('login/', accounts_views.user_login, name='login'),
    path('logout/', accounts_views.user_logout, name='logout'),
    path('signup/', accounts_views.user_signup, name='signup'),
]
