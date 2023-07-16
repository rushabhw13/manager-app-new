from rest_framework import serializers
from .models import Menu, Staff, Todayspecial, Tables

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class TodayspecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todayspecial
        fields = '__all__'

class TablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tables
        fields = '__all__'
