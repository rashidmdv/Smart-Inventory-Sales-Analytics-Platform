from rest_framework import serializers
from apps.students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'roll_no', 'name', 'email', 'date_of_birth', 'joined_at', 'is_active']
