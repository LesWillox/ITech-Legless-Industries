from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class Bar(models.Model):
    #link to owner's account
    owner = models.ForeignKey(UserProfile)

    #basic bar info
    name = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=256, unique=True)
    bio = models.TextField()

    def __unicode__(self):
        return self.name


class Review(models.Model):
    #link to user that posted review
    poster = models.ForeignKey(UserProfile)

    #link to the bar being reviewed
    bar = models.ForeignKey(Bar)

    #ratings
    booze = models.IntegerField(default=0)
    beats = models.IntegerField(default=0)
    barstaff = models.IntegerField(default=0)
    bucks = models.IntegerField(default=0)

    #overall rating is average of all other ratings
    overall = models.IntegerField(default=0)

    #review details
    text_review = models.TextField()
    date_posted = models.DateTimeField()
    likes = models.IntegerField(default=0)
    favourites = models.IntegerField(default=0)

    def __unicode__(self):
        return self.text_review


class Comment(models.Model):
    #link to posting user
    poster = models.ForeignKey(UserProfile)

    #link to review being commented on
    review = models.ForeignKey(Review)

    text_comment = models.TextField()
    date_posted = models.DateTimeField()
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.text_comment


class Categories(models.Model):
    #link to bar
    bar = models.ForeignKey(Bar)

    #true or false categories (can be added to if necessary
    food = models.BooleanField(default=False)
    big_screen = models.BooleanField(default=False)
    beer_garden = models.BooleanField(default=False)
    real_ale = models.BooleanField(default=False)
    whisky_collection = models.BooleanField(default=False)
    children_welcome = models.BooleanField(default=False)
    pets_welcome = models.BooleanField(default=False)
    dartboard = models.BooleanField(default=False)
    pool_tables = models.BooleanField(default=False)
    games_machines = models.BooleanField(default=False)
    historic = models.BooleanField(default=False)
    wi_fi = models.BooleanField(default=False)
    function_room = models.BooleanField(default=False)

    def __unicode__(self):
        return self.bar.name


class News(models.Model):
    #link to bar
    bar = models.ForeignKey(Bar)

    events = models.TextField()
    news = models.TextField()

    def __unicode__(self):
        return self.news


class Photos(models.Model):
    bar = models.ForeignKey(Bar)
    image = models.ImageField(upload_to='uploads')

    def __unicode__(self):
        return self.image