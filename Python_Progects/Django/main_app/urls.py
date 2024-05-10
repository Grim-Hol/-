from django.urls import path
from .import views
from .views import Paper_News,post_news,RegisterUsers,LoginView,LoginUser, logout_us
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', Paper_News.as_view(), name='home'),
    path('body', views.forms, name='main_text'),
    path('main_txt/<int:post_id>/',post_news, name = 'body_txt'),
    path('reg', RegisterUsers.as_view(),name = 'registration'),
    path('aut', LoginUser.as_view(), name = 'aut'),
    path('logout/',logout_us, name='logout')
]