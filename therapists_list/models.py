from django.db import models

class Therapists(models.Model):
    firstname = models.CharField('firstname', max_length=255)
    lastname = models.CharField('lastname', max_length=255)
    phone = models.CharField('phone', max_length=255)
    email = models.CharField('email', max_length=255)
    experience = models.IntegerField('experience')
    degree = models.CharField('education', max_length=255)
    about = models.TextField('about')
    age = models.IntegerField('age')
    city = models.CharField('city', max_length=255)
    sex = models.CharField('sex', max_length=6)
    photo = models.ImageField('photo', upload_to='therapists_photo/')

    def __str__(self):
        return self.firstname + ' ' + self.lastname

    def get_absolute_url(self):
        return f'/therapists/{self.id}'

    class Meta:
        verbose_name = 'Therapist'
        verbose_name_plural = 'Therapists'


