from dataclasses import fields
from rest_framework import serializers
from api.models import Student

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name','roll','city')