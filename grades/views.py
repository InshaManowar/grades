from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'grades/calculator.html')
def cgpa_input(request):
    return render(request, 'grades/calculate_cgpa.html')

def total_marks(request):
    internal_marks = request.POST.get('internal_marks')
    cgpa = request.POST.get('cgpa')
    if (internal_marks) and (cgpa):
        a = float(1.5 * float(internal_marks))
        b = float(2.5 * float(cgpa))
        res = a + b
        improve = '1000'
        grade = 'error'
        if res < 40 :
            grade = 'F'
        elif res >= 40 and res < 49.5:
            grade = 'E'
            improve = 50 - float(internal_marks)
        elif res >= 49.5 and res < 59.5:
            grade = 'D'
            improve = 60 - float(internal_marks)
        elif res >= 59.5 and res < 69.5:
            grade = 'C'
            improve = 70 - float(internal_marks)
        elif res >= 69.5 and res < 79.5:
            grade = 'B'
            improve = 80 - float(internal_marks)
        elif res >= 79.5 and res < 89.5:
            grade = 'A'
            improve = 90 - float(internal_marks)
        elif res > 89.5 and res < 100:
            grade = 'A+'
            improve = 'no more'
 
        return render(request, 'grades/result.html', {'result':res, 'grade':grade, 'improve':improve})
    else:
        res = "enter valid digits"
     
        return render(request, 'grades/result.html', {'result':res,'grade':grade, 'improve':improve})
    
def cgpa_result(request):
    marks1=request.POST.get('marks1')
    credit1 = request.POST.get('one')
    marks2=request.POST.get('marks2')
    credit2= request.POST.get('two')
   # marks3=request.POST.get('marks3') * request.POST.get('three')
   # marks4=request.POST.get('marks4') * request.POST.get('four')
   # marks5=request.POST.get('marks5')  * request.POST.get('five')
   # marks6=request.POST.get('marks6')* request.POST.get('six')
   # lab1=request.POST.get('lab1') * request.POST.get('lone')
   # lab2=request.POST.get('lab2') * request.POST.get('ltwo')
   # lab3=request.POST.get('lab3') * request.POST.get('lthree')
   # lab4=request.POST.get('lab4') * request.POST.get('lfour')
    if (marks1) and (marks2):
    #and (marks3) and (marks4) and (marks5) and (marks6) and (lab1) and (lab2) and (lab3) and (lab4):
        cgpa=(marks1 * credit1) + (marks2 * credit2)
        return render(request, 'grades/cgpa_result.html', {'cgpa':cgpa})
