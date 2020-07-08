from django.db import models
from django.utils.datetime_safe import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    name = models.CharField(max_length=100, default="example")

    # def __str__(self):
    #     return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.question.name


# Create your models here.
class Employer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    salary = models.FloatField(default=0.00)
    joined_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return self.first_name + " " + self.last_name


class Departments(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    description = models.TextField()

    def __str__(self):
        return self.name


TEA_TYPE_CHOICES =[
        ("G", "Green",),
        ("B", "Black",),
        ("R", "Red",),
    ]


class Tea(models.Model):

    code = models.PositiveIntegerField(verbose_name="Код продукта")
    name = models.CharField(max_length=100, verbose_name="Наименование")
    tea_color = models.CharField(max_length=1, choices=TEA_TYPE_CHOICES, default="B",
                                 verbose_name="Цвет")
    count = models.PositiveIntegerField(verbose_name="Колличество")
    price = models.FloatField(verbose_name="Цена", max_length=1000.0)
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return str(self.code) + " | " + self.name

    def calculate(self):
        return self.count * self.price

    def set_price(self, new_price: float) -> bool:
        if new_price < 0:
            return False
        self.price = new_price
        self.save()
        return True


