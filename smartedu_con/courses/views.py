from django.shortcuts import get_object_or_404, render
from . models import Course, Category, Tag
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User


# def course_list(request):
#     courses = Course.objects.filter(available=True).order_by('-date').all
#     categories = Category.objects.all()
#     tags = Tag.objects.all()

#     context = {
#         'courses': courses, 'categories': categories, 'tags': tags
#     }

#     return render(request, 'courses/courses.html', context)


# Birden çok tekrarlanan ifadeleri bir arada topladık !
def course_list(request, category_slug=None, tag_slug=None):
    category_page = None
    tag_page = None
    categories = Category.objects.all()
    tags = Tag.objects.all()
    currentUser = request.user

    if category_slug != None:
        category_page = get_object_or_404(Category, slug=category_slug)
        courses = Course.objects.filter(
            category=category_page, available=True).order_by('-date').all
    elif tag_slug != None:
        tag_page = get_object_or_404(Tag, slug=tag_slug)
        courses = Course.objects.filter(
            tag=tag_page, available=True).order_by('-date').all
    else:
        # courses = Course.objects.all().order_by('-date').all
        if currentUser.is_authenticated:
            enrolledCourses = currentUser.courses_joined.all()
            courses = Course.objects.all().order_by('-date')
            for course in enrolledCourses:
                courses = courses.exclude(id=course.id)

        else:
            courses = Course.objects.all().order_by('-date').all

    context = {
        'courses': courses,
        'categories': categories,
        'tags': tags
    }

    return render(request, 'courses/courses.html', context)


# def category_list(request, category_slug):
#     courses = Course.objects.filter(category__slug=category_slug)
#     categories = Category.objects.all()
#     tags = Tag.objects.all()

#     context = {
#         'courses': courses,
#         'categories': categories,
#         'tags': tags
#     }

#     return render(request, 'courses/courses.html', context)


# def tag_list(request, tag_slug):
    courses = Course.objects.filter(tag__slug=tag_slug).order_by('-date')
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'courses': courses,
        'categories': categories,
        'tags': tags
    }

    return render(request, 'courses/courses.html', context)


def course_detail(request, category_slug, course_id):
    currentUser = request.user
    course = Course.objects.get(category__slug=category_slug, id=course_id)
    courses = Course.objects.all().order_by('-date').all()
    
        
    categories = Category.objects.all()

    if currentUser.is_authenticated:
        enrolledCourses = currentUser.courses_joined.all()

    else:
        enrolledCourses = courses
        
        
    context = {
        'course': course,
        'categories': categories,
        'tags': Tag.objects.all(),
        'enrolledCourses': enrolledCourses
    }

    return render(request, 'courses/course_detail.html', context)


def search_course(request):
    courses = Course.objects.filter(
        name__contains=request.GET.get('search')).order_by('-date').all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'courses': courses,
        'categories': categories,
        'tags': tags
    }
    return render(request, 'courses/courses.html', context)
