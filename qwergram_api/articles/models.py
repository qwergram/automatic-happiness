from django.db import models

# Create your models here.

ARTICLE_TAGS = [(choice, choice) for choice in [
    "Vent",
    "Tutorial",
    "Learning Journal",
    "Observation",
    "General",
]]


class PotentialIdeaModel(models.Model):
    """
    A potential idea that I don't have to build.
    """
    title = models.CharField(max_length=255, unique=True)
    pitch = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField()
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class CodeArticleModel(models.Model):
    """
    An article about some code challenge/tutorial or experiment that I want
    to write about.
    """
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    draft = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    original_idea = models.ForeignKey(PotentialIdeaModel, null=True)
    hidden = models.BooleanField(default=False)
    tag = models.CharField(choices=ARTICLE_TAGS, default="General", max_length=16)

    def __str__(self):
        return self.title


class RepostModel(models.Model):
    """
    A constant stream of data that I find amusing.
    """
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=500)
    date_posted = models.DateTimeField(auto_now_add=True)
    link = models.URLField()
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class StatModel(models.Model):
    """
    A model containing a piece of data.
    E.g. The health of this project.
    """
    name = models.CharField(max_length=255, unique=True)
    value = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    hidden = models.BooleanField(default=False)
