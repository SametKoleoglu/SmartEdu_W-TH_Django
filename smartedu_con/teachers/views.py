from django.views.generic import ListView
from django.views.generic.detail import DetailView
from teachers.models import Teacher
from courses.models import Course


# Create your views here.

class TeachersViews(ListView):
    model = Teacher
    template_name = 'teachers/teachers.html'
    context_object_name = 'teachers'
    paginate_by = 2
    
    
class TeacherViews(DetailView):
    model = Teacher
    template_name = 'teachers/teacher.html'
    context_object_name = 'teacher'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(available=True, teacher=self.object)
        return context
    