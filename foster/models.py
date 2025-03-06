from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.IntegerField()
    health_status = models.TextField()
    special_needs = models.TextField(blank=True, null=True)
    date_taken_in = models.DateField()

    def __str__(self):
        return self.name

class FosterFamily(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField()
    address = models.TextField()
    number_of_pets = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class FosterRequest(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    family_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
    request_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.family_name} - {self.pet.name} ({self.status})"
