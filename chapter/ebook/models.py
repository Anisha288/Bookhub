from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50)
    category_img = models.ImageField(upload_to='pic_upload',verbose_name="Put Category Image file")
    describe = models.TextField(verbose_name='Description Text')


def __str__(self):
    return self.title

class Meta:
    verbose_name_plural = "Categories"


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    bookname = models.CharField(max_length=264)
    author = models.CharField(max_length=30)
    mainimage = models.ImageField(upload_to='pic_upload',verbose_name="Put Image file")
    pdf = models.FileField(upload_to='pdf_upload',verbose_name="Put PDF file")
    preview_text = models.TextField(verbose_name='Preview Text')

    def __str__(self):
        return self.bookname


