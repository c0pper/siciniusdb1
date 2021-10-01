from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Person
from .forms import CreateNewPerson

# Create your views here.


def home(response):
    user = response.user
    print(user)
    people = Person.objects.all()
    return render(response, "main/home.html", {"people": people, "user": user})


def create(response):

    if response.method == "POST":
        form = CreateNewPerson(response.POST)
        if form.is_valid():
            person = Person(
                fname=response.POST.get("fname"),
                lname=response.POST.get("lname"),
                birth_date=response.POST.get("birth_date"),
                phone=response.POST.get("phone"),
                city=response.POST.get("city"),
                province=response.POST.get("province"),
                job=response.POST.get("job")
            )
            person.save()
            response.user.person.add(person)

            return HttpResponseRedirect("/")
    else:
        form = CreateNewPerson()
    return render(response, 'main/create.html', {"form": form})

def user_subs(response):
    user = response.user
    return render(response, "main/user_subs.html", {})
