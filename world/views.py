from django.contrib import messages
from django.shortcuts import redirect, render, reverse, get_object_or_404
from .models import *
from .forms import *

# Create your views here.

def world_index(request):
    wrestlers = Wrestler.objects.order_by("name")
    moves = Move.objects.order_by("name")
    matches = Match.objects.order_by("name")
    return render(request, "world_index.html", {"wrestlers": wrestlers, "moves": moves, "matches": matches})

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


def single_wrestler(request, pk):
    wrestler = get_object_or_404(Wrestler, pk=pk)
    return render(request, "single_wrestler.html", {"wrestler": wrestler})


def add_move(request):
    if request.method == "POST":
        move_form = MoveForm(request.POST)
        if move_form.is_valid():
            move = move_form.save(commit=False)
            move.save()
            messages.error(request, 'Added {0}'.format(move.name), extra_tags='alert')
            return redirect("world_index")
    else:
        move_form = MoveForm()
    return render(request, "add_move.html", {"move_form": move_form})


def edit_move(request, pk):
    this_move = Move.objects.get(pk=pk)
    if request.method == "POST":
        move_form = MoveForm(request.POST, instance=this_move)
        if move_form.is_valid():
            move = move_form.save(commit=False)
            move.save()
            messages.error(request, 'Edited {0}'.format(move.name), extra_tags='alert')
            return redirect("world_index")
    else:
        move_form = MoveForm(instance=this_move)
    return render(request, "edit_move.html", {"move_form": move_form})


def delete_move(request, pk):
    instance = Move.objects.get(pk=pk)
    messages.error(request, 'Deleted {0}'.format(instance.name), extra_tags='alert')
    instance.delete()
    return redirect(reverse('world_index'))


def single_move(request, pk):
    move = get_object_or_404(Move, pk=pk)
    return render(request, "single_move.html", {"move": move})


def promotions(request):
    promos = Promotion.objects.order_by("name")
    return render(request, "promotions.html", {"promos": promos})


def add_promotion(request):
    if request.method == "POST":
        promotion_form = PromotionForm(request.POST)
        if promotion_form.is_valid():
            promotion = promotion_form.save(commit=False)
            promotion.save()
            messages.error(request, 'Added {0}'.format(promotion.name), extra_tags='alert')
            return redirect("promotions")
    else:
        promotion_form = PromotionForm()
    return render(request, "add_promotion.html", {"promotion_form": promotion_form})


def edit_promotion(request, pk):
    this_promotion = Promotion.objects.get(pk=pk)
    if request.method == "POST":
        promotion_form = PromotionForm(request.POST, instance=this_promotion)
        if promotion_form.is_valid():
            promotion = promotion_form.save(commit=False)
            promotion.save()
            messages.error(request, 'Edited {0}'.format(promotion.name), extra_tags='alert')
            return redirect("promotions")
    else:
        promotion_form = PromotionForm(instance=this_promotion)
    return render(request, "edit_promotion.html", {"promotion_form": promotion_form, "this_promotion": this_promotion})


def delete_promotion(request, pk):
    instance = Promotion.objects.get(pk=pk)
    messages.error(request, 'Deleted {0}'.format(instance.name), extra_tags='alert')
    instance.delete()
    return redirect(reverse('promotions'))


def single_promotion(request, pk):
    promo = get_object_or_404(Promotion, pk=pk)
    return render(request, "single_promotion.html", {"promo": promo})


def add_match(request):
    if request.method == "POST":
        match_form = MatchForm(request.POST)
        if match_form.is_valid():
            match = match_form.save(commit=False)            
            match.save()
            mid = str(match.pk)
            match.name = 'Match Number: {0}'.format(mid)
            messages.error(request, 'Started {0}'.format(match.name), extra_tags='alert')
            match.save()
            return redirect("world_index")
    else:
         match_form = MatchForm()
    return render(request, "add_match.html", {"match_form": match_form})


def delete_match(request, pk):
    instance = Match.objects.get(pk=pk)
    messages.error(request, 'Deleted {0}'.format(instance.name), extra_tags='alert')
    instance.delete()
    return redirect(reverse('world_index'))