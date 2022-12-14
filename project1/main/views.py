from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .forms import UserImage
from .data import *

# Create your views here.

def index(request):
    SetCategory("Все")
    return render(request, 'main\index.html', { 'films': filmsList, 'category': 'Все', 'categoryes': categoryes, 'isAdmin': isAdmin })

def filmPage(request):
    SetCategory("")
    if request.method == 'POST':
        return render (request, 'main/filmPage.html', { 'film': GetFilmDetailByName(request.POST['filmName']), 'categoryes': categoryes, 'isAdmin': isAdmin, 'form': UserImage })
    else: 
        return render (request, 'main/Error.html', { 'error': "При открытии фильма возникла ошибка!", 'isAdmin': isAdmin })

def Search(request):
    search = request.POST['Search']

    if request.method == 'POST' and GetCurrentCategory() == None:
        SetCategory("")

        filmDetail = GetFilmDetailByName(search)
        if filmDetail != None:
            return render(request, 'main/filmPage.html', { 'film': filmDetail, 'categoryes': categoryes, 'isAdmin': isAdmin, 'form': UserImage })
        
        filmDetail = GetFilmListBySearch(search)
        if(filmDetail != None):
            return render(request, 'main/index.html', {'films': filmDetail, 'category': "Фильмы по запросу '" + str(search) + "'", 'categoryes': categoryes, 'isAdmin': isAdmin})
        else: return render (request, 'main/Error.html', { 'error': "По запросу '" + search + "' ничего не найдено!", 'isAdmin': isAdmin })
    elif(request.method == 'POST'):
        for film in GetFilmDetailByGenre(GetCurrentCategory()):
            if film['name'] == search:
                return render(request, 'main/filmPage.html', { 'film': film, 'categoryes': categoryes, 'isAdmin': isAdmin , 'form': UserImage})

        flist = list()

        for film in GetFilmListByGenre(GetCurrentCategory()):
            if str(film['title']).__contains__(search[0]):
                flist.append(film)

        if len(flist) > 0:
            return render(request, 'main/index.html', {'films': flist, 'category': "Фильмы по запросу '" + str(search) + "'", 'categoryes': categoryes, 'isAdmin': isAdmin})
        else: return render (request, 'main/Error.html', { 'error': "По запросу '" + search + "' ничего не найдено!", 'isAdmin': isAdmin })
    else: return render (request, 'main/Error.html', { 'error': "При поиске фильма возникла ошибка!", 'isAdmin': isAdmin })

def Genre(request):
    if request.method == 'POST':
        if request.POST['genre'] == 'All':
            SetCategory(request.POST['category'])
            return render(request, 'main\index.html', { 'films': filmsList, 'category': request.POST['category'], 'categoryes': categoryes, 'isAdmin': isAdmin })

        flist = GetFilmListByGenre(request.POST['genre'])

        if flist != None:
            SetCategory(request.POST['category'])
            return render(request, 'main\index.html', { 'films': flist, 'category': request.POST['category'], 'categoryes': categoryes, 'isAdmin': isAdmin })
        else: return render (request, 'main/Error.html', { 'error': "Фильмов жанра '" + request.POST['genre'] + "' не найдено!", 'isAdmin': isAdmin })
    else: return render (request, 'main/Error.html', { 'error': "При поиске фильмов возникла ошибка!", 'isAdmin': isAdmin })

def Admin(request):
    global isAdmin
    isAdmin = True
    SetCategory("Все")
    print("!!!")
    return render(request, 'main\index.html', { 'films': filmsList, 'category': 'Все', 'categoryes': categoryes, 'isAdmin': isAdmin })

def AdminClose(request):
    global isAdmin
    isAdmin = False
    SetCategory("Все")
    return render(request, 'main\index.html', { 'films': filmsList, 'category': 'Все', 'categoryes': categoryes, 'isAdmin': isAdmin })

def ChangeFilmDetails(request):
    if request.method == 'POST':
        print(request.POST.keys())
        print(request.POST['OldFilmName'])
        form = UserImage(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            img_obj = form.instance
            print(img_obj.image.url)

            for film in filmsList:
                if request.POST['OldFilmName'] == film['title']:
                    film['title'] = request.POST['name']
                    film['img'] = img_obj.image.url
                    film['category'] = request.POST['genre']
                    film['isStaticImage'] = False
                    break

            for film in filmDetail:
                if request.POST['OldFilmName'] == film['name']:
                    film['name'] = request.POST['name']
                    film['img'] = img_obj.image.url
                    film['category'] = request.POST['genre']
                    film['isStaticImage'] = False

                    film['raiting'] = request.POST['raiting']
                    film['rangeYellow'] = range(int(request.POST['raiting']))
                    film['rangeBlack'] =  range(5 - int(request.POST['raiting']))
                    film['about'] = request.POST['about']
                    break

            SetCategory("Все")
            return render(request, 'main\index.html', { 'films': filmsList, 'category': 'Все', 'categoryes': categoryes, 'isAdmin': isAdmin })
        else: return render (request, 'main/Error.html', { 'error': "При отправке формы возникла ошибка!", 'isAdmin': isAdmin })
    else: return render (request, 'main/Error.html', { 'error': "При изменении фильма возникла ошибка!", 'isAdmin': isAdmin })

def AddFilmPage(request):
    if isAdmin:
        return render(request, 'main/AddFilmPage.html', { 'categoryes': categoryes, 'form': UserImage })
    else: return render (request, 'main/Error.html', { 'error': "Ошибка прав доступа!", 'isAdmin': isAdmin })

def AddFilm(request):
    if request.method == 'POST':
        form = UserImage(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance

            filmsList.append({
                'title': str(request.POST['name']),
                'img': str(img_obj.image.url),
                'isStaticImage': False,
                'category': str(request.POST['genre'])
            })


            filmDetail.append({
                'name': str(request.POST['name']),
                'img': str(img_obj.image.url),
                'isStaticImage': False,
                'category': str(request.POST['genre']),
                'raiting': 4,
                'rangeYellow': range(int(request.POST['raiting'])),
                'rangeBlack': range(5 - int(request.POST['raiting'])),
                'about': str(request.POST['about']),
            })


            for film in filmDetail:
                print(film['name'])

            SetCategory("Все")
            return render(request, 'main\index.html', { 'films': filmsList, 'category': 'Все', 'categoryes': categoryes, 'isAdmin': isAdmin })
        else: return render (request, 'main/Error.html', { 'error': "При отправке формы возникла ошибка!", 'isAdmin': isAdmin })
    else: return render (request, 'main/Error.html', { 'error': "При добавлении фильма возникла ошибка!", 'isAdmin': isAdmin })

def DeleteFilm(request):
    if request.method == 'POST':
        filmName = request.POST['OldFilmName']

        DeleteFilmByName(filmName)

        SetCategory("Все")
        return render(request, 'main\index.html', { 'films': filmsList, 'category': 'Все', 'categoryes': categoryes, 'isAdmin': isAdmin })
    else: return render (request, 'main/Error.html', { 'error': "При удалении фильма возникла ошибка!", 'isAdmin': isAdmin })
