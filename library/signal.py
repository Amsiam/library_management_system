from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import IssueBook, Book


@receiver(pre_delete, sender=IssueBook)
def my_handler(sender, instance, **kwargs):
    book = Book.objects.get(id=instance.book_id.id)
    book.in_stock += 1
    book.save()
