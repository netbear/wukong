import random
import hashlib
import re

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

SHA1_RE = re.compile('^[a-f0-9]{40}$')

class InvitationManager(models.Manager):
    """
    Custom manager for model Invitation

    The methods defined here provide shortcuts to create invitation
    codes and registration validation.
    """

    def validate_invitation(self, invitation_code):
        if SHA1_RE.search(invitation_code):
            try:
                inv = self.get(invitation_code=invitation_code)
            except self.model.DoesNotExist:
                return False
            return inv.user
        return False

    def create_invitation(self, user, to_mail, message):
        sha1 = hashlib.sha1()
        sha1.update(str(random.random()))
        salt = sha1.hexdigest()[:5]
        sha1.update(salt + to_mail)
        invitation_code = sha1.hexdigest()
        return self.create(user=user, to_mail=to_mail,
                           message=message, invitation_code=invitation_code)

class Invitation(models.Model):
    """
    The table that stores invitations sent by users in the shop.
    invitations are sent by emails provided by existing users, 
    with a message for explanation.
    """
    user = models.ForeignKey(User)
    to_mail = models.EmailField()
    message = models.TextField(blank=True)
    invitation_code = models.CharField(max_length=40)

    objects = InvitationManager()

    def __unicode__(self):
        return u"Invitation from %s to %s" % (self.user, to_mail)
