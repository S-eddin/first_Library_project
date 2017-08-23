# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import  BookInstance,Genre, Author ,Book 
 

admin.site.register( BookInstance)

admin.site.register(  Author)

admin.site.register(Genre)

admin.site.register(Book )







