from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.
def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n 

def maths_tasks(request):
    if request.method == 'POST':
        action = request.POST['action']
        n = int(request.POST['n'])
        k = int(request.POST['k'])
        try:
            answer=fac(n)//(fac(n-k)*fac(k))
        except (ZeroDivisionError, TypeError, NameError):
            answer = 'Введите верные данные!'
            return redirect('maths_tasks')
        else:
            if action=='P':
                answer=fac(n)
            elif action=='A':
                answer=fac(n)//fac(n-k)
            elif action=='C':
                answer=fac(n)//(fac(n-k)*fac(k))
            else:
                messages.error(request, 'Неверные данные')
                return redirect('maths_tasks') 
        if answer is not None:
            return render(request, 'maths_tasks/maths_tasks.html', {'maths_tasks': answer})
        else:
            messages.error(request, 'Неверные данные')
            return redirect('maths_tasks')
    else:
        return render(request, 'maths_tasks/maths_tasks.html')
