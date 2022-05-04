from audioop import reverse
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, FormView, TemplateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from adminportal.forms import CourseAddForm, UserAddForm

from adminportal.models import Course, User 

# Create your views
#------------------User Base Class--------------------------
# class BaseListView(LoginRequiredMixin, ListView):
#     pass

# class BaseDetailView(LoginRequiredMixin,DetailView):
#     pass

# class BaseAdminMixin(PermissionRequiredMixin):
#     raise_exception = True
#     permission_required = 'is_staff'
#     redirect_field_name ='next'

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.request.user.is_authenticated:
    #         return redirect_to_login(self.request.get_full_path(),self.get_login_url(),self.get_redirect_field_name())

    #     if not self.has_permission():
    #         return redirect('/login-1/')

        # return super(BaseAdminMixin, self).dispatch(request, *args, **kwargs)

#---------------------Course Base Class----------------------
class BaseCreateView(CreateView,ListView):
    model = Course 
    form_class = CourseAddForm
    template_name = 'adminportal/createcourse.html'
    # success_url = 'about'
    redirect = 'course_view/'

    def get_success_message(self,cleaned_data):
        self.courseName = cleaned_data['name']
        return self.courseName + "Created Successfully....!"

    # def get_success_url(self):
    #     return reverse('user_urls:admin_customized')

class BaseCourseView(ListView):
    model = Course
    template_name = 'adminportal/course_view.html'
    context_object_name = 'courses'
    # def get(self,request):  
    #     return render(request,'adminportal/course_view.html')

    # def courseview(request):        
    #     return render(request,'adminportal/course_view.html')
    # def get_queryset(self):
    #     return Course.objects.filter(courseName='Python')

class BaseUpdateView(UpdateView):
    model = Course
    form_class = CourseAddForm 
    template_name = 'adminportal/update.html'
    success_url = 'thanks/'  
    def get_success_message(self, cleaned_data):
        self.courseName = cleaned_data["name"]
        return self.courseName + "Updated Successfully...!"

    # def get_success_url(self):
    #     return reverse('user_urls:admin_customized')
class ThanksUpdateView(TemplateView):
    template_name = 'adminportal/thanks.html'




class BaseDeleteView(SuccessMessageMixin,DeleteView):
    model = Course
    template_name = 'adminportal/coursedel.html'
    context_object_name = 'delete_course'
    success_url = 'thanks/'

    def get_success_message(self, cleaned_data):
        return "Course Deleted Successfully...!"

    # def get_success_url(self):
    #     return reverse('user_urls:admin_customized')

#---------------------User Create Base Class--------------
class BaseUserCreateView(CreateView):
    model = User
    form_class = UserAddForm
    template_name = 'adminportal/createuser.html'
    # success_url = 'thanks/'

#---------------------Show User Base Class----------------
class BaseUserView(ListView):
    model = User
    template_name = 'adminportal/user_view.html'
    context_object_name = 'users'

    def get_context_data(self, *args,**kwargs):
         context = super().get_context_data(*args,**kwargs)
         context['newers']=User.objects.all().order_by('firstName')
         return context



#----------------------Multi user Authentication-------------------
class BaseLoginView(LoginRequiredMixin,ListView):
    model = User
    template_name = 'adminportal/login.html'
    context_object_name = 'users'
    
    def get_queryset(self):
        return User.objects.filter(username='admin')

    def get_success_url(self):
        return reverse('user_urls:admin_customized')

    def get_context_data(self, **kwargs):
        context = super(BaseLoginView, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context