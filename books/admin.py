from django.contrib import admin

# Register your models here.
from .models import Author,Category,Book,Messages,Favoritebooks

# admin.site.register(Author)
admin.site.register(Category)
# admin.site.register(Book)
admin.site.register(Messages)
admin.site.register(Favoritebooks)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
#     # 1. اختيار الأعمدة التي تظهر في الجدول
    list_display = ('title', 'autor', 'spread_date', 'language', 'number_pages')
    
#     # 2. إضافة فلاتر جانبية (مفيدة جداً للتنظيم)
    list_filter = ('language', 'category', 'spread_date')
    
#     # 3. محرك بحث داخلي (يبحث في العنوان واسم المؤلف)
    search_fields = ('title', 'autor__name') # لاحظ استخدام __ للوصول لاسم المؤلف في علاقة ForeignKey
    
#     # 4. ترتيب العرض الافتراضي (الأحدث أولاً)
    ordering = ('-spread_date',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # تقسيم الحقول إلى مجموعات (Fieldsets)
    fieldsets = (
        ('المعلومات الأساسية', {
            'fields': ('name', 'nationallty', 'photo_profile')
        }),
        ('التاريخ والسيرة', {
            'fields': ('birth_date', 'bio'),
            'classes': ('collapse',), # جعل القسم قابلاً للطي
        }),
    )

