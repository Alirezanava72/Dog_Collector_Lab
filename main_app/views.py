from django.shortcuts import render


dogs = [
  {'name': 'Rex', 'breed': 'golden retriever', 'description': 'playful and friendly', 'age': 3},
  {'name': 'Bella', 'breed': 'poodle', 'description': 'smart and energetic', 'age': 2},
  {'name': 'Max', 'breed': 'german shepherd', 'description': 'loyal and protective', 'age': 4},
  {'name': 'Lucy', 'breed': 'beagle', 'description': 'curious and affectionate', 'age': 1},
]


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', {
        'dogs': dogs
    })