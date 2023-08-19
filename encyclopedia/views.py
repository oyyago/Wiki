from markdown2 import Markdown
from django.shortcuts import render
from . import util
markdowner = Markdown()
    

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request,title):
    converter = convert_to_mardown(title)
    l = "tetsteet"
    if converter == None:   
        return render(request,'encyclopedia/erro.html',{
            "erro":"Essa página não exite filho"
        })
    else:
        return render(request,'encyclopedia/entry.html',{
            "title":title,
            "content": converter
        })
    


def search(request):
    if request.method == 'POST':   
        entry_search = request.POST['q']
        convert_content = convert_to_mardown(entry_search)
        if convert_content is not None :
            return render(request, 'encyclopedia/entry.html', {
                'title':entry_search,
                'content':convert_content
            })
        else:
            entries = util.list_entries()
            reco = []
            for entry in entries:
                if entry_search.lower() in entry.lower():
                    reco.append(entry)
            return render(request, "encyclopedia/search.html", {
                'recomendation': reco
            })



def new_page(request):
    if request.method == 'GET': 
        return render(request, 'encyclopedia/new.html')
    else:
        title = request.POST["title"]
        content = request.POST["content"]
        check_exist = util.get_entry(title)
    if check_exist is not None:
        return render(request, 'encyclopedia/erro.html',{
            'erro':"this page already exist"
        })
    else: 
        util.save_entry(title,content)
        converted = convert_to_mardown(title)
        return render(request, 'encyclopedia/entry.html',{
            "title":title,
            "content":converted
        })

def edit(request):
    if request.method == 'POST':
        title = request.POST["valor_entrada"]
        content = util.get_entry(title)
        
        return render(request,'encyclopedia/edit.html',{
            "title":title,
            "content":content
        })


def edit_save(request):
    if request.method == 'POST':
        title = request.POST["title"]
        content = request.POST["content"]
        util.save_entry(title,content)
        converted = convert_to_mardown(title)
        return render(request, 'encyclopedia/entry.html',{
            "title":title,
            "content":converted
        })




def random(request):
    import random
    entries = util.list_entries()
    randEndtri = random.choice(entries)
    converted = convert_to_mardown(randEndtri)
    return render(request, 'encyclopedia/entry.html',{
            "title":randEndtri,
            "content":converted
    })



def convert_to_mardown(title):
    content = util.get_entry(title)
    if content == None:
        return None
    else:
        return markdowner.convert(content)