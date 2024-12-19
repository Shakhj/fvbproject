from django.contrib import admin
from django.urls import include,re_path
from myapp import views
urlpatterns=[
re_path(r'^admin/',admin.site.urls),
re_path(r'^$',views.display),
re_path(r'^insert/',views.insert_view),
re_path(r'^delete/(?P<id>\d+)',views.delete_view),
re_path(r'^update/(?P<id>\d+)',views.update_view),
]