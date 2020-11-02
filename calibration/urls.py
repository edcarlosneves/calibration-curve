from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('analyses/', views.AnalysisListView.as_view(), name="analyses"),
    path('analysis/<int:pk>/update/', views.AnalysisUpdate.as_view(), name="analysis_update"),
    path("analysis/<int:pk>", views.AnalysisDetailView.as_view(), name="analysis-detail"),
    path('analysis/<int:pk>/delete/', views.AnalysisDelete.as_view(), name="analysis_delete"),
]
