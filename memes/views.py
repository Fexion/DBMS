from django.http import HttpResponse
from django.shortcuts import render
from .models import User, Mem
from django.db import connection

def index(request):
    cursor = connection.cursor()
    all_memes = cursor.execute("select id, Name, picture from memes_mem")
    context = {
        "all_memes" : all_memes,
    }
    return render(request, "memes/index.html", context)

def creators(request):
    cursor = connection.cursor()
    creators = cursor.execute("select id, Nickname from memes_creator")
    context = {
        "creators" : creators,
    }
    return render(request, "memes/creators.html", context)



def mem_information(request, mem_id):
    cursor = connection.cursor()
    context = {}
    picture = cursor.execute('select Picture from memes_mem where id='+str(mem_id))
    context["picture"] = picture.fetchone()[0]
    context["name"] = cursor.execute('select Name from memes_mem where id='+str(mem_id)).fetchone()[0]
    context["BirthDate"] = cursor.execute('select Birth_Date from memes_mem where id='+str(mem_id)).fetchone()[0]
    creator = cursor.execute('select Nickname from memes_creator where id=(select Creator_id_id from memes_mem where id ='+str(mem_id)+');')
    context["creator"] = creator.fetchone()[0]
    context["likes"] = cursor.execute('select count(user_id) from memes_mem_User_likes_Mem where mem_id='+str(mem_id)).fetchone()[0]
    context["tags"] = cursor.execute('select name  from memes_tag where id in (select tag_id from memes_tag_tag_mem where mem_id ='+str(mem_id)+');').fetchall()#cant print multiple
    print(context["tags"])
    return render(request, "memes/mem_inf.html", context)

def creator_inf(request, Creator_id):
    cursor = connection.cursor()
    context = {}
    picture = cursor.execute('select Nickname from memes_creator where id='+str(Creator_id))
    context["Nickname"] = picture.fetchone()[0]
    all_memes = cursor.execute('select picture, name from memes_mem where Creator_id_id='+str(Creator_id))
    print(all_memes)
    context["pictures"] = all_memes.fetchall()

    return render(request, "memes/creator_inf.html", context)

def search(request):
    creator = request.GET.get("creator")
    tag1    = request.GET.get("tag1")
    tag2    = request.GET.get("tag2")
    tag3    = request.GET.get("tag3")
    tag4    = request.GET.get("tag4")
    tag5    = request.GET.get("tag5")
    name    = request.GET.get("name")
    source  = request.GET.get("source")
    sphere1 = request.GET.get("sphere1")
    sphere2 = request.GET.get("sphere2")
    sphere3 = request.GET.get("sphere3")

    cursor = connection.cursor()
    context = {}

    tag_list = '\''+str(tag1)+'\', \''+ str(tag2)+'\', \''+ str(tag3)+'\', \''+ str(tag4)+'\', \''+ str(tag5)+'\''
    tags = cursor.execute('select id, picture from memes_mem where id in \
    (select mem_id from memes_tag_tag_mem where tag_id in (select id from memes_tag where name in ('+tag_list+'))) and id in \
    (select mem_id from memes_mem_source where source_id in (select id from memes_source where name like \'%'+str(source)+'%\'));')
    context["tags"] = tags.fetchall()

    print(tags.fetchall())
    # search_mem = request.GET.get("q")
    # search_creator = request.GET.get("w")
    # search_tag = request.GET.get("e")
    #
    # search_source = request.GET.get("r")
    # search_sphere = request.GET.get("t")
    #
    # cursor = connection.cursor()
    # context = {}
    # if search_mem:
    #     picture = cursor.execute('select id, picture from memes_mem where name like \'%'+str(search_mem)+'%\'')
    #     context["all_memes"] = picture
    # if search_creator:
    #     creators = cursor.execute('select id, Nickname from memes_creator where nickname like \'%'+str(search_creator)+'%\'')
    #     context["creators"] = creators
    #
    # if search_tag:
    #     tags = cursor.execute('select id, picture from memes_mem where id in \
    #     (select mem_id from memes_tag_tag_mem where tag_id in (select id from memes_tag where name like \'%'+str(search_tag)+'%\'));')
    #     context["tags"] = tags
    # if search_source:
    #     source = cursor.execute('select id, picture from memes_mem where id in \
    #     (select mem_id from memes_mem_source where source_id in (select id from memes_source where name like \'%'+str(search_source)+'%\'));')
    #     print(source)
    #     context["sources"] = source



    return render(request, "memes/search.html", context)
