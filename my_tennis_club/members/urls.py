from django.urls import path # type: ignore
from . import views
from django.views.generic import TemplateView # type: ignore

urlpatterns = [
    path('', views.members, name='members'),
    path('about', views.about, name='about'),
    path('all_members', views.all_members, name="all_members"),
    path('new_member', views.new_member, name='new_member'),
    path('create', views.member_create_view, name='member_create'),
    path('success', TemplateView.as_view(template_name="success.html"), name="member_success"),
]