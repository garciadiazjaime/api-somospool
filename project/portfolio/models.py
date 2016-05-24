from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)
    order = models.IntegerField(null=True, blank=True, default=1)

    def __unicode__(self):
        return "%s" % (self.name)

class Project(models.Model):
    STATUS_TYPES = (
        ('CREATED', 'CREATED'),
        ('DRAFT', 'DRAFT'),
        ('PUBLISHED', 'PUBLISHED'),
        ('DISABLED', 'DISABLED'),
    )
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=120)
    categories = models.ManyToManyField(Category)
    order = models.IntegerField(null=True, blank=True, default=1)
    status = models.CharField(choices=STATUS_TYPES, default='CREATED', max_length=20)
    cover = models.URLField(max_length=500, default='')

    def __unicode__(self):
		return "%s" % (self.title)

class Block(models.Model):
    BLOCK_TYPES = (
        ('INTRO', 'INTRO'),
        ('IMAGE', 'IMAGE'),
        ('DESCRIPTION', 'DESCRIPTION'),
        ('TEXT', 'TEXT'),
        ('SLIDER', 'SLIDER'),
        ('IMAGE_IMAGE', 'IMAGE_IMAGE'),
        ('IMAGE_TEXT', 'IMAGE_TEXT'),
        ('TEXT_IMAGE', 'TEXT_IMAGE'),
        ('SLIDER_TEXT', 'SLIDER_TEXT'),
        ('TEXT_SLIDER', 'TEXT_SLIDER'),
        ('SLIDER_IMAGE', 'SLIDER_IMAGE'),
        ('IMAGE_SLIDER', 'IMAGE_SLIDER'),
    )
    type = models.CharField(choices=BLOCK_TYPES, default='IMAGE', max_length=20)
    text = models.TextField(null=True, blank=True, default='')
    order = models.IntegerField(null=True, blank=True, default=1)
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return "%s" % self.type

class Image(models.Model):
    url = models.URLField(max_length=500, default='')
    block = models.ForeignKey(Block, default='')

    def __unicode__(self):
        return "%s" % self.url
