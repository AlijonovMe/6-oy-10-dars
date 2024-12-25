from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('type/<int:type_id>/', types, name='type_detail'),
    path('type/<int:type_id>/update', updateType, name='updateType'),
    path('type/<int:type_id>/delete', deleteType, name='deleteType'),

    path('flower/<int:flower_id>/', flower, name='flower_detail'),
    path('flower/<int:flower_id>/update', updateFlower, name='updateFlower'),
    path('flower/<int:flower_id>/delete', deleteFlower, name='deleteFlower'),

    path('type/add/', addType, name='addType'),
    path('flower/add/', addFlower, name='addFlower')
]
