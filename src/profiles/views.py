from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.http import HttpResponse

User = get_user_model()

# Create your views here.
@login_required
def profile_detail_view(request, username=None):
    user = request.user
    print(user.has_perm("subscription.Basic"), "**********")
    print(user.has_perm("subscription.pro"), "**********")
    print(user.has_perm("subscription.advanced"), "**********")
    # user_group = user.groups.all()
    # print(user_group,"user_group")
    # if user_group.filter(name__icontains="basic").exits():
    #     return HttpResponse("Profile Detail View")
    profile_user_object = get_object_or_404(User, username = username)
    is_me = profile_user_object == user
    context = {
        'object': profile_user_object,
        "instance": profile_user_object,
        "is_me": is_me
    }
    return render(request, "profile/detail.html", context)

@login_required
def profile_list_view(request):
    context = {
        "object_list": User.objects.filter(is_active=True)
    }
    print(context)
    return render(request, "profile/list.html", context)
