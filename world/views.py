from django.contrib import messages
from django.shortcuts import redirect, render, reverse, get_object_or_404
from .models import *
from .forms import *

# Create your views here.

def world_index(request):
    wrestlers = Wrestler.objects.order_by("name")
    return render(request, "world_index.html", {"wrestlers": wrestlers})

def add_wrestler(request):
    if request.method == "POST":
        wrestler_form = WrestlerForm(request.POST)
        if wrestler_form.is_valid():
            wrestler = wrestler_form.save(commit=False)
            wrestler.save()
            messages.error(request, 'Added {0}'.format(wrestler.name), extra_tags='alert')
            return redirect("world_index")

    else:
        wrestler_form = WrestlerForm()
    return render(request, "add_wrestler.html", {"wrestler_form": wrestler_form})


def edit_wrestler(request, pk):
    this_wrestler = Wrestler.objects.get(pk=pk)
    if request.method == "POST":
        wrestler_form = WrestlerForm(request.POST, instance=this_wrestler)
        if wrestler_form.is_valid():
            wrestler = wrestler_form.save(commit=False)
            wrestler.save()
            messages.error(request, 'Edited {0}'.format(wrestler.name), extra_tags='alert')
            return redirect("world_index")
    else:
        wrestler_form = WrestlerForm(instance=this_wrestler)
    return render(request, "edit_wrestler.html", {"wrestler_form": wrestler_form})


def delete_wrestler(request, pk):
    instance = Wrestler.objects.get(pk=pk)
    messages.error(request, 'Deleted {0}'.format(instance.name), extra_tags='alert')
    instance.delete()
    return redirect(reverse('world_index'))