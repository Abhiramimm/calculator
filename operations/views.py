from django.shortcuts import render
from django.views.generic import View
from operations.forms import RegistrationForm,BmrForm,EmiCalculatorForm,TemperatureForm,CurrentBillForm


# Create your views here.

class AddtionView(View):
    
    def get(self,request,*args,**kwargs):

        return render(request,"add.html")
    
    def post(self,request,*args,**kwargs):

        print("****addition post method****")

        num1=request.POST.get("box1")

        num2=request.POST.get("box2")

        result=int(num1)+int(num2)

        print(result)

        return render(request,"add.html",{"data":result})

class SubstractionView(View):

    def get(self,request,*args,**kwargs):
        
        return render(request,"sub.html")
    
    def post(self,request,*args,**kwargs):
        
        print("***substraction post method***")
        
        num1=request.POST.get("box1")
        
        num2=request.POST.get("box2")
        
        result=int(num1)-int(num2)
        
        print(result)
        
        return render(request,"sub.html",{"data":result})

class MultiplicationView(View):

    def get(self,request,*args,**kwargs):
        
        return render(request,"multiply.html")
    
    def post(self,request,*args,**kwargs):
        
        print("***Multiplicatation post method")
        
        num1=request.POST.get("box1")
        
        num2=request.POST.get("box2")
        
        result=int(num1)*int(num2)
        
        print(result)
        
        return render(request,"multiply.html",{"data":result})


class FactorialView(View):
    
    def get(self,request,*args,**kwargs):
        
        return render(request,"factorial.html")
    
    def post(self,request,*args,**kwargs):
        
        num=int(request.POST.get("box"))
        
        result=1
        
        for i in range(1,(num+1)):
        
            result=result*i
        
        return render(request,"factorial.html",{"data":result})
    
class PrimeNumberView(View):

    def get(self,request,*args,**kwargs):
        
        return render(request,"prime.html")
    
    def post(self,request,*args,**kwargs):
        
        num=int(request.POST.get("box"))
        
        is_prime=True
        
        for i in range(2,num):
        
            if num%i==0:
        
                is_prime=False
        
                break
        
        return render(request,"prime.html",{"data":is_prime})

class BmiView(View):

    def get(self,request,*args,**kwargs):
        
        return render(request,"bmi.html")
    
    def post(self,request,*args,**kwargs):
        
        weight=int(request.POST.get("wbox"))
        
        height=int(request.POST.get("hbox"))
        
        height_in_m2=height/100
        
        bmi=weight/(height_in_m2)**2
        
        bmi=round(bmi,2)
        
        if bmi<19:
        
            result="underweight"
        
        elif bmi<25:
        
            result="normal weight"
        
        elif bmi<30:
        
            result="overweight"
        
        elif bmi>30:
        
            result="obese"

        return render(request,"bmi.html",{"data":result})

class ReverseDigitView(View):

    def get(self,request,*args,**kwargs):
        
        return render(request,"reverse.html")
    
    def post(self,request,*args,**kwargs):
        
        num=int(request.POST.get("box"))
        
        result=""
        
        while(num!=0):
        
            digit=num%10
        
            result=result+str(digit)
        
            num=num//10
        
        return render(request,"reverse.html",{"data":result})

# from operations.forms import RegistrationForm
class SignupView(View):

    def get(self,request,*args,**kargs):
            
            form=RegistrationForm()

            return render(request,"register.html",{"form":form})

class BmrView(View):

    def get(self,request,*args,**kwrags):

        form=BmrForm()

        return render(request,"bmr.html",{"form":form})
     
    def post(self,request,*args,**kwargs):

        height=int(request.POST.get("height"))

        weight=int(request.POST.get("weight"))

        age=int(request.POST.get("age"))

        gender=request.POST.get("gender")

        activity_level=int(request.POST.get("activity_level"))

        print(height,weight,age,gender,activity_level)

        bmr=0

        if gender=="male":

        # BMR = (10 × weight in kg) + (6.25 × height in cm) − (5 × age in years) + 5
            bmr=(10*weight)+(6.25*height)-(5*age)+5

        elif gender=="female":
        
            bmr=(10*weight)+(6.25*height)-(5*age)-161

        print(bmr)


        form=BmrForm()

        calorie=0

        if activity_level==1:

            calorie=bmr*1.2
        
        elif activity_level==2:

            calorie=bmr*1.375
        
        elif activity_level==3:

            calorie=bmr*1.55

        elif activity_level==4:


            calorie=bmr*1.725
         
        elif activity_level==5:

            calorie=bmr*1.9
        
        print(f"Number of calories you need in order to maintain your weight:{calorie}")

             

        return render(request,"bmr.html",{"form":form})


    
class EmiCalculatorView(View):

    def get(self,request,*args,**kwargs):

        form=EmiCalculatorForm() # create object

        return render(request,"emi.html",{"form":form})
    
    def post(self,request,*args,**kwargs):

        amount=int(request.POST.get("amount"))
        
        interest=int(request.POST.get("interest"))

        tenure=int(request.POST.get("tenure"))

        # print(amount,interest,tenure)
       
        r=interest/12
       
        i=r/100
       
        n=tenure*12
       
        monthly_emi=(amount*i)*((1+i)**n)/((1+i)**n-1)
       
        print(f"monthly emi:{monthly_emi}")
        # total_interest=(monthly_emi*n)-amount
        # print(f"total interest:{total_interest}")
        # total_payment=amount+total_interest
        # print(f"total_payment:{total_payment}")

        form=EmiCalculatorForm()

        return render(request,"emi.html",{"form":form})
    

class TempConversionView(View):

    def get(self,request,*args,**kwargs):

        form_instance=TemperatureForm()

        return render(request,"temp.html",{"form":form_instance})
    
    def post(self,requset,*args,**kwargs):

        form_instance=TemperatureForm(requset.POST)

        if form_instance.is_valid():
            
            print("no error")
            
            print(form_instance.cleaned_data)
        
        else:
            print("error")
        
        return render(requset,"temp.html",{"form":form_instance})


class BmrVersionTwoView(View):

    def get(self,request,*args,**kwargs):

        form_instance=BmrForm()

        return render(request,"bmrsecond.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=BmrForm(request.POST)
        
        if form_instance.is_valid():

            # print(form_instance.cleaned_data)

            validated_data=form_instance.cleaned_data

            height=validated_data.get("height")

            weight=validated_data.get("weight")

            age=validated_data.get("age")

            gender=validated_data.get("gender")

            activity_level=validated_data.get("activity_level")

            print(weight,height,age,gender,activity_level)

            bmr=0
            
            if gender=="male":
                
                bmr=(10*weight)+(6.25*height)-(5*age)+5
            
            elif gender=="female":

                bmr=(10*weight)+(6.25*height)-(5*age)-161
            
            print(bmr)

            activity_level_values={"1":1.2,"2":1.375,"3":1.55,"4":1.725,"5":1.9}


            calorie=bmr*activity_level_values.get(activity_level)

            # context={"data":calorie}

            print(calorie)


            return render(request,"bmrsecond.html",{"form":form_instance,"data":calorie})
        
        else:
            print("errors")

            return render(request,"bmrsecond.html",{"form":form_instance})
        


class CurrentBillView(View):

    def get(self,request,*args,**kwargs):

        form_instance=CurrentBillForm()

        return render(request,"currentbill.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=CurrentBillForm(request.POST)

        if form_instance.is_valid():

            # print(form_instance.cleaned_data)

            validated_data=form_instance.cleaned_data

            previous_reading=validated_data.get("previous_reading")

            current_reading=validated_data.get("current_reading")

            phase=validated_data.get("phase")

            print(previous_reading,current_reading,phase)

            unit=current_reading-previous_reading

            print(unit)

            amount=0

            phase_values={"1":80,"2":160}

            if unit<100 :
                amount=(unit*6.05)+phase_values.get(phase)
            elif unit<200:
                amount=(unit*6.80)+phase_values.get(phase)
            elif unit<300:
                amount=(unit*7.50)+phase_values.get(phase)
            elif unit<500:
                amount=(unit*8.15)+phase_values.get(phase)
            elif unit>500:
                amount=(unit*9.40)+phase_values.get(phase)
            
            print(amount)

            
            return render(request,"currentbill.html",{"form":form_instance,"data":amount})
        
        else:

            print("errors")

            return render(request,"currentbill.html",{"form":form_instance})




        


              
                    
                
    