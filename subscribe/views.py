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
            print("Valid Form")
            print(subscribe_form.cleaned_data)
            email = subscribe_form.cleaned_data['email']
            first_name = subscribe_form.cleaned_data['first_name']
            last_name = subscribe_form.cleaned_data['last_name']
            subscribe = Subscribe(first_name=first_name,
                                  last_name=last_name, email=email)
            subscribe.save()
            return redirect(reverse('thank_you'))
    context['foam'] = subscribe_form
    return render(request, 'subscribe/subscribe.html', context)


def thankyou(request):
    context = {}
    return render(request, 'subscribe/thankyou.html', context)
