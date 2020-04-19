from django.shortcuts import render, get_object_or_404, redirect

from .models import Meeting, Room
from .forms import MeetingForm


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def rooms_list(request):
    return render(request, "meetings/rooms_list.html",
            {"rooms": Room.objects.all()})


def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})


# As a bonus, here are example implementations
# Of an edit and delete form
# See also urls.py and templates

def edit(request, id):
    # First, get the meeting to edit from the database
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        # After editing: get data from form
        # Note the second argument: the meeting we are editing
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            # redirect back to detail page after save
            return redirect("detail", id)
    else:
        # Pre-fill the form with data from existing meeting
        form = MeetingForm(instance=meeting)
    return render(request, "meetings/edit.html", {"form": form})


# Delete is different: the form is only shown to ask for confirmation
# When we get a POST, we know we can go ahead and delete
def delete(request, id):
    # First, get the meeting to edit from the database
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        meeting.delete()
        return redirect("welcome")
    else:
        return render(request, "meetings/confirm_delete.html", {"meeting": meeting})