"""amat_rick_and_morty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.home, name='home'),
    path("room", views.room, name='room'),
    path('api_schema/', get_schema_view(title='API schema',
                                        description="Rick & Morty REST API guide"), name="api_schema"),
    path("swagger-ui/", TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url': 'api_schema'}
    ), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('charachters/compare/<str:first_character_id>/<str:second_character_id>', views.compare_character),
    path('charachters/compare_to_csv/<str:first_character_id>/<str:second_character_id>', views.compare_two_character_to_csv)
]

