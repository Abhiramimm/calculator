from django import forms

class RegistrationForm(forms.Form):

    username=forms.CharField()

    password=forms.CharField()

    email=forms.CharField()


class BmrForm(forms.Form):
    
    weight=forms.IntegerField()

    height=forms.IntegerField()

    age=forms.IntegerField()

    options=(
        ("male","male"),
        ("female","female")
            )
    
    
    gender=forms.ChoiceField(choices=options)

    choices=(
        (1,"Sedentary"),
        (2,"LightlyActive"),
        (3,"Moderatively Active"),
        (4,"Very Active"),
        (5,"Extra Active")
        )
    activity_level=forms.ChoiceField(choices=choices)


class EmiCalculatorForm(forms.Form):

    amount=forms.IntegerField()

    interest=forms.IntegerField()

    tenure=forms.IntegerField()


class TemperatureForm(forms.Form):

    temp_in_deg=forms.IntegerField(required=False)
    
    temp_in_fh=forms.IntegerField(required=False)



class CurrentBillForm(forms.Form):

    previous_reading=forms.IntegerField()

    current_reading=forms.IntegerField()

    options=(

        (1,"singlephase"),
        (2,"threephase")

        )

    phase=forms.ChoiceField(choices=options)

    


    

   
