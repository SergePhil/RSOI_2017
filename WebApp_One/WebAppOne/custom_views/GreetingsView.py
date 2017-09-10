from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.http import Http404


class GreetingsView(View):

    template_name = 'greeting.html'

    def get(self, request):
        gender = request.GET.get('gender', None)
        last_name = request.GET.get('last_name', None)
        if last_name == None:
            raise Http404

        context = {'last_name': last_name, 'male_greeting' : False}
        if gender == 'm':
            context['male_greeting'] = True
        elif gender == 'f':
            context['male_greeting'] = False
        else:
            raise Http404

        return render(request, self.template_name, context)