from django.shortcuts import redirect, render
from django.http import HttpResponseNotFound
from django.urls import reverse
from app.models import JobPost


def job_list(request):
    job_list = JobPost.objects.all()
    context = {
        'jobs': job_list
    }
    return render(request, 'app/index.html', context)


def job_details(request, id):
    print(type(id))
    try:
        if id == 0:
            return redirect(reverse('home-page'))
        job = JobPost.objects.get(slug=id)
        print(job)
        context = {
            'job': job
        }
        return render(request, 'app/job_details.html', context)
    except Exception as ex:
        print(ex)
        return HttpResponseNotFound("Not Found")
