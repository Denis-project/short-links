from django.urls import include, path
from .views import shortlinksappCreate, shortlinksappList, shortlinksappDetail, shortlinksappUpdate, shortlinksappDelete


urlpatterns = [
    path('create/', shortlinksappCreate.as_view(), name='create-shortlinksapp'),
    path('', shortlinksappList.as_view()),
    path('<int:pk>/', shortlinksappDetail.as_view(), name='retrieve-shortlinksapp'),
    path('update/<int:pk>/', shortlinksappUpdate.as_view(), name='update-shortlinksapp'),
    # path('delete/<int:pk>/', shortlinksappDelete.as_view(), name='delete-shortlinksapp')
]