# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import project
from cafe.models import Post
from cafe.models import cafeinfo




admin.site.register(project)


admin.site.register(Post)

admin.site.register(cafeinfo)

# Register your models here.
