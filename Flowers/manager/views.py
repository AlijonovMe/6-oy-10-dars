from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.handlers.wsgi import WSGIRequest
from django.contrib import messages
from datetime import datetime
from .forms import *
from .models import *


def index(request):
    flowers = Flowers.objects.filter(published=True)

    context = {
        'flowers': flowers,
        'current_year': datetime.now().year
    }

    return render(request, 'index.html', context)


def types(request, type_id):
    types = get_object_or_404(Types, id=type_id)
    flowers = Flowers.objects.filter(type_id=type_id, published=True)

    context = {
        'types': [types],
        'flowers': flowers,
        'current_year': datetime.now().year
    }

    return render(request, 'index.html', context)


def flower(request, flower_id):
    flower = get_object_or_404(Flowers, id=flower_id, published=True)

    context = {
        'flower': flower,
        'current_year': datetime.now().year
    }

    return render(request, 'detail.html', context)


def addType(request: WSGIRequest):
    if request.method == 'POST':
        form = TypeForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            if Types.objects.filter(name=form.cleaned_data['name']).exists():
                messages.error(request, "Ma'lumot qo'shilmadi. Bunday ma'lumot allaqachon qo'shilgan.")
            else:
                Types.objects.create(**form.cleaned_data)
                messages.success(request, "Ma'lumot muvaffaqiyatli qo'shildi.")
            return redirect('home')
    context = {
        'forms': TypeForm(),
        'current_year': datetime.now().year
    }
    return render(request, 'addType.html', context)


def addFlower(request: WSGIRequest):
    if request.method == 'POST':
        form = FlowerForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            Flowers.objects.create(**form.cleaned_data)
            messages.success(request, "Ma'lumotlar muvaffaqiyatli qo'shildi.")
            return redirect('home')
    context = {
        'forms': FlowerForm(),
        'current_year': datetime.now().year
    }

    return render(request, 'addFlower.html', context)


def updateType(request: WSGIRequest, type_id):
    types = get_object_or_404(Types, pk=type_id)

    if request.method == 'POST':
        form = TypeForm(data=request.POST, files=request.FILES)
        if form.is_valid():

            if Types.objects.filter(name=form.cleaned_data.get('name')).exists():
                messages.success(request, "Ma'lumot o'zgartirilmadi. Bunday ma'lumot allaqachon qo'shilgan.")
                return redirect('home')

            types.name = form.cleaned_data.get('name')
            types.save()

            messages.success(request, "Ma'lumot muvaffaqiyatli o'zgartirildi.")
            return redirect('home')

    forms = TypeForm(initial={
        'name': types.name
    })

    context = {
        'forms': forms,
        'current_year': datetime.now().year
    }

    return render(request, 'addType.html', context)


def deleteType(request, type_id):
    type = get_object_or_404(Types, pk=type_id)
    type.delete()
    messages.success(request, "Ma'lumot muvaffaqiyatli o'chirildi.")
    return redirect('home')


def updateFlower(request: WSGIRequest, flower_id):
    flower = get_object_or_404(Flowers, pk=flower_id)

    if request.method == 'POST':
        form = FlowerForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            flower.name = form.cleaned_data.get('name')
            flower.description = form.cleaned_data.get('description')
            flower.price = form.cleaned_data.get('price')
            flower.count = form.cleaned_data.get('count')
            flower.published = form.cleaned_data.get('published')
            flower.type = form.cleaned_data.get('type')
            flower.save()

            messages.success(request, "Ma'lumot muvaffaqiyatli o'zgartirildi.")
            if flower.published:
                return redirect('flower_detail', flower_id=flower_id)
            else:
                return redirect('home')

    forms = FlowerForm(initial={
        'name': flower.name,
        'description': flower.description,
        'price': flower.price,
        'count': flower.count,
        'published': flower.published,
        'type': flower.type
    })

    context = {
        'forms': forms
    }

    return render(request, 'addFlower.html', context)


def deleteFlower(request, flower_id):
    flower = get_object_or_404(Flowers, pk=flower_id)
    flower.delete()

    messages.success(request, "Ma'lumot muvaffaqiyatli o'chirildi.")
    return redirect('home')
