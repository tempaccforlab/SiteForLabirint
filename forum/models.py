from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='author')
    votes_total = models.IntegerField(default=0)
    pluses = models.ManyToManyField(User,blank=True,related_name='pluses')
    minuses = models.ManyToManyField(User,blank=True,related_name='minuses')
    is_published = models.BooleanField(default=True)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]



class Comment(models.Model):
    class Meta:
        db_table = "comments"

    path = ArrayField(models.IntegerField())
    post_id = models.ForeignKey(Post,on_delete=models.PROTECT)
    user_id = models.ForeignKey(User,on_delete=models.PROTECT)
    content = models.TextField('Комментарий ')
    pub_date = models.DateTimeField('Дата комментария', default=timezone.now)
    #username = models.ManyToManyField()

 

