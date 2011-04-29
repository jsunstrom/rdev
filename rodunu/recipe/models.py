from google.appengine.ext import db


class Recipe(db.Model):
    name = db.StringProperty()
    recipe = db.SelfReferenceProperty()
    created_on = db.DateTimeProperty(auto_now_add = 1)
    created_by = db.UserProperty()

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return '/recipe/%s/' % self.key()


class Ingredient(db.Model):
    recipe = db.ReferenceProperty(Recipe, collection_name='ingredients')
    quantity = db.StringProperty(required=True)
    unit = db.StringProperty()
    name = db.StringProperty(required=True)


class Direction(db.Model):
    recipe = db.ReferenceProperty(Recipe, collection_name='directions')
    order = db.IntegerProperty(required=True)
    description = db.StringProperty(required=True)