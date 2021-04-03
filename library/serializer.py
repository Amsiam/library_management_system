from rest_framework import serializers
from .models import *


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['department_detail'] = DepartmentSerializer(
            instance.department_id).data
        return representation


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['department_detail'] = DepartmentSerializer(
            instance.department_id).data
        representation['author_detail'] = AuthorSerializer(
            instance.author_id).data
        return representation


class IssueBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueBook
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['student_detail'] = StudentSerializer(
            instance.student_id).data
        representation['book_detail'] = BookSerializer(
            instance.book_id).data
        return representation
