from django.db import models

# Create your models here.

class UserInfo(models.Model):

    RUSSIA = 'RU'
    KASAKH = 'KZ'
    NOT_RUSSIA = 'WORLD'

    YEAR_IN_SCHOOL_CHOICES = [
        (RUSSIA, 'Russian Federation'),
        (NOT_RUSSIA, 'Not Russian'),
        (KASAKH, 'Kazakstan'),
    ]

    name = models.CharField(
        max_length = 20,
        help_text = "Your name")
    second_name = models.CharField(
        max_length = 20,
        help_text = "Your sec name")
    age = models.PositiveSmallIntegerField(
        help_text = "Yuor age! yep, not a birth's day")
    country = models.CharField(
        max_length=5,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=RUSSIA,
    )
    city = models.CharField( 
        max_length = 20,
        help_text = "You live")
    about = models.TextField()

    class Meta:
        ordering = ["name", "-second_name"]

    def __str__(self):
        return self.name + self.second_name


    pass