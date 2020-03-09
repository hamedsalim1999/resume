from django.contrib import admin
from .models import Article
from .models import Category
from .models import Form


@admin.register(Article)
class ArticlePost(admin.ModelAdmin):
    date_hierarchy = 'published_at'
    actions_on_bottom = True
    actions_selection_counter = True
    fieldsets = (
        (None, {
            'fields':(
                
            ('tittle','auther',),
            ('image', 'width_field','height_field',),
            ('main_text',),
            ('main_file',),
            ('category_list',),
           
            )

        }),
        ('Advanced options', {
             
            'fields': (('slug',),('published_at',), ('publish_status',))
            
        }),
    )



@admin.register(Category)
class Category(admin.ModelAdmin):
    actions_on_bottom = True
    actions_selection_counter = True



@admin.register(Form)
class Form_view(admin.ModelAdmin):
    list_display = ('tittle','ISread',)
    actions_on_bottom = True
    actions_selection_counter = True
    date_hierarchy = 'published_at'
    readonly_fields = [ 'tittle','message','auther','published_at','email']
    fieldsets = (
       ( None , {
            'fields':(
                
            ('tittle',),
            ('message', ),
            ('auther',),
            ('email',),
            ('published_at',),
            ('ISread',),
           
            )
            }
            ),
    )

