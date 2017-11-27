# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

class project(models.Model):
	author = models.ForeignKey('auth.User')
	name=models.CharField(max_length=100)
	language=models.CharField(max_length=100)
	starttime=models.DateTimeField(blank=True,null=True)
	deadline=models.DateTimeField(blank=True,null=True)
	
	published_date=models.DateTimeField(default=timezone.now)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()


	
	def __str__(self):
	        return self.name




# Create your models here.
