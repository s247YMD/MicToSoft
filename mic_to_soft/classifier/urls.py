from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api', views.api, name='api'),
    path('sign/signup', views.signup, name='signup'),
    path('sign/signin', views.signin, name='signin'),
    path('board/', views.board, name='board'),
    path('board/models', views.models, name='models'),
    path('board/data', views.data, name='data'),
    path('mypage/', views.mypage, name='mypage'),
    path('mypage/account', views.account, name='account'),
    path('mypage/managemodels', views.managemodels, name='managemodels'),
    path('about/', views.about, name='about'),
    path('about/help/', views.help, name='help'),
]
