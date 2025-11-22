from django.shortcuts import render, get_object_or_404
from animals.models import Animal

def display_home(request):
    return render(request, 'home.html')

# Show list of all animals
def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'animals_list.html', {'animals': animals})


# Show detail of one animal
def animal_detail(request, aid):
    a = get_object_or_404(Animal, aid=aid)
    return render(request, 'animal.html', {
        'image': a.image,
        'title': a.title,
        'description': a.description,
        'age': a.age,
        'food': a.food,
        'place': a.place,
        'donated_by': a.donated_by,
        'care_taker': a.care_taker,
    })

def display_tiger(request):
    return render(request, 'animal.html', context=tigers)

def display_lion(request):
    return render(request, 'animal.html', context=lions)

def display_monkey(request):
    return render(request, 'animal.html', context=monkeys)

def display_snake(request):
    return render(request, 'animal.html', context=snakes)

def display_bird(request):
    return render(request, 'animal.html', context=birds)



