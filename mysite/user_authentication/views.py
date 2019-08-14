from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, View

class TestView(TemplateView):
    def get_template_names(self):
        return 'test_template.html'