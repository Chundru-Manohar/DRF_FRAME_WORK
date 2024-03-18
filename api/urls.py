from .import views
from django.urls import path

urlpatterns = [
   path('',views.apiOverview,name='apiOverview'),
   path('list/',views.showall,name='product-list'),
   path('details/<int:pk>/',views.ViewProduct,name='details'),
   path('create/',views.createProduct,name='create'),
   path('update/<int:pk>/',views.updateProduct,name='update'),
   path('delete/<int:pk>/',views.deleteProduct,name='delete'),

]
