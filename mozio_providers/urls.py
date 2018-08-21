from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view

from core import views

schema_view = get_swagger_view(title='Mozio API')

urlpatterns = [
    path('provider/', views.ProviderListView.as_view()),
    path('provider/', include('rest_auth.urls')),
    path('provider/registration/', include('rest_auth.registration.urls')),

    path('service-area/', views.ServiceAreaListView.as_view()),
    path('service-area/<int:pk>/', views.ServiceAreaDetailsView.as_view()),

    path('docs/', schema_view)
]
