# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.utils import timezone

from django.shortcuts import ( render_to_response)
from django.template import RequestContext
from django.http import HttpResponse

# HTTP Error 400
def page_error(request):

	context={}
	return render(request,'project/error.html',context)




def main(request):
	return render(request,'project/base.html')

