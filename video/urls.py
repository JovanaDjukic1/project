
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index),
    path('download', views.download, name="download"),
    path('history', views.history, name="history"),
    path('mvcarhitecture', views.mvcarhitecture, name="mvcarhitecture"),
    path('functions', views.functions, name="functions"),
    path('laravel8', views.laravel8, name="laravel8"),
    path('composer', views.composer, name="composer"),
    path('artisan', views.artisan, name="artisan"),
    path('other', views.other, name="other"),
    path('framework', views.framework, name="framework"),
    path('php', views.php, name="php"),
    path('why', views.why, name="why"),
    path('support', views.support, name="support"),
    


]