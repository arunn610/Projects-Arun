from rest_framework import serializers
from .models import Bank

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['bank_name', 'bank_id','branch', 'ifsc', 'address', 'city', 'district', 'state']
