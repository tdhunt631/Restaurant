from geopy import geocoders
from django.db import models

class Restaurant(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	zipcode = models.CharField(max_length=10)
	latitude = models.CharField('Latitude', max_length=20, null=True, blank=True)
	longitude = models.CharField('Latitude', max_length=20, null=True, blank=True)
	
	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		g = geocoders.GoogleV3()
		place, (lat, lng) = g.geocode("%s %s %s %s" % (self.address, self.city, self.state, self.zipcode))
		self.latitude = lat
		self.longitude = lng		
		super(Restaurant, self).save(*args, **kwargs)

	def getRating(self, *args, **kwargs):
		rating = 0
		reviews = Review.objects.filter(restaurant=self)
		for review in reviews:
			rating += review.rating
		if rating != 0:
			avg = rating/reviews.count()
			return avg
		else:
			return 'No reviews yet!'

class Review(models.Model):
	restaurant = models.ForeignKey('Restaurant')
	name = models.CharField(max_length=100)
	rating = models.IntegerField()
	comment = models.TextField()	

	def __unicode__(self):
		return "%s-%s" % (self.restaurant, self.name)
	

