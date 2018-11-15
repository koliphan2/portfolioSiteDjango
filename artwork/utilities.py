from .models import webContent
from PIL import image
import os


# Model Functions
def get_dictionary(propertyName=None):
    # deal with property name if added
    allObjects = webContent()
    dictionary = {}
    for obj in allObjects.objects.filter():
        dictionary[obj.propertyName] = obj.proertyValue
    return dictionary


def make_thumbnail(file_name):
    size_200 = (200,200)

    i = image.open(file_name)
    fn, fext = os.path.splitext(file_name)

    i.thumbnail(size_200)
    i.save('./media/thumbnails/{}_thumbnail.{}'.format(fn, fext))
