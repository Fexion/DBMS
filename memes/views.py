from django.http import HttpResponse
from django.shortcuts import render
from .models import User, Mem
from django.db import connection

def index(request):
    cursor = connection.cursor()
    all_memes = cursor.execute("select id, Name from memes_mem")
    context = {
        "all_memes" : all_memes,
    }
    return render(request, "memes/index.html", context)

def mem_information(request, mem_id):
    cursor = connection.cursor()
    context = {}
    picture = cursor.execute('select Picture from memes_mem where id='+str(mem_id))
    context["picture"] = picture.fetchone()[0]
    all_memes = cursor.execute('select Name, Birth_Date from memes_mem where id='+str(mem_id))
    context["mem"] = all_memes.fetchall()[0]
    creator = cursor.execute('select Nickname from memes_creator where id=(select Creator_id_id from memes_mem where id ='+str(mem_id)+');')
    context["creator"] = creator.fetchall()[0][0]
    return render(request, "memes/mem_inf.html", context)
