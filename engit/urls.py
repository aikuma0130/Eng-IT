from django.conf.urls import include, url

from . import views

app_name = 'engit'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(
        r'^articles/(?P<page>\d+)/$',
        views.article_list,
        name='article_list_pagenated'
    ),
    url(r'^articles/$', views.article_list, name='article_list'),
    url(r'^collects/', views.collects, name='collects'),
]
