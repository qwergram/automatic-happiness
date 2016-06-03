from django.contrib import admin
from articles import models
# Register your models here.

admin.site.register(models.PotentialIdeaModel)
admin.site.register(models.CodeArticleModel)
admin.site.register(models.RepostModel)
admin.site.register(models.StatModel)
admin.site.register(models.HistoricalStockModel)
