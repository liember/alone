from django.db import models
from regpage.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):

    RUSSIA = 'RU'
    KASAKH = 'KZ'
    NOT_RUSSIA = 'WORLD'

    YEAR_IN_SCHOOL_CHOICES = [
        (RUSSIA, 'Russian Federation'),
        (NOT_RUSSIA, 'Not Russian'),
        (KASAKH, 'Kazakstan'),
    ]

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='profile')

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

    # TODO ADD DEFAULT IMAGE "default.png"
    image = models.ImageField(upload_to='images/', default='avatars/default.png')

    class Meta:
        ordering = ["name", "-second_name"]

    def __str__(self):
        return self.name + self.second_name
    pass

@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.create(user=kwargs['instance'])