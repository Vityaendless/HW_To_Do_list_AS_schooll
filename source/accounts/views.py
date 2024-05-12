from django.shortcuts import redirect, reverse, HttpResponseRedirect
from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .forms import NewUserForm


class MyLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        next_page = self.request.GET.get('next')
        reg_url = "/accounts/registration/"
        login_url = "/accounts/login/"
        if next_page:
            if reg_url in next_page or login_url in next_page:
                page_parts = next_page.split('?')
                return HttpResponseRedirect(f'/accounts/login/?{page_parts[-1]}')
        return super().dispatch(request, *args, **kwargs)


class RegisterView(CreateView):
    model = get_user_model()
    form_class = NewUserForm
    template_name = 'registration.html'

    def dispatch(self, request, *args, **kwargs):
        next_page = self.request.GET.get('next')
        reg_url = "/accounts/registration/"
        login_url = "/accounts/login/"
        if next_page:
            if login_url in next_page or reg_url in next_page:
                page_parts = next_page.split('?')
                return HttpResponseRedirect(f'/accounts/registration/?{page_parts[-1]}')
        return super().dispatch(request, *args, **kwargs)

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