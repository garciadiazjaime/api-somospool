from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)

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
    status = models.CharField(choices=STATUS_TYPES, default='CREATED', max_length=20)

    def __unicode__(self):
		return "%s" % (self.title)

class Block(models.Model):
    BLOCK_TYPES = (
        ('COVER', 'COVER'),
        ('INTRO', 'INTRO'),
        ('DESCRIPTION', 'DESCRIPTION'),
        ('IMAGE', 'IMAGE'),
    )
    type = models.CharField(choices=BLOCK_TYPES, default='COVER', max_length=20)
    content = models.TextField(null=True, blank=True)
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return "%s" % self.type

class Image(models.Model):
    url = models.URLField(max_length=500, default='')
    block = models.ForeignKey(Block, default='')

    def __unicode__(self):
        return "%s" % self.url
