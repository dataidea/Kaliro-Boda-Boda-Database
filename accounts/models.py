from django.db import models


class Member(models.Model):
    surname = models.CharField(max_length=25)
    given_name = models.CharField(max_length=25)
    designation = models.CharField(max_length=25)
    stage = models.CharField(max_length=25)
    place_of_residence = models.CharField(max_length=25)
    district = models.CharField(max_length=25)
    subcounty = models.CharField(max_length=25)
    parish = models.CharField(max_length=25)
    contact = models.CharField(max_length=15)
    date_of_issue = models.DateTimeField("date of id card issue")
    date_of_expiry = models.DateTimeField("date of expiry of id card")
    card_no = models.IntegerField()

    def __str__(self):
        return f"{self.surname} {self.given_name}"
