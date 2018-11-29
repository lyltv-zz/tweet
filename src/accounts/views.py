from django.contrib.auth import get_user_model
<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, View

from .models import UserProfile
# Create your views here.

=======
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import FormView
# Create your views here.

from .forms import UserRegisterForm
from .models import UserProfile
>>>>>>> 95749ba6f1abb5428cb20106f9298bddb642af6f

User = get_user_model()


<<<<<<< HEAD
=======
class UserRegisterView(FormView):
    template_name = 'accounts/user_register_form.html'
    form_class = UserRegisterForm
    success_url = '/login'

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create(username=username, email=email)
        new_user.set_password(password)
        new_user.save()
        return super(UserRegisterView, self).form_valid(form)




>>>>>>> 95749ba6f1abb5428cb20106f9298bddb642af6f
class UserDetailView(DetailView):
    template_name = 'accounts/user_detail.html'
    queryset = User.objects.all()
    
    def get_object(self):
        return get_object_or_404(
                    User, 
                    username__iexact=self.kwargs.get("username")
                    )
<<<<<<< HEAD

=======
>>>>>>> 95749ba6f1abb5428cb20106f9298bddb642af6f
    def get_context_data(self, *args, **kwargs):
        context = super(UserDetailView, self).get_context_data(*args, **kwargs)
        following = UserProfile.objects.is_following(self.request.user, self.get_object())
        context['following'] = following
<<<<<<< HEAD
        return context


=======
        context['recommended'] = UserProfile.objects.recommended(self.request.user)
        return context



>>>>>>> 95749ba6f1abb5428cb20106f9298bddb642af6f
class UserFollowView(View):
    def get(self, request, username, *args, **kwargs):
        toggle_user = get_object_or_404(User, username__iexact=username)
        if request.user.is_authenticated():
            is_following = UserProfile.objects.toggle_follow(request.user, toggle_user)
        return redirect("profiles:detail", username=username)
<<<<<<< HEAD
=======
        # url = reverse("profiles:detail", kwargs={"username": username})
        # HttpResponseRedirect(url)
>>>>>>> 95749ba6f1abb5428cb20106f9298bddb642af6f
