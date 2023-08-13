from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.db.models import Q
from django.template.defaultfilters import slugify
from .utils import get_random_code


# Create your models here.
class Profile(models.Model):
    # first name of the profile
    first_name = models.CharField(max_length=50, blank=True)
    # last name of the profile
    last_name = models.CharField(max_length=50, blank=True)
    # each profile has only one user by One to One relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # bio of the profile
    biography = models.TextField(default="no biography added...", max_length=400)
    # email of the profile
    email = models.EmailField(max_length=150, blank=True)
    # profile picture of the profile, install pillow to hold images
    avatar = models.ImageField(default="avatar.png", upload_to="avatars/")
    # slug field will be used for creating url's for each profile
    slug = models.SlugField(unique=True, blank=True)

    PROFILE_TYPE = [
        ('Organizer', 'Organizer'),
        ('Volunteer', 'Volunteer'),
    ]
    # status field to hold profile status of model
    type = models.CharField(choices=PROFILE_TYPE, default='Volunteer', max_length=200)
    # updated field to hold when profile is updated
    updated = models.DateTimeField(auto_now=True)
    # created field to hold when profile is created
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}"

    __initial_first_name = None
    __initial_last_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initial_first_name = self.first_name
        self.__initial_last_name = self.last_name

    def save(self, *args, **kwargs):
        #exists
        slug_exists = False
        to_slug = self.slug
        # bugfix for slugified urls
        # make sure slug does change after username changed
        if (self.first_name != self.__initial_first_name or
            self.last_name != self.__initial_last_name or
            self.slug==""):
            # check first name and last name exists
            if self.first_name and self.last_name:
                # slugify with first name and last name
                to_slug = slugify(str(self.first_name) + " " + str(self.last_name))
                # check if slug exists
                slug_exists = Profile.objects.filter(slug=to_slug).exists()
                # create another slug as far as a slug exists
                while slug_exists:
                    # create another slug
                    to_slug = slugify(to_slug + " " + str(get_random_code()))
                    # check this slug exists or not
                    slug_exists = Profile.objects.filter(slug=to_slug).exists()
            else:
                to_slug = str(self.user)
        # update current slug
        self.slug = to_slug
        super().save(*args, **kwargs)



