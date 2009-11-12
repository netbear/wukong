from django.forms import ModelForm
from invitation import Invitation

class InvitationForm(ModelForm):
    class Meta:
        model = Invitation
        fields = ('to_mail', 'message')

