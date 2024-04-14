from django.shortcuts import render

# Create your views here.
def s1(request):
    d={'name':'Ashish','age':23}
    return render(request,'file.html',context=d)
def s2(request):
    d1={'loc':'Banglore'}
    return  render(request,'file2.html',context=d1)
