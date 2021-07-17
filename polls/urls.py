# from django.urls import path
#
# from . import views
#
# # app_name = 'polls' #app命名空间，html可直接使用url'polls:index'访问inde视图，对于detail、results、vote同理
# app_name='polls'
#
# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     # path('<int:question_id>/vote/', views.vote, name='vote'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]