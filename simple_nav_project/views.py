from django.shortcuts import render

def home(request):
    d = {'author' : 'Rahim', 'age' : 22, 'lst' : [1,2,3], 'courses' : [

        {
            'id' : 231,
        'coursename' : 'Logic gate',
        'fee' : 5000
        },
          {
            'id' : 373,
        'coursename' : 'Algorithm',
         'fee' : 3000
        },
    ]}
    return render(request, "home.html", d)