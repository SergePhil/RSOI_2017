from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseBadRequest


class GreetingsView(View):

    template_name = 'greeting.html'

    def get(self, request):
        gender = request.GET.get('gender', None)
        last_name = request.GET.get('last_name', None)

        context = {'last_name': last_name, 'male_greeting' : False}
        if gender == 'm':
            context['male_greeting'] = True
        elif gender == 'f':
            context['male_greeting'] = False
        else:
            return HttpResponseBadRequest('Gender is either m or f')

        if last_name == None or last_name == '':
            return HttpResponseBadRequest('Last name should be specified')

        return render(request, self.template_name, context)