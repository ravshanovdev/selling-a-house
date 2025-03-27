from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


CUSTOM_CHOICE2 = (
    ('active', 'Active'),
    ('sold', 'Sold')
)


class Schedule(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_prefix = models.DecimalField(max_digits=10, decimal_places=2)
    price_suffix = models.DecimalField(max_digits=10, decimal_places=2)
    price_custom = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=150)
    image1 = models.ImageField(upload_to='images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=CUSTOM_CHOICE2)
    material = models.CharField(max_length=500)
    baths = models.IntegerField(default=0, blank=True, null=True)
    garages = models.IntegerField(default=0, blank=True, null=True)
    home_area = models.IntegerField(validators=[MinValueValidator(1)], help_text='Maydon kvadrat futda (sqft)')
    year_build = models.DateTimeField(auto_now=True, blank=True, null=True)
    beds = models.IntegerField(validators=[MinValueValidator(1)], help_text='Kamida bitda yotoqxona bolishi shart')
    label = models.CharField(max_length=155)
    rooms = models.IntegerField(validators=[MinValueValidator(1)], help_text='kamida bir xonali bolishi kerak')
    lot_dimensions = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class SavedSchedule(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id}-{self.schedule}-{self.saved_at}"


