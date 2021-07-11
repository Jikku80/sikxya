from django.urls import path, include

from . import views

urlpatterns = [
    path('list/', views.ManageCourseListView.as_view(), name='list'),
    path('create/', views.CourseCreateView.as_view(), name='create'),
    path('search/', views.SearchResultsListView.as_view(), name='search_results'),
    path('<pk>/edit/', views.CourseUpdateView.as_view(), name='edit'),
    path('<pk>/delete/', views.CourseDeleteView.as_view(), name='delete'),
    path('<pk>/module/', views.CourseModuleUpdateView.as_view(), name='update'),
    path('module/<int:module_id>/content/<model_name>/create/',
         views.ContentCreateUpdateView.as_view(), name='content_create'),
    path('module/<int:module_id>/content/<model_name>/<id>/',
         views.ContentCreateUpdateView.as_view(), name='content_update'),
    path('content/<int:id>/delete/',
         views.ContentDeleteView.as_view(), name='content_delete'),
    path('module/<int:module_id>/',
         views.ModuleContentListView.as_view(), name='content_list'),
    path('module/order/', views.ModuleOrderView.as_view(), name='module_order'),
    path('content/order', views.ContentOrderView.as_view(), name='content_order'),
    path('subject/<slug:subject>/', views.CourseListView.as_view(),
         name='course_list_subject'),
    path('<slug:slug>/', views.CourseDetailView.as_view(), name='course_detail'),
]
