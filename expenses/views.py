from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseModelForm

# Create your views here.
# 儲存送出表單資料時，Django會使用POST方法，將表單資料傳送至目前的網址，這時候在views.py中，就可以透過以下的程式碼，儲存表單資料至資料庫中
def index(request):

    expenses = Expense.objects.all()

    form = ExpenseModelForm()

    if request.method == "POST":
        form = ExpenseModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/expenses")

    context = {
        'expenses' : expenses,
        'form': form
    }

    return render(request, 'expenses/index.html', context)

def update(request, pk):
    expense = Expense.objects.get(id=pk)
    form = ExpenseModelForm(instance=expense)

    if request.method =='POST':
        form = ExpenseModelForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
        return redirect("/expenses")

    context = {
        'form' : form
    }
    return render(request, 'expenses/update.html', context)

def delete(request, pk):
    expense = Expense.objects.get(id=pk)

    if request.method =='POST':
        expense.delete()
        return redirect("/expenses")

    context = {
        'expense' : expense
    }
    return render(request, 'expenses/delete.html', context)
