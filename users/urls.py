from django.contrib.auth import urls
from . import views
from django.urls import path, include

app_name = "users"

urlpatterns = [

    path("", include(urls), name=urls),
    path("register/", views.register, name="register"),
    path("register/profile/<int:user_id>/", views.profile_register, name='register_profile'),
    path("profile/<int:user_id>/", views.profile, name="profile"),
    path("edite_profile/<int:user_id>/", views.edite_profile, name="edite_profile")

]