from django.shortcuts import render
 
def home(rquest):
    
    return render(rquest, 'home.html')