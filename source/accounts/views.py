from django.shortcuts import redirect, reverse
from django.contrib.auth import login, get_user_model
from django.views.generic import CreateView
from .forms import NewUserForm


class RegisterView(CreateView):
    model = get_user_model()
    form_class = NewUserForm
    template_name = 'registration.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_page = self.request.GET.get('next')
        if not next_page:
            next_page = self.request.POST.get('next')
        if not next_page:
            next_page = reverse('webapp:index')
        return next_page