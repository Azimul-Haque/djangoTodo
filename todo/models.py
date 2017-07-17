from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
import uuid


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, default=uuid.uuid4)

    def __str__(self):
	    return self.name

class Priority(models.Model):
    name = models.CharField(max_length=200, unique=True, default=uuid.uuid4)

    def __str__(self):
        return self.name



class Task(models.Model):
    created_by = models.ForeignKey(User, unique=False)
    title = models.CharField(max_length=300)
    text = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    is_pinned = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(editable=False, default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo:list', kwargs={'pk': self.pk})