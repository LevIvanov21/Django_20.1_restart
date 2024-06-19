from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Категория", help_text="Введите название категории"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание", help_text="Введите описание"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=70,
        verbose_name="Наименование",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание", help_text="Введите описание"
    )
    photo = models.ImageField(
        upload_to="",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите название категории",
        blank=True,
        null=True,
        related_name='products',
    )
    price = models.FloatField(verbose_name="Цена",help_text="Введите описание")
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создание записи",
        help_text="Укажите дату создания",
    )
    updated_at = models.DateField(
        blank=True, null=True, verbose_name="Дата последнего изменения"
    )
    manufactured_at = models.DateField(
        blank=True, null=True, verbose_name="Дата производства продукта"
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "created_at", "updated_at"]

    def __str__(self):
        return self.name

