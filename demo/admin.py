from django.contrib import admin
from .models import Post
from .models import Poll
from .models import Roll
from .models import Category,Intial

class PostAdmin(admin.ModelAdmin):
    '''
            Admin View or a
    '''
    list_display = ('id','Name','Company',)
    list_filter = ('id','Name',)
    search_fields = ('Name',)
        # inlines = [
        #     Inline,
        # ]
        # raw_id_fields = ('',)
        # readonly_fields = ('',)
admin.site.register(Post,PostAdmin)


class PollAdmin(admin.ModelAdmin):
    '''
        Admin View or a
    '''
    list_display = ('id','Name','DOB')
    list_filter = ('Name',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)

admin.site.register(Poll,PollAdmin)

class RollAdmin(admin.ModelAdmin):
    '''
        Admin View or a
    '''
    list_display = ('id','Name','DOB')
    list_filter = ('Name',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)


admin.site.register(Roll, RollAdmin)


class CategoryAdmin(admin.ModelAdmin):
    '''
        Admin View for 
    '''
    list_display = ('id','Family',)
    list_filter = ('Family',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)


admin.site.register(Category, CategoryAdmin)


class IntialAdmin(admin.ModelAdmin):
    '''
        Admin View for
    '''
    list_display = ('id','Surname')
    list_filter = ('Surname',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)


admin.site.register(Intial, IntialAdmin)

