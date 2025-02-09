from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Kategori(models.Model):
    nama = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nama)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nama

    def get_absolute_url(self):
        return reverse('kategori_detail', kwargs={'slug': self.slug})

class Tag(models.Model):
    nama = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nama)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nama

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})

class Post(models.Model):
    judul = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    konten = models.TextField()
    gambar = models.ImageField(upload_to='images/', blank=True, null=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, related_name='posts', null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    tanggal_publikasi = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.judul)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.judul

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})