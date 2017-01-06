from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import datetime, timedelta

class Employer(models.Model):
	user=models.ForeignKey(User,editable=True, unique=True)
	company=models.CharField(max_length=50)
	compdesc=models.CharField(max_length=500)
	compwebsite=models.CharField(max_length=50)
	compemail=models.CharField(max_length=50)
	compcontact=models.CharField(max_length=50)
	def __unicode__(self):
		return self.company
	def get_absolute_url(self):
		return reverse('jobboard:company-detail', args=(self.pk,))
		
class Employee(models.Model):
	user=models.ForeignKey(User,editable=True)
	email=models.CharField(max_length=50)
	reciever=models.BooleanField(choices=((1,"True"),(0,"False")),default=1,)
	def __unicode__(self):
		return unicode(self.user)
	def get_absolute_url(self):
		return reverse('jobboard:profile-detail', args=(self.pk,))
		
class Post(models.Model):
	job_types=(
	('Full Time','Full Time'),
	('Part Time','Part Time'),
	('Internship','Internship'),)
	employer=models.ForeignKey(Employer,editable=True)
	title=models.CharField(max_length=50)
	postdesc=models.CharField(max_length=500)
	posttype=models.CharField(max_length=50, choices=job_types)
	wage=models.CharField(max_length=50)
	pubdate=models.DateTimeField(default=datetime.now())
	expdate=models.DateTimeField(default=datetime.now()+timedelta(days=90))
	active=models.BooleanField(choices=((1,"True"),(0,"False")),default=1,)
	def __unicode__(self):
		return unicode(self.title)
	def get_absolute_url(sefl):
		return reverse('jobboard:post-detail', args=(self.pk,))
		
		
		
	
