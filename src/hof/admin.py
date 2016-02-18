from django.contrib import admin
from .models import Store, StoreImage, Review, ReviewImage

admin.site.register(Store)
admin.site.register(StoreImage)
admin.site.register(Review)
admin.site.register(ReviewImage)
