from time import sleep

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import CreateNewList
from .models import TodoList, Item


def index(response, id):
    todo = response.user.todo_list.filter(id=id)[0]

    if not todo:
        return HttpResponseRedirect("/")

    if response.method == "POST":
        if response.POST.get("save"):
            for note in todo.item_set.all():
                if response.POST.get(f"c{note.id}") == "completed":
                    note.closing_date = response.time
                    note.completed = True
                else:
                    note.completed = False
                note.save()

        elif response.POST.get("newNote"):
            txt = response.POST.get("new")
            if len(txt) > 2:
                todo.item_set.create(text=txt, completed=False, opening_date=response.time)
            else:
                print("invalid")
    return render(response, "main/list.html", {"todo": todo})


def home(response):
    print(response.time)
    user = response.user
    if user.is_authenticated:
        return render(response, "main/home.html", {"todos": user.todo_list.all()})

    return render(response, "main/home.html", {"todos": []})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            new_todo = TodoList(name=form.cleaned_data["name"])
            new_todo.save()
            response.user.todo_list.add(new_todo)
        return HttpResponseRedirect(f"/{new_todo.id}")

    else:
        form = CreateNewList()
        return render(response, "main/create.html", {"form": form})


