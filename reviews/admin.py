from django.contrib import admin
from reviews.models import Restaurant, Review

class RestaurantAdmin(admin.ModelAdmin):
	pass

class ReviewAdmin(admin.ModelAdmin):
	pass

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Review, ReviewAdmin)
