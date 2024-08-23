# courses/urls.py
from django.urls import path
from .views import (
    CourseListCreateView,
    CourseDetailView,
    CourseInstanceListCreateView,
    CourseInstanceDetailView,
    api_root  # Ensure it's correctly imported
)

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('instances/<int:year>/<int:semester>/', CourseInstanceListCreateView.as_view(), name='instance-list-create'),
    path('instances/<int:year>/<int:semester>/<int:course_id>/', CourseInstanceDetailView.as_view(), name='instance-detail'),
    path('', api_root, name='api-root'),  # Include this if you defined api_root
]

