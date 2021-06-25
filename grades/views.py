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
        
        if res < 40 :
            grade = 'F'
        elif res >= 40 and res <= 49:
            grade = 'E'
            improve = 49 - float(internal_marks)
        elif res >= 50 and res <= 59:
            grade = 'D'
            improve = 59 - float(internal_marks)

        elif res >= 60 and res <= 69:
            grade = 'C'
            improve = 69 - float(internal_marks)
        elif res >= 70 and res <= 79:
            grade = 'B'
            improve = 79 - float(internal_marks)
        elif res >= 80 and res <= 89:
            grade = 'A'
            improve = 89 - float(internal_marks)
        elif res > 90:
            grade = 'A+'
 
        return render(request, 'grades/result.html', {'result':res, 'grade':grade, 'improve':improve})
    else:
        res = "enter valid digits"
        return render(request, 'grades/result.html', {'result':res})
    
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
