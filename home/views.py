from django.shortcuts import render
from django.views import generic


from .models import Course, Author, Papers


def home(request):
    return render(request, "index.html")


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_courses = Course.objects.count()  # The 'all()' is implied by default.
    num_papers = Papers.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_courses': num_courses,
                 'num_papers': num_papers
                 }
    )


class CourseListView(generic.ListView):
    model = Course
    paginate_by = 2


class AuthorDetailView(generic.DetailView):
    model = Author


class PaperListView(generic.ListView):
    model = Papers
    paginate_by = 2
