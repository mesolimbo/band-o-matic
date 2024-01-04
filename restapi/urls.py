from django.urls import path
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from restapi import views


urlpatterns = [
    path('random/', views.random_band_endpoint, name='random_band_endpoint'),
    path('openapi.html', views.openapi, name="openapi"),
    path('category/', views.CategoryListCreateAPIView.as_view()),
    path('category/<int:pk>/', views.CategoryUpdateDeleteAPIView.as_view()),
    path('word/', views.WordListCreateAPIView.as_view()),
    path('word/<int:pk>/', views.WordUpdateDeleteAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include_docs_urls(title="Bands.Twerk.Click REST API")),
]
