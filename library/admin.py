from django.utils.html import mark_safe
from django.contrib import admin

from .models import *

# Register your models here.

admin.site.site_header = "Library Management System"
admin.site.site_title = "Library Management System"


class BookAdmin(admin.ModelAdmin):
    list_display = ["name", "author",
                    "department", "total_book", "in_stock", ]

    autocomplete_fields = ["department_id", "author_id"]
    search_fields = ["name", "author_id__name", "department_id__name"]

    def department(self, instance):
        return mark_safe(f'<a href="/library/department/{instance.department_id.id}/">{instance.department_id}</a>')

    def author(self, instance):
        return mark_safe(f'<a href="/library/author/{instance.author_id.id}/">{instance.author_id}</a>')


class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "department", "roll_no", "registrartion_no", ]

    search_fields = ["name", "roll_no", "registrartion_no"]
    autocomplete_fields = ["department_id"]

    def department(self, instance):
        return mark_safe(f'<a href="/library/department/{instance.department_id.id}/">{instance.department_id}</a>')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


class IssueBookAdmin(admin.ModelAdmin):
    list_display = ["view_Detail", "student_details",
                    "book_details", "return_date"]
    search_fields = ["student_id__name", "book_id__name"]
    autocomplete_fields = ["student_id", "book_id"]
    ordering = ["return_date"]

    def view_Detail(self, instance):
        return "Issue Details"

    def student_details(self, instance):
        return mark_safe(f'<a href="/library/student/{instance.student_id.id}/">{instance.student_id}</a>')

    def book_details(self, instance):
        return mark_safe(f'<a href="/library/book/{instance.book_id.id}/">{instance.book_id}</a>')


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(IssueBook, IssueBookAdmin)
