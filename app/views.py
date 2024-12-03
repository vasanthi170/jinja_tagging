from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'Vasanthi Reddy','fn':'Sudhakar Reddy','mn':'Sireesha Reddy'}
    return render(request,'jinja_print.html',context=d)