from . import views
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('register/', views.register_view, name='register_view'),
    path('register/create/', views.register_create, name='register_create'),
    path('login/', views.login_view, name='login_view'),
    path('login/create/', views.login_create, name='login_create'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<int:id>/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', views.ProfileEdit.as_view(), name='profile_edit'),
    path('activate/<uidb64>/<token>/',views.activate_user,name='activate'
    ),
]
