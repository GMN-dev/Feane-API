from django.db import models
from django.urls import reverse
from .utils import upload_image_formater


# Create your models here.
class tag(models.Model):
    tag = models.CharField(max_length=50)
    
    class Meta:
        db_table = "tbl_tag"
        verbose_name_plural = ("s")

    def __str__(self):
        return self.tag




class menu(models.Model): 
    image = models.ImageField(upload_to=upload_image_formater, blank=True, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    tag = models.ForeignKey(tag, on_delete=models.CASCADE, related_name="tags")

    class Meta:
        db_table = "tbl_menu"
        managed = True

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"pk": self.pk})
