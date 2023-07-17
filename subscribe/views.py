from django.shortcuts import redirect, render
from django.urls import reverse
from subscribe.forms import SubscribeForm

from subscribe.models import Subscribe

# Create your views here.


def subscribe(request):
    context = {}
    subscribe_form = SubscribeForm()
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            return redirect(reverse('thank_you'))
    context['form'] = subscribe_form
    return render(request, 'subscribe/subscribe.html', context)


def thankyou(request):
    context = {}
    return render(request, 'subscribe/thankyou.html', context)
