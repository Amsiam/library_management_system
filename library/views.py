from django.shortcuts import render

from rest_framework import generics, viewsets
from rest_framework.response import Response

from .models import *
from .serializer import *


class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class IssueBookView(viewsets.ModelViewSet):
    queryset = IssueBook.objects.all()
    serializer_class = IssueBookSerializer
