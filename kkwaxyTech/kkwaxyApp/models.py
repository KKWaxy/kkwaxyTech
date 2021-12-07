from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Post(models.Model):
    
    title = models.CharField(_("Title"),null=False,blank=False,max_length=150)
    intro = models.TextField(_("Introduction"),null=False,blank=False)
    body = models.TextField(_("Body"), null=False,blank=False)
    media = models.FileField(_("Media"),upload_to="kkwaxyApp\\images")
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    updated_date = models.DateTimeField(_("Created"),auto_now=True)
    created_date = models.DateTimeField(_("Updated"),auto_now_add=True)
    
    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


        
