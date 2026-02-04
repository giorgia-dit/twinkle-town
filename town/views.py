from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.views import LoginView
from django.urls.base import reverse
from django.http.response import HttpResponse

from town.forms import CustomAuthenticationForm
from .models import User, House

class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class TownPageView(ListView):
    model = House
    template_name = 'town.html'
    context_object_name = 'houses'

    def get_queryset(self):
        return super().get_queryset().select_related('owner')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['full_town'] = not User.objects.filter(last_login__isnull=True).exists()
        return context


class UserListView(ListView):
    model = User
    template_name = 'users.html'
    context_object_name = 'users'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.exclude(pk__in=[1, 2])
        if 'shuffle' in self.request.GET:  
            return queryset.order_by('?') 
        return queryset.order_by('first_name')
    

class HouseDetailView(DetailView):
    model = House
    template_name = 'house_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.GET.get('username', '')
        context['username'] = username
        return context
    

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'partials/login_form.html'

    def form_invalid(self, form):
        if self.request.headers.get('HX-Request'):
            return self.render_to_response(self.get_context_data(
                form=form,
                username=form.data.get('username'))
            )
        return super().form_invalid(form)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.headers.get('HX-Request'):
            response = HttpResponse('', headers={'HX-Redirect': self.get_success_url()})
        return response

    def get_success_url(self):
        return reverse('town')
    

class ThanksPageView(TemplateView):
    template_name = 'thanks.html'