from django.db import models


class Types(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Nomi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Turlar "
        verbose_name_plural = "Turlar"
        ordering = ['-id']


class Flowers(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nomi")
    description = models.TextField(default="Ma'lumot qo'shilmadi.", verbose_name="Tavsifi")
    price = models.IntegerField(verbose_name="Narxi")
    count = models.IntegerField(default=0, verbose_name="Soni")
    published = models.BooleanField(default=False, verbose_name="Nashr etilgan")
    type = models.ForeignKey(Types, on_delete=models.CASCADE, verbose_name="Turi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Gullar "
        verbose_name_plural = "Gullar"
        ordering = ['-id']
