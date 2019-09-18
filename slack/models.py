from django.db import models

# Create your models here.


class organizations(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50, unique=True)
    slack_org_id = models.CharField(max_length=50, unique=True)
    channel_name = models.CharField(max_length=50)
    channel_id = models.CharField(max_length=50)
    access_token = models.CharField(max_length=200)
    installation_date = models.DateTimeField('installation date')
    bot_access_token = models.CharField(max_length=200)


class users(models.Model):
    def __str__(self):
        return self.name
    org_id = models.ForeignKey(organizations, on_delete=models.CASCADE)
    slack_mem_id = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    avatar = models.CharField(max_length=500)


class shoutouts(models.Model):
    def __str__(self):
        return self.message
    giver_id = models.ForeignKey(users, on_delete=models.CASCADE)
    receiver_id = models.ForeignKey(
        users, on_delete=models.CASCADE, related_name="r_id")
    message = models.CharField(max_length=5000)
    timestamps = models.DateTimeField('timestamp')
    message_ts = models.CharField(max_length=500)
