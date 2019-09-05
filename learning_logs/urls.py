
# 定义learning_logs的url模式
from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^topics/$',views.topics,name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
]
app_name = 'learning_logs'