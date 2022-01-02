# BMI-calculator
using this program you can check your body mass index


h= float(input('enter you height in cm :'))
w= float(input('enter your weight in kilogram :'))
bmi= (w/h**2)
print(bmi)

if bmi>25:
    print('over weight : you need to subtract carbs')
elif bmi<=24.9 and bmi>18.5:
    print('normal : you need to take 100gm of protien per day')
elif bmi<18.5:
    print('under weight : you need to add carbs in your diet')
else:
    print('invalid creds')  

'''
A BMI below 18.5 means that you are underweight.
A BMI of 18.6 to 24.9 is healthy.
A BMI of 25 to 29.9 means that you are overweight.
A BMI of 30 or greater indicates obesity.
'''
