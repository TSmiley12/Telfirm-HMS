from django.urls import path, re_path
from .views import index
from .utils import service_worker,manifest,offline,RobotsTxtView

urlpatterns=[
    path('',index,name='home'),
    re_path(r'^serviceworker\.js$', service_worker, name='sw'),
    re_path(r'^manifest\.json$', manifest, name='manifest'),
    path('offline/',offline,name='offline'),
    re_path(r'^robots\.txt$', RobotsTxtView.as_view()),
]