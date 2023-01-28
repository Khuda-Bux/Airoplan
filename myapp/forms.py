from django import forms
from .models import plan
class Myplan(forms.ModelForm):
    class Meta:
        model = plan
        fields=['departing_from','final_destination','no','date',
                  'name_airline','flight_number','date2','delayed',
                  'hourse1','days','caused']
        labels={'no':'Did you have any connecting flights?','date':'Date, What was your scheduled departure date?','delayed':'Now onto the flight disruption itself. what actually happened?','hourse1':'How many hours late did you arrive?','days':'How far in advance did the airine notify you of the cancellations?','caused':'What did the airline say caused your disruption?'}
        STATE_CHOICE= (
        ('', 'Landing Point'),   
        ('','Nawabshah'),
        ('','Mirpur Khas'),
        ('','Dadu'),
        ('','Shahdadko'),
        ('','Sukkur'),
        ('','Kotri'),
        ('','Shikarpur'),
        ('','Tando Allahyar'),
    )
        LANDING_CHOICE= (
        ('','japan'),
        ('chaina','france'),
        ('chaina','islamabab'),
        ('Tando Allahyar','Shahdadko'),
     )
        CAUSED_CHOICE= (
        ('','Open it here'),   
        ('Slect the reason','Sont remember'),
        ('Sechnical problem','Sad weather conditions'),
        ('Snfluence by other Slights','Sther problem'),
       )
        NO_CHOICE= (
        ('','Open it here'),   
        ('No, I did not','No, I did not'),
        ('Yes, I had to change flights','Yes, I had to change flights'),
        
       )
        DELAYED_CHOICE= (
        ('','Open it here'),   
        ('My flight was Delayed!!','1.  My flight was Delayed!!'),
        ('My flight was Canceled!!','2. My flight was Canceled!!'),
        ('My flight was Boardig!!', '3. My flight was Boardig!!'),
       )
        HOURS_CHOICE= (
        ('','Open it here'),   
        ('0-1 hours',' 0-1 hours'),
        ('1-2 hours',' 1-2 hours'),
        ('2-3 hours',' 2-3 hours'),
        ('3-4hours','  3-4hours'),
        ('4+hours','   4+hours'),
        ('Never arrived','6. Never arrived'),
       )
        DAYS_CHOICE= (
        ('','Open it here'),   
        ('Less than 14 days','Less than 14 days'),
        ('14 days or more','14 days or more'),
       )
        widgets = {'departing_from': forms.Select(choices=STATE_CHOICE,attrs={'class': 'form-control'}),
     'final_destination': forms.Select(choices=LANDING_CHOICE,attrs={'class': 'form-control','required':False}),
     'no': forms.Select(choices=NO_CHOICE,attrs={'class': 'form-control'}),
     'date':forms.DateInput(attrs={'class':'form-control'}),
     'name_airline':forms.TextInput(attrs={'class':'form-control','placeholder':'United Airlines, UA'}), 
     'flight_number':forms.NumberInput(attrs={'class':'form-control'}), 
     'date2':forms.DateInput(attrs={'class':'form-control'}),  
     'delayed': forms.Select(choices=DELAYED_CHOICE,attrs={'class': 'form-control'}),  
     'hourse1': forms.Select(choices=HOURS_CHOICE,attrs={'class': 'form-control'}),  
     'days': forms.Select(choices=DAYS_CHOICE,attrs={'class': 'form-control'}),                                                         
     'caused': forms.Select(choices=CAUSED_CHOICE,attrs={'class': 'form-control'}),
    }
    
    