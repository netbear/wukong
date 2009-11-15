from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from account.models import Credit, Invitation
from account.forms import InvitationForm

@login_required
def display_credit(request):
    """ view credit info """
    try:
        user_data = Credit.objects.get(user=request.user.id)
    except Credit.DoesNotExist:
        user_data = None

    credit_dict = {
        'user_data' : user_data
    }

    context = RequestContext(request, credit_dict)

    return render_to_response('credit/view_profile.html', context)

@login_required
def invite_friends(request):
    """ invite friends to join the shop """
    init_data = {}
    is_sent = False

    if request.POST:
        form = InvitationForm(request.POST)
        invitation = form.save(commit=False)
        inv_record = Invitation.objects.create_invitation(request.user, 
                                    invitation.to_mail, invitation.message)
        is_sent = True
    else:
        form = InvitationForm()

    init_data['form'] = form
    init_data['status'] = is_sent
    
    context = RequestContext(request, init_data)

    return render_to_response('invite/send_invitation.html', context)

def register(request, invitation_code):
    """ register a invited user """
    invitation_code = invitation_code.lower()
    user = Invitation.objects.validate_invitation(invitation_code)
    if user:
        import satchmo_store.accounts.views as _
        return _.register(request)
    else:
        context = RequestContext(request)
        return render_to_response('invite/invalid_invitation.html', context)
