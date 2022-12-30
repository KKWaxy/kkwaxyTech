from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

def user_directory_path(instance: models.Model, filename: str)->str:
    
    return 'users/{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(_("Avatar"),upload_to=user_directory_path, default="")
    bio = models.TextField(_("Biographie"), max_length=500, null=True, blank=True)
   # cv = models.FieldFile()
    
class Tag(models.Model):
    name = models.CharField(_("Nom"),max_length=25,null=False,blank=False)
    updated_date = models.DateTimeField(_("Created"),auto_now=True)
    created_date = models.DateTimeField(_("Updated"),auto_now_add=True)
    
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
    
    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    
    title = models.CharField(_("Title"),null=False,blank=False,max_length=150)
    intro = models.TextField(_("Introduction"),null=False,blank=False)
    body = models.TextField(_("Body"), null=False,blank=False)
    media = models.FileField(_("Media"),upload_to="kkwaxyApp\\images")
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag,null=False,blank=False)
    updated_date = models.DateTimeField(_("Created"),auto_now=True)
    created_date = models.DateTimeField(_("Updated"),auto_now_add=True)
    
    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ["-updated_date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

