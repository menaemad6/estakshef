from django.db import models
from django.utils.text import slugify


class Site(models.Model):
    name = models.CharField(max_length=40 , verbose_name=('English Name'))
    arabic_name = models.CharField(max_length=40 , verbose_name=('Arabic Name'))
    place = models.CharField(max_length=150 , verbose_name=("Site Place"))
    description = models.CharField(max_length=1000 , verbose_name=("Site Description"))
    rate = models.IntegerField(default='5')
    map_link = models.CharField(max_length=1000 , verbose_name=("Map Link URL") , blank=True)




    lower_price = models.CharField(max_length=30 , blank=True , verbose_name=("Lower Price"))
    higher_price = models.CharField(max_length=30 , blank=True , verbose_name=("Higher Price"))



    contact_url = models.CharField(max_length=1000 , verbose_name=("Contact Url") , blank=True)
    contact_name = models.CharField(max_length=1000 , verbose_name=("Contact Name") , blank=True)


    first_image = models.ImageField( upload_to='sites/' , verbose_name=("First Image (Main)") , blank=True ,  null=True)
    second_image = models.ImageField(upload_to='sites/' , verbose_name=("Second Image") , blank=True ,  null=True)
    third_image = models.ImageField(upload_to='sites/' , verbose_name=("Third Image"),blank=True ,  null=True )
    fourth_image = models.ImageField(upload_to='sites/' , verbose_name=("Fourth Image"), blank=True ,  null=True)
# %y/%m/%d

    duration = models.CharField(max_length=1000 , verbose_name=("Recomended Duration"))




    SAME = 'SAME'
    YES_BUT_NOT_SAME = 'NOT_SAME'
    NO = 'NO'
    HOURS_CHOICES = [
        (SAME, 'Same Hours All The Week'),
        (YES_BUT_NOT_SAME, 'There Is Open Hour But Not Same'),
        (NO, 'There Isnt Hours Availble'),
    ]
    # hours = models.CharField(max_length=20, choices=HOURS_CHOICES, default=SAME , verbose_name=("There Is Open Hours?"))

    # HOUR1 = '1'
    # HOUR2 = '2'
    # HOUR3 = '3'
    # HOUR4 = '4'
    # HOUR5 = '5'
    # HOUR6 = '6'
    # HOUR7 = '7'
    # HOUR8 = '8'
    # HOUR9 = '9'
    # HOUR10 = '10'
    # HOUR11 = '11'
    # HOUR12 = '12'

    # HOURS = [
    #     (HOUR1, '1'),
    #     (HOUR2, '2'),
    #     (HOUR3, '3'),
    #     (HOUR4, '4'),
    #     (HOUR5, '5'),
    #     (HOUR6, '6'),
    #     (HOUR7, '7'),
    #     (HOUR8, '8'),
    #     (HOUR9, '9'),
    #     (HOUR10, '10'),
    #     (HOUR11, '11'),
    #     (HOUR12, '12'),
    # ]
    open_hours = models.CharField(max_length=100 , blank=True )
    close_hours = models.CharField(max_length=100 , blank=True)

    # saturday_open = models.CharField(max_length=30 , blank=True , choices=HOURS )
    # saturday_close = models.CharField(max_length=30 , blank=True , choices=HOURS )
    # sunday_open = models.CharField(max_length=30 , blank=True , choices=HOURS )
    # sunday_close = models.CharField(max_length=30 , blank=True , choices=HOURS )
    # monday_open = models.CharField(max_length=30 , blank=True , choices=HOURS )
    # monday_close = models.CharField(max_length=30 , blank=True , choices=HOURS )
    # tuesday_open = models.CharField(max_length=30 , blank=True , choices=HOURS )
    # tuesday_close = models.CharField(max_length=30 , blank=True , choices=HOURS )
    # wednesday_open = models.CharField(max_length=30 , blank=True , choices=HOURS )
    # wednesday_close = models.CharField(max_length=30 , blank=True , choices=HOURS )
    # thursday_open = models.CharField(max_length=30 , blank=True , choices=HOURS )
    # thursday_close = models.CharField(max_length=30 , blank=True , choices=HOURS )
    # friday_open = models.CharField(max_length=30 , blank=True , choices=HOURS )
    # friday_close = models.CharField(max_length=30 , blank=True , choices=HOURS )



    slug = models.SlugField(blank=True , null=True , verbose_name=("Site Slug (URL)") , allow_unicode=True , unique=True)


    def save(self , *args , **kwargs):
        if not self.slug :
            self.slug = slugify(self.name)
            super(Site , self).save(*args , **kwargs)

    def __str__(self):
        return self.name


class Login(models.Model):
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.email




