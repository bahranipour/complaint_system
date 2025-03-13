from django.shortcuts import render, redirect,get_object_or_404
from .forms import ComplaintForm
from .models import Complaint
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def submit_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            messages.success(request,'شکایت شما با موفقیت ثبت شد')
            return redirect('complaint_list')
    else:
        form = ComplaintForm()
    return render(request, 'complaints/submit_complaint.html', {'form': form})

@login_required
def complaint_list(request):
    complaints = Complaint.objects.all()
    return render(request, 'complaints/complaint_list.html', {'complaints': complaints})


@login_required
def complaint_detail(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    return render(request, 'complaints/complaint_detail.html', {'complaint': complaint})


@login_required
def edit_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    
    if request.method == 'POST':
        form = ComplaintForm(request.POST, instance=complaint)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            return redirect('complaint_detail', complaint_id=complaint.id)
    else:
        form = ComplaintForm(instance=complaint)
    
    return render(request, 'complaints/edit_complaint.html', {'form': form, 'complaint': complaint})



@login_required
def delete_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    
    if request.method == 'POST':
        complaint.delete()
        return redirect('complaint_list')
    
    return render(request, 'complaints/confirm_delete.html', {'complaint': complaint})