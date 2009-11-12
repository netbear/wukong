from django.contrib.auth.models import User
from django.db import models
from invitation import Invitation

# User credis.
class Credit(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, unique=True)
    credits = models.IntegerField()

    def __unicode__(self):
        return u'%s %d' % (self.user, self.credits)
