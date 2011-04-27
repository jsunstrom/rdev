from django.http import HttpResponse, HttpResponseRedirect
from rodunu.recipe import models
from django.shortcuts import render_to_response

def index(request):
    recipes = models.Recipe.all().order('-created_on').fetch(20)
    payload = dict(recipes = recipes)
    return render_to_response('index.html', payload)

def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        ing1 = request.POST['ingredient1']
        ing2 = request.POST['ingredient2']
        recipe = models.Recipe(name = name)
        recipe.save()
        ingredient1 = models.Ingredient(recipe = recipe, name = ing1, quantity = 2.0)
        ingredient2 = models.Ingredient(recipe = recipe, name = ing2, quantity = 1.0)

        ingredient1.save()
        ingredient2.save()

        return HttpResponseRedirect(recipe.get_absolute_url())

    return render_to_response('add.html')

def view(request, recipe_key):
    recipe = models.Recipe.get(recipe_key)
    payload = dict(recipe = recipe)
    return render_to_response('view.html', payload)