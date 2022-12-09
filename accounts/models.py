from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    """
    Represents user profile
    """

    class Meta:
        verbose_name = "نمایه کاربری"
        verbose_name_plural = "نمایه کاربری"

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='نمایه کاربری')
    # fields that are stored in User: first_name, last_name, email, date_joined

    mobile = models.CharField('تلفن همراه', max_length=11)

    MALE = 1
    FEMALE = 2
    NON_BINARY = 3
    GENDER_CHOICES = (
        (MALE, 'مرد'),
        (FEMALE, 'زن'),
        (NON_BINARY, 'نان باینری')
    )
    gender = models.IntegerField('جنسیت', choices=GENDER_CHOICES, null=True, blank=True)
    birth_date = models.DateTimeField('تاریخ تولد', null=True, blank=True)
    address = models.TextField('آدرس', null=True, blank=True)
    profile_image = models.ImageField('تصویر', upload_to='users/profile_images/', null=True, blank=True)

    balance = models.IntegerField('اعتبار', default=0)

    def __str__(self):
        return self.user.get_full_name()

    def deposit(self, amount):
        self.balance += amount
        self.save()

    def spend(self):
        # if self.balance < amount:
        #     return False
        # self.balance -= amount
        # self.save()
        return True
