from django.db import models

# Create your models here.


class Suggestions(models.Model):
    contributor_name = models.CharField(max_length=50)
    suggestion_text = models.CharField(max_length=200)
    completed_status = models.BooleanField(default=False)
    vote_count = models.IntegerField(default=0)
    approved = models.IntegerField(default=0, max_length=1)
    created_date = models.DateTimeField("date created")

    def __str__(self):
        return self.suggestion_text


class Projects(models.Model):
    project_name = models.CharField(max_length=200)
    project_info = models.CharField(max_length=1000)
    project_link = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.project_name
