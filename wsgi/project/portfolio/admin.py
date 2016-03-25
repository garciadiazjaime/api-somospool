from django.contrib import admin
import nested_admin

from .models import Category, Project, Block, Image

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'order')

class ChoiceImage(nested_admin.NestedStackedInline):
	model = Image
	extra = 1

class ChoiceBlock(nested_admin.NestedStackedInline):
	model = Block
	extra = 1
	inlines = [ChoiceImage]

class ProjectAdmin(nested_admin.NestedModelAdmin):
	list_display = ('id', 'title', 'subtitle', 'status', 'order')
	search_fields = ['code', 'name']
	inlines = [ChoiceBlock]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
