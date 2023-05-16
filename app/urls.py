from django.urls import path
from .views import home, todo_view, todo_detail, TodoView, TodoDetail, TodoCRUD
from rest_framework.routers import DefaultRouter

router =DefaultRouter()
router.register("all", TodoCRUD)

urlpatterns = [
    path("", home),
    path("todo/", todo_view),
    path("todo/<int:id>/", todo_detail),
    path("todocb/",TodoView.as_view()),
    path("todocb/<int:id>",TodoDetail.as_view()),

] + router.urls