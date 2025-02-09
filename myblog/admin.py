from django.contrib import admin
from .models import Post, Kategori, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('judul', 'tanggal_publikasi', 'kategori')
    search_fields = ('judul', 'konten')
    prepopulated_fields = {'slug': ('judul',)}

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    list_display = ('nama',)
    search_fields = ('nama',)
    prepopulated_fields = {'slug': ('nama',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('nama',)
    search_fields = ('nama',)
    prepopulated_fields = {'slug': ('nama',)}