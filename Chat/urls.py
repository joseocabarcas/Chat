from django.conf.urls import include, url
from django.contrib import admin
from comment.views import IndexView,HomeView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view()),
    url(r'^home/$',HomeView.as_view()),
    url(r'^crear-comentario/$', 'comment.views.create_comment'),
]