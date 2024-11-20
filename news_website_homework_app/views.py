from django.shortcuts import render, get_object_or_404
from .models import News, NewCategory


def main_home_page(request):
    all_categories = NewCategory.objects.order_by('category_name')
    news_latest = News.objects.order_by('-date_added')

    latest_news_order_by_category = {}
    for category in all_categories:
        for new in news_latest:
            if new.category.category_name == category.category_name:
                latest_new = new
                latest_news_order_by_category[category.category_name] = latest_new
                break

    return render(request, 'news_website_homework_app/main_home_page.html',
                  {'latest_news_order_by_category': latest_news_order_by_category})


def main_home_read_more(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news_website_homework_app/read_more.html', {'news_item': news_item})


def world_news(request):
    category_ = NewCategory.objects.get(category_name='World')
    world_news_latest = News.objects.filter(category=category_).order_by('-date_added')
    return render(request, 'news_website_homework_app/world_news.html', {'world_news_latest': world_news_latest})


def business_news(request):
    category_ = NewCategory.objects.get(category_name='Business')
    world_news_latest = News.objects.filter(category=category_).order_by('-date_added')
    return render(request, 'news_website_homework_app/business_news.html', {'world_news_latest': world_news_latest})


def technology_news(request):
    category_ = NewCategory.objects.get(category_name='Technology')
    world_news_latest = News.objects.filter(category=category_).order_by('-date_added')
    return render(request, 'news_website_homework_app/technology_news.html', {'world_news_latest': world_news_latest})


def health_news(request):
    category_ = NewCategory.objects.get(category_name='Health')
    world_news_latest = News.objects.filter(category=category_).order_by('-date_added')
    return render(request, 'news_website_homework_app/health_news.html', {'world_news_latest': world_news_latest})


def entertainment_news(request):
    category_ = NewCategory.objects.get(category_name='Entertainment')
    world_news_latest = News.objects.filter(category=category_).order_by('-date_added')
    return render(request, 'news_website_homework_app/entertainment_news.html', {'world_news_latest': world_news_latest})


def sports_news(request):
    category_ = NewCategory.objects.get(category_name='Sports')
    world_news_latest = News.objects.filter(category=category_).order_by('-date_added')
    return render(request, 'news_website_homework_app/sports_news.html', {'world_news_latest': world_news_latest})


def science_news(request):
    category_ = NewCategory.objects.get(category_name='Science')
    world_news_latest = News.objects.filter(category=category_).order_by('-date_added')
    return render(request, 'news_website_homework_app/science_news.html', {'world_news_latest': world_news_latest})


def lifestyle_news(request):
    category_ = NewCategory.objects.get(category_name='Lifestyle')
    world_news_latest = News.objects.filter(category=category_).order_by('-date_added')
    return render(request, 'news_website_homework_app/lifestyle_news.html', {'world_news_latest': world_news_latest})


def weather_news(request):
    category_ = NewCategory.objects.get(category_name='Weather')
    world_news_latest = News.objects.filter(category=category_).order_by('-date_added')
    return render(request, 'news_website_homework_app/weather_news.html', {'world_news_latest': world_news_latest})
