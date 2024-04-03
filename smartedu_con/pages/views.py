from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from courses.models import Course
from . forms import ContactForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from teachers.models import Teacher


# def index(request):
#     return render(request, 'pages/index.html')

# def about(request):
#     return render(request, 'pages/about.html')

# Class Tabanlı 
class IndexView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(available=True).order_by('-date')[:2]
        context['total_course'] = Course.objects.filter(available=True).count()
        context['total_student'] = User.objects.count()
        context['total_teacher'] = Teacher.objects.count()
        return context

class AboutView(TemplateView):
    template_name = 'pages/about.html'
    
class ContactView(SuccessMessageMixin,FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = 'Your message has been sent. Thank you!'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    