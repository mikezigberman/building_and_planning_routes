from django.db import models

from cities.models import City

class Train(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Train number')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Travel time')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                  # null=True, blank=True,
                                  related_name='from_city_set',
                                  verbose_name='From what city?')
    to_city = models.ForeignKey('cities.City', on_delete=models.CASCADE,
                                related_name='to_city_set',
                                verbose_name='Which city?')

    def __str__(self):
        return f'Train No.{self.name} from the city {self.from_city}'
    
        class Meta:
            verbose_name = 'Train'
            verbose_name_plural = 'Trains'
            ordering = ['travel_time']