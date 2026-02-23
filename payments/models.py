from django.db import models
from students.models import Student

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.IntegerField()
    payment_method = models.CharField(max_length=50)
    screenshot = models.ImageField(upload_to="payments/")
    created_at = models.DateTimeField(auto_now_add=True)
