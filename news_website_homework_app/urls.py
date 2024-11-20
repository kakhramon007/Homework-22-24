from django.urls import path
from . import views
from .models import News, NewCategory

urlpatterns = [
    path('', views.main_home_page, name='main_home_page'),
    path(f'News/<int:news_id>/', views.main_home_read_more, name='read_more'),
    path('World/', views.world_news, name='world_news'),
    path('Business/', views.business_news, name='business_news'),
    path('Technology/', views.technology_news, name='technology_news'),
    path('Health/', views.health_news, name='health_news'),
    path('Entertainment/', views.entertainment_news, name='entertainment_news'),
    path('Sports/', views.sports_news, name='sports_news'),
    path('Science/', views.science_news, name='science_news'),
    path('Lifestyle/', views.lifestyle_news, name='lifestyle_news'),
    path('Weather/', views.weather_news, name='weather_news'),
]