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
    context={}
    creators = cursor.execute("select id, Nickname from memes_creator")
    context["creators"] = creators
    return render(request, "memes/creators.html", context)



def mem_information(request, mem_id):
    cursor = connection.cursor()
    context = {}
    picture = cursor.execute('select Picture from memes_mem where id='+str(mem_id))
    context["picture"] = picture.fetchone()[0]
    context["name"] = cursor.execute('select Name from memes_mem where id='+str(mem_id)).fetchone()[0]
    context["BirthDate"] = cursor.execute('select Birth_Date from memes_mem where id='+str(mem_id)).fetchone()[0]
    creator = cursor.execute('select Nickname from memes_creator where id=(select creator_id from memes_mem where id ='+str(mem_id)+');')
    context["creator"] = creator.fetchone()[0]
    context["likes"] = cursor.execute('select count(user_id) from memes_mem_is_liked_by_user where mem_id='+str(mem_id)).fetchone()[0]
    context["tags"] = cursor.execute('select name  from memes_tag where id in (select tag_id from memes_tag_mem where mem_id ='+str(mem_id)+');').fetchall()#cant print multiple
    print(context["tags"])
    return render(request, "memes/mem_inf.html", context)

def creator_inf(request, Creator_id):
    cursor = connection.cursor()
    context = {}

    Nickname = cursor.execute('select Nickname from memes_creator where id='+str(Creator_id))
    context["Nickname"] = Nickname.fetchone()[0]
    all_memes = cursor.execute('select picture, name from memes_mem where Creator_id='+str(Creator_id))
    context["pictures"] = all_memes.fetchall()
    popularity = cursor.execute('select popularity from memes_creator where id='+str(Creator_id))
    context["Popularity"] = popularity.fetchall()[0][0]

    Birthdate = cursor.execute('select Birth_Date from memes_user where id in (select user_id from  memes_creator where id='+str(Creator_id)+')')

    context["BirthDate"] = Birthdate.fetchall()[0][0]

    sex = cursor.execute('select sex from memes_user where id = (select user_id from  memes_creator where id='+str(Creator_id)+')')
    if sex.fetchall()[0][0]:
        sex = "female"
    else:
        sex = "male"
    context["sex"] = sex

    sources = cursor.execute('select name from memes_source where id in (select source_id from memes_creator_source where creator_id ='+str(Creator_id)+')')
    context["sources"] = sources.fetchall()

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
    if (tag1 or tag2 or tag3 or tag4 or tag5):
        tag_list = '\''+str(tag1)+'\', \''+ str(tag2)+'\', \''+ str(tag3)+'\', \''+ str(tag4)+'\', \''+ str(tag5)+'\''
        tag_select = 'id in(select mem_id from memes_tag_mem where tag_id in (select id from memes_tag where name in ('+tag_list+'))) and '
    else:
        tag_select = ''

    if (sphere1 or sphere2 or sphere3):
        sphere_list = '\''+str(sphere1)+'\', \''+ str(sphere2)+'\', \''+ str(sphere3)+'\''
        sphere_select = 'id in(select mem_id from memes_sphere_mem where sphere_id in (select id from memes_sphere where theme in ('+sphere_list+'))) and '
    else:
        sphere_select = ''

    result = cursor.execute('select id, picture from memes_mem where '+\
                            tag_select+sphere_select+\
    'id in (select mem_id from memes_mem_source where source_id in (select id from memes_source where name like \'%'+str(source)+'%\'))\
    and name like \'%'+str(name)+'%\'\
    and Creator_id in (select id from memes_creator where nickname like \'%'+str(creator)+'%\')\
    ;')
    context["result"] = result.fetchall()


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

def search_creator(request):
    creator = request.GET.get("creator")
    hight = request.GET.get("hight")
    low = request.GET.get("low")
    cursor = connection.cursor()
    context = {}
    print("q",hight,"q", low, sep='')
    if (hight or low):
        if (hight and low ==''):
            low = 0
        if (low and hight==''):
            hight = 100
            print("sdkjhflkjsdfhtglkjhrtlkh")
        popularity = ' and popularity <='+str(hight)+' and popularity >='+str(low)
    else:
        popularity = ""

    result = cursor.execute('select id, Nickname from memes_creator where Nickname like \'%'+str(creator)+'%\'' + popularity)




    context["result"] = result.fetchall()

    return render(request, "memes/search_creator.html", context)
