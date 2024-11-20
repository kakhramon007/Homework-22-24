from django.db import models


class NewCategory(models.Model):
    category_name = models.CharField('Category Name', max_length=100)
    date_added = models.DateTimeField('Date Added', auto_now_add=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category Name'
        verbose_name_plural = 'Category Names'


class News(models.Model):
    title = models.CharField('Title', max_length=100)
    text = models.TextField('Text')
    category = models.ForeignKey(NewCategory, on_delete=models.CASCADE, related_name='News')
    date_added = models.DateTimeField('Date Added', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'


