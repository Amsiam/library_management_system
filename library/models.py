from django.db import models

# Create your models here.


class MainClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Department(MainClass):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(MainClass):
    name = models.CharField(max_length=100)
    department_id = models.ForeignKey(
        'department', on_delete=models.CASCADE, verbose_name="Department")
    roll_no = models.IntegerField()
    registrartion_no = models.IntegerField()
    phone_no = models.CharField(max_length=11)

    def __str__(self):
        return self.name


class Author(MainClass):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(MainClass):
    name = models.CharField(max_length=100)
    department_id = models.ForeignKey(
        'department', on_delete=models.CASCADE, verbose_name="Department")
    author_id = models.ForeignKey(
        'author', on_delete=models.CASCADE, verbose_name="Author")
    total_book = models.IntegerField(default=0)
    in_stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Book, self).save(*args, **kwargs)


class IssueBook(MainClass):

    student_id = models.ForeignKey(
        'student', on_delete=models.CASCADE, verbose_name="Student")
    book_id = models.ForeignKey(
        'book', on_delete=models.CASCADE, verbose_name="Book")

    return_date = models.DateField()

    def save(self, *args, **kwargs):
        book = Book.objects.get(id=self.book_id.id)
        book.in_stock -= 1
        book.save()
        super(IssueBook, self).save(*args, **kwargs)
