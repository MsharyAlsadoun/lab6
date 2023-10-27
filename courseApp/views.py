from django.shortcuts import render , HttpResponse
from .models import Student , course

# Create your views here.

def students(request):
    if request.method == 'POST':
        first = request.POST.get('first')
        last = request.POST.get('last')
        gpa = request.POST.get('gpa')
        student = Student.objects.create(first = first, last = last, gpa = gpa)
    
    return render(request , 'students.html', {"students" : Student.objects.all()})
        
        
        

def courses(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        newcourse = course.objects.create(name = name)
        
    return render(request , 'courses.html',{"courses": course.objects.all()})
 
        
def details(request, Student_id): 
    student = Student.objects.get(id = Student_id)
    courses = student.courses.all()
    notRe = course.objects.exclude(name = 'courses')
    if request.method == 'POST':
        s = Student.objects.get(id = Student_id)
        cId = request.POST.get('course')
        c = course.objects.get(id = cId)
        #name = request.POST.get('c.name')
        s.courses.add(c.id)
        s.save
        return render(request , 'details.html' , {"student" : student,"notIn": notRe , "courses": courses})   
        
    
    return render(request , 'details.html' , {"student" : student,"notIn": notRe , "courses": courses})   