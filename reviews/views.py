from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from reviews.models import Restaurant, Review

class Index(ListView):
	model = Restaurant
	template_name = 'reviews/index.html'
	context_object_name = 'restaurants'

class Details(DetailView):
	model = Restaurant
	template_name = 'reviews/details.html'
	context_object_name = 'restaurants'
	
	def get_context_data(self, **kwargs):
		context = super(Details, self).get_context_data(**kwargs)
		context['reviews'] = Review.objects.filter(restaurant=self.kwargs['pk'])
		return context
