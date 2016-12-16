from __future__ import unicode_literals
from ..User.models import User
from django.db import models
class Blog_CommentManager(models.Manager):
    def check_Blog(self,postData):
        print postData

        errors =[]

        if not postData['blog']:
            errors.append('blog can not empty')
        if len(postData['blog']) < 5:
            errors.append('blog must 5 characters long')
        if not postData['comment']:
            errors.append('comment can not empty')
        if len(postData['comment']) < 5:
            errors.append('comment must 5 characters long')

        response = {}
        if errors:
            response['status'] = False
            response['errors'] = errors
        else:
            response['status'] = True
            self.create(blog=postData['blog'],comment=postData['comment'])
        return response


# Create your models here.
class Blog_Comment(models.Model):
    blog = models.TextField(max_length=1000)
    comment = models.TextField(max_length=1000)
    user = models.ManyToManyField(User, related_name="user")
    Create_at = models.DateTimeField(auto_now_add=True)
    Update_at = models.DateTimeField(auto_now=True)
    objects = Blog_CommentManager()
