from django.urls import path
from . import views

urlpatterns = [
    path ("", views.home),
    path ("fakultet", views.fakultetView, name ="fakultetURL"),
    path ("maglumat", views.maglumatView, name ="maglumatURL"),
    path ("dashbord", views.dashbordView, name ="dashbordURL"),
    path ("biz", views.bizView, name ="bizURL"),
    path ("taze", views.tazeView, name ="tazeURL"),
    path ("yas",views.yasView, name = "yasURL"),
    path ("t1",views.t1View, name = "t1URL"),
    path ("t2",views.t2View, name = "t2URL"),
    path ("t3",views.t3View, name = "t3URL"),
    path ("tazelik",views.tazelikView, name = "tazelikURL")
    
]