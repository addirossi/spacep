from django.urls import path

from product.views import ProductsListView, ProductDetailsView, CreateProductView, UpdateProductView, DeleteProductView

urlpatterns = [
    path('', ProductsListView.as_view(), name='products-list'),
    path('<int:pk>/', ProductDetailsView.as_view(), name='product-details'),
    path('create/', CreateProductView.as_view(), name='create-product'),
    path('update/<int:pk>/', UpdateProductView.as_view(), name='update-product'),
    path('delete/<int:pk>/', DeleteProductView.as_view(), name='delete-product')
]
