from django.db import models
from django.utils.html import mark_safe
from django.conf import settings
from datetime import date


# Create your models here.

# These will be my tables.


class webContent(models.Model):
    propertyName = models.CharField(max_length=200)
    propertyValue = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.propertyName

    def getDictionary(self, propName=None):
        if propName is None:
            allObjects = self.__class__.objects.all()
            dictionary = {}
            for obj in allObjects:
                    dictionary[obj.propertyName] = obj.propertyValue
            return dictionary
        else:
            singleObject = self.__class__.objects.filter(propertyName = propName)
            return singleObject


class Artpiece(models.Model):
    # id is automatically added as a primary key with an incrementing number

    # title
    title = models.CharField(max_length=200)

    # creation date
    create_date = models.DateField(
        'date created',
        default = date.today,
        blank = True,
        )

    # medium of artpiece
    medium_choices = (
        ('drawing', 'Drawings'),
        ('paint', 'Paintings'),
        ('digital', 'Digital Artwork'),
        ('animation', 'Animation')
    )

    medium = models.CharField(
        max_length=10,
        choices=medium_choices,
        default='drawing'
    )

    # actual image address
    image = models.FileField("Image File", upload_to='media')

    # description and extra notes
    description = models.TextField()

    def image_tag(self):
        return mark_safe("{}/{}".format(settings.MEDIA_URL, self.image))

    image_tag.short_description = "Image"

    # toString of Model
    def __str__(self):
        return self.title



