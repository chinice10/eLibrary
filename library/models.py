from django.db import models
from datetime import datetime,timedelta
import uuid

class Students(models.Model):
    mat_no = models.CharField(max_length=100,unique=True)
    fullname = models.CharField(max_length=100 ,help_text="surname first")
    study_program = models.CharField(max_length=100)
    student_dept = models.CharField(max_length=100)
    student_faculty = models.CharField(max_length=100)
    email=models.EmailField(max_length=100,help_text="student e-mail")
    def __str__(self):
        return self.fullname
        
class Staff(models.Model):
    staff_id = models.CharField(max_length=100,unique=True)
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    Email=models.EmailField(max_length=100,help_text="staff e-mail")
    def __str__(self):
        return self.fullname

class Book(models.Model):
    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=100)
    book_pages = models.PositiveIntegerField()
    book_category = models.CharField(max_length=100, help_text="category the book falls into, for instance fiction, romance")
    book_description=models.TextField(max_length=200, help_text="Short description about the book",null=True,blank=True)
    def __str__(self):
        return self.book_title

class BookInstance(models.Model):
    id=models.AutoField(primary_key=True,help_text="Book unique id across the Library")
    book=models.ForeignKey('Book', on_delete=models.CASCADE,null=True)
    book_number=models.PositiveIntegerField(null=True,help_text="Book number for books of the save kind")
    Is_borrowed = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.id} {self.book}"

def get_returndate():
    return datetime.today() + timedelta(days=8)

class Book_Issue(models.Model):
    student = models.ForeignKey('Students', on_delete=models.CASCADE)
    book_instance = models.ForeignKey('BookInstance', on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now=True,help_text="Date the book is issued")
    due_date = models.DateTimeField(default=get_returndate(),help_text="Date the book is due to")
    date_returned=models.DateField(null=True, blank=True,help_text="Date the book is returned")
    remarks_on_issue = models.CharField(max_length=100, default="Book in good condition", help_text="Book remarks/condition during issue")
    remarks_on_return = models.CharField(max_length=100, default="Book in good condition", help_text="Book remarks/condition during return")

    def __str__(self):
        return self.student.fullname + " borrowed " + self.book.book_title