from django.shortcuts import render, redirect, get_object_or_404
from .forms import FosterRequestForm, FosterFamilyForm, PetForm
from .models import Pet, FosterFamily

def home(request):
    return render(request, 'foster/home.html')

def add_foster_family(request):
    if request.method == 'POST':
        form = FosterFamilyForm(request.POST)
        
        if form.is_valid():
            # Save the new foster family
            form.save()
            
            # Check if the "Add Another Family" button was clicked
            if request.POST.get('action') == 'add_another_family':
                # If "Add Another Family" clicked, reload the form to add another family
                return redirect('foster:add_foster_family')
            else:
                # If "Add Family" clicked, redirect to the foster family list
                return redirect('foster:foster_family_list')
    else:
        form = FosterFamilyForm()

    return render(request, 'foster/add_foster_family.html', {'form': form})


def pet_list(request):
    pets = Pet.objects.all()  # Query all pets
    return render(request, 'foster/pet_list.html', {'pets': pets})

def foster_family_list(request):
    foster_families = FosterFamily.objects.all()
    return render(request, 'foster/foster_family_list.html', {'foster_families': foster_families})

def request_foster(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)  # Get the pet by id
    
    if request.method == 'POST':
        form = FosterRequestForm(request.POST)
        if form.is_valid():
            # Save the foster request (you can implement your logic here)
            form.save()
            return redirect('foster:pet_list')  # Redirect back to the pet list after request
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
            form.save()  # Save the new pet
            
            action = request.POST.get('action')  # Get the action from the button clicked

            if action == 'add_pet':
                # If 'Add Pet' clicked, redirect to pet list page
                return redirect('foster:pet_list')
            elif action == 'add_another_pet':
                # If 'Add Another Pet' clicked, clear the form and stay on the page
                form = PetForm()  # Reset the form for another entry
                return render(request, 'foster/add_pet.html', {'form': form})
    else:
        form = PetForm()  # If GET request, show an empty form
    
    return render(request, 'foster/add_pet.html', {'form': form})
