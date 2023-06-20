from django.urls import path
from .views import bankviewset



urlpatterns = [
    path('banks/', bankviewset.as_view({'get':'bank_list'}), name='bank-list'),
    path('banks/<str:branch>/', bankviewset.as_view({'get':'bank_details'}), name='bank-details'),
]
