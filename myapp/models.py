from django.db import models
# Create your models here.
STATE_CHOICE= (
    ('Sukkur','Nawabshah'),
    ('Kotri','Mirpur Khas'),
    ('Shikarpur','Dadu'),
    ('Tando Allahyar','Shahdadko'),
)
LANDING_CHOICE= (
('lahore','japan'),
('chaina','france'),
('chaina','islamabab'),
('Tando Allahyar','Shahdadko'),
 )
CAUSED_CHOICE= (
('1.Dont remember!!','1. Dont remember!!'),
('2.Technical problem','2. Dad weather conditions'),
('3.Dad weather conditions Flights','3. Influence by other Flights'),
('4.Technical airoplan','4. Technical problem'),
('5.Influence by other Flights','5. Other problem'),
 )
class plan(models.Model):
    departing_from = models.CharField(choices=STATE_CHOICE, max_length=100)
    final_destination = models.CharField(choices=LANDING_CHOICE, max_length=100)
    no = models.CharField(max_length=100)
    date = models.DateField()
    name_airline=models.CharField(max_length=100)
    flight_number=models.IntegerField()
    date2=models.DateField()
    delayed=models.CharField(max_length=50)
    hourse1=models.CharField(max_length=50)
    days=models.CharField(max_length=50)
    caused = models.CharField(choices=CAUSED_CHOICE, max_length=100)
