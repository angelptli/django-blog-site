from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import DetailView, CreateView
# from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import ProfilePageForm, SignUpForm, EditProfileForm
from .forms import PasswordChangingForm, ProfilePageForm
from myblog.models import Profile


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/create_user_profile_page.html"
    # fields = '__all__'


    def form_valid(self, form):
        # Make user info availiable to the user filling out the form
        # so that saving the form will save to the correct user
        form.instance.user = self.request.user

        return super().form_valid(form)

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('home')
    fields = ['bio', 'profile_pic', 'website_url', 'facebook_url',
              'twitter_url', 'instagram_url', 'youtube_url']


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        context["page_user"] = page_user

        return context


class PasswordsChangeView(PasswordChangeView):
    # form_class = PasswordChangeForm
    form_class = PasswordChangingForm

    # success_url = reverse_lazy('home')
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})


class UserRegisterView(generic.CreateView):
    # form_class = UserCreationForm

    # Use SignUpForm from forms.py
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    
    def get_object(self):
        return self.request.user