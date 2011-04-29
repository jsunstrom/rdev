from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from google.appengine.api import users
from rodunu.recipe import models
from rodunu.utils.errors import Errors
from rodunu.utils.query import fetch_entities
from rodunu.utils.regex import is_fraction
import re

def index(request):
    recipes = models.Recipe.all().order('-created_on').fetch(20)
    payload = dict(recipes = recipes)
    return render_to_response('index.html', payload)

def add(request):
    errors = Errors()
    if request.method == 'POST':
        name = request.POST['name']
        recipe = models.Recipe(name = name)

        if users.get_current_user():
            recipe.created_by = users.get_current_user()

        recipe.save()

        regx = re.compile('(qty)(\d+)', re.IGNORECASE)
        for key, value in request.POST.iteritems():
            match = regx.search(key)
            if match and len(request.POST['qty%s'%match.group(2)]) != 0:
                id = match.group(2)
                qid = 'qty%s' % id
                qty = request.POST[qid]
                name = request.POST['ingredient%s' % id]
                unit = request.POST['unit%s' % id]
                quantity = ""
                if is_fraction(qty):
                    quantity = qty
                else:
                    errors.data[qid] = 'Quantity must be a whole number or fraction. Ex. 1 1/3'


                if not errors.has_errors():
                    ing = models.Ingredient(recipe = recipe, \
                                            name = name, \
                                            quantity = quantity, \
                                            unit = unit)
                    ing.save()

        if not errors.has_errors():
            return HttpResponseRedirect(recipe.get_absolute_url())

    if errors.has_errors():
        print errors.data

    return render_to_response('add.html', {'errors':errors.data})


def view(request, recipe_key):
    recipe = models.Recipe.get(recipe_key)
    ingredients = fetch_entities(models.Ingredient.all().filter('recipe',recipe))
    payload = dict(recipe = recipe, ingredients = ingredients)
    return render_to_response('view.html', payload)