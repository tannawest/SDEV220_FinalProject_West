from django.shortcuts import render, redirect
from .models import Pet, FosterFamily
from .forms import FosterRequestForm, FosterFamilyForm, PetForm

def home(request):
    return render(request, 'foster/home.html')

def add_foster_family(request):
    form = FosterFamilyForm()
    if request.method == 'POST':
        form = FosterFamilyForm(request.POST)
        if form.is_valid():
            form.save()
            if 'add_another' in request.POST:
                return redirect('add_foster_family')  # Stay on the form to add another family
            return redirect('foster_family_list')  # Redirect to the foster family list
    return render(request, 'foster/add_foster_family.html', {'form': form})


def pet_list(request):
    pets = Pet.objects.all()  # Query all pets
    return render(request, 'foster/pet_list.html', {'pets': pets})

def foster_family_list(request):
    foster_families = FosterFamily.objects.all()
    return render(request, 'foster/foster_family_list.html', {'foster_families': foster_families})

def request_foster(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    if request.method == 'POST':
        form = FosterRequestForm(request.POST)
        if form.is_valid():
            foster_request = form.save(commit=False)  # Don't save yet
            foster_request.pet = pet  # Link the pet to the foster request
            foster_request.save()  # Now save the foster request with the pet linked
            return redirect('pet_list')
    else:
        form = FosterRequestForm()
    return render(request, 'foster/request_foster.html', {'form': form, 'pet': pet})

def edit_pet(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm(instance=pet)
    return render(request, 'foster/edit_pet.html', {'form': form, 'pet': pet})

def add_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            if 'add_another' in request.POST:
                return redirect('add_pet')  # Redirect back to the form to add another pet
            return redirect('pet_list')  # Redirect to the pet list if not adding another pet
    else:
        form = PetForm()
    return render(request, 'foster/add_pet.html', {'form': form})
