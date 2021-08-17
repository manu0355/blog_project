from django.db import models
# from django.db.models.signals import pre_save


class Post(models.Model):
    title = models.CharField(max_length= 50)
    slug = models.SlugField()
    intro = models.TextField(max_length= 100)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']
    
    def __str__(self):
        return self.title


# def slug_generator(sender,instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = 'SLUG'

# pre_save.connect(slug_generator, sender = Post)