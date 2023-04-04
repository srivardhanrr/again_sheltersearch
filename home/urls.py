from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = (
    path("", views.HomeView.as_view(), name="home"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("policy/<called>", views.PolicyView.as_view(), name="policies"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    # path("signup/", views.SignUpView.as_view(), name="signup"),
    # path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.logout_user, name="logout"),
)