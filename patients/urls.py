from django.urls import path

from .views import new_patient,view_patient,view_results,PatientListView


urlpatterns=[
    path('',PatientListView.as_view(),name='patient_mgt'),
    path('new/',new_patient,name='new_patient'),
    path('view/<str:mrn>/',view_patient,name='view'),
    path('results/<int:test_id>/<int:patient_id>/',view_results,name='results'),
]