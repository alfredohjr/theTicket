from django.db import models
import uuid

# Create your models here.

class Sector(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    group = models.ForeignKey('auth.Group', related_name='sectors', on_delete=models.CASCADE, blank=True, null=True)
    sla = models.IntegerField(default=24)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Ticket(models.Model):

    CHOICES_STATUS = (
        ('OPE', 'Open'),
        ('IPR', 'In Progress'),
        ('CLO', 'Closed'),
    )

    CHOICES_PRIORITY = (
        ('LOW', 'Low'),
        ('MED', 'Medium'),
        ('HIG', 'High'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=3, default='OPE', choices=CHOICES_STATUS)
    priority = models.CharField(max_length=3, default='LOW', choices=CHOICES_PRIORITY)
    sector = models.ForeignKey(Sector, related_name='tickets', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='tickets', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket = models.ForeignKey(Ticket, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    attachment = models.FileField(upload_to='helpdesk/attachments/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body
