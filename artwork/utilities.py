from .models import webContent


# Model Functions
def getDictionary(propertyName=None):
        # deal with proerty name if added
        allObjects = webContent()
        dictionary = {}
        for obj in allObjects.objects.filter():
            dictionary[obj.propertyName] = obj.proertyValue
        return dictionary

