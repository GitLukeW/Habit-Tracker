from django.shortcuts import render, get_object_or_404, redirect
from .models import Habit, DailyRecord
from .forms import HabitForm, DailyRecordForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def daily_habits(request):
    habit = Habit.objects.filter(user=request.user)
    return render(request, 'habit_tracker/daily_habits.html', {'habits': habit})


@login_required
def habit_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    return render(request, 'habit_tracker/habit_detail.html', {"habit": habit})


@login_required
def habit_new(request):
    if request.method == "POST":
        habit_form = HabitForm(request.POST)
        if habit_form.is_valid():
            habit = habit_form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect('habit_detail', pk=habit.pk)
    else:
        habit_form = HabitForm()
    return render(request, 'habit_tracker/habit_edit.html', {'habit_form': habit_form})


@login_required
def habit_edit(request, pk):
    post = get_object_or_404(Habit, pk=pk)
    if request.method == "POST":
        habit_form = HabitForm(request.POST, instance=post)
        if habit_form.is_valid():
            habit = habit_form.save()
            return redirect('habit_detail', pk=post.pk)
    else:
        habit_form = HabitForm(instance=post)
    return render(request, 'habit_tracker/habit_edit.html', {'habit_form': habit_form})


@login_required
def habit_remove(request, pk):
    post = get_object_or_404(Habit, pk=pk)
    post.delete()
    return redirect('daily_habits')


@login_required
def daily_record(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    daily_record = habit.dailyrecord.all()
    return render(request, 'habit_tracker/habit_detail.html', {'daily_record': daily_record})


@login_required
def edit_daily_record(request, pk):
    post = get_object_or_404(DailyRecord, pk=pk)
    if request.method == "POST":
        daily_record_form = DailyRecordForm(request.POST, instance=post)
        if daily_record_form.is_valid():
            daily_record = daily_record_form.save()
            return redirect('habit_detail', pk=post.pk)
    else:
        daily_record_form = DailyRecordForm(instance=post)
    return render(request, 'habit_tracker/habit_detail.html', {'daily_record_form': daily_record_form})
