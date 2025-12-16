from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ангилалын нэр")
    description = models.TextField(blank=True, verbose_name="Тайлбар")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ангилал"
        verbose_name_plural = "Ангилалууд"
        ordering = ['name']
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Нэр")
    description = models.TextField(verbose_name="Тайлбар")
    detailed_description = models.TextField(verbose_name="Дэлгэрэнгүй тайлбар")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Үнэ"
)
    sale = models.DecimalField(
        max_digits=3,
        decimal_places=0,
        verbose_name="Хямдрал %"
    )
    stock = models.PositiveIntegerField(default=0, verbose_name="Үлдэгдэл")
    sku = models.TextField(verbose_name="Барааны код")

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name="Ангилал"
    )
    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True,
        verbose_name="Зураг"
    )
        

    is_active = models.BooleanField(default=True, verbose_name="Идэвхтэй эсэх")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Бүтээгдэхүүн"
        verbose_name_plural = "Бүтээгдэхүүнүүд"
        ordering = ['-created_at']
    def __str__(self):
        return self.name