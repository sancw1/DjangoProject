#Variables

import datetime

from django.conf import settings
from django.http import HttpResponse


isAdmin = False

#Functions

def GetImgDir(file: str) -> str:
    return "main/imgs/" + file

def GetFilmDetailByName(name: str):
    for film in filmDetail:
        print(film['name'])
        if film['name'] == name: return film
    return None

def GetFilmDetailByGenre(genre: str):
    flist = list()

    for film in filmDetail:
        if film['category'] == genre:
            flist.append(film)

    return None if len(flist) <= 0 else flist

def GetFilmWichContains(_str: str):
    flist = list()

    for film in filmsList:
        if film['title'].__contains__(_str):
            flist.append(film)
    
    if len(flist) > 0: return flist
    else: return None

def GetFilmListBySearch(name: str):
    flist = GetFilmWichContains(name)

    if flist != None: return flist
    else: return GetFilmWichContains(name[0])

def GetFilmListByGenre(genre: str):
    flist = list()

    for film in filmsList:
        if film['category'] == genre:
            flist.append(film)

    return None if len(flist) <= 0 else flist

def SetCategory(category: str):
    for cat in categoryes:
        if cat['name'] == category:
            cat['isCurrent'] = True
        else: cat['isCurrent'] = False

def GetCurrentCategory():
    for cat in categoryes:
        if cat['genre'] == 'All' and cat['isCurrent']: return None
        if cat['isCurrent']: return cat['genre']

def DeleteFilmByName(name: str):
    global filmsList, filmDetail

    _filmList = list()
    _filmdetail = list()

    for film in filmsList:
        _filmList.append(film)

    for film in filmDetail:
        _filmdetail.append(film)

    filmsList.clear()
    filmDetail.clear()

    for film in _filmList:
        if film['title'] != name: 
            filmsList.append(film)

    for film in _filmdetail:
        if film['name'] != name: 
            filmDetail.append(film)

    


# Data

filmsList = [
    {
        'title': 'Драйв',
        'img': GetImgDir('drive.jpeg'),
        'isStaticImage': True,
        'category': 'Боевик',
    },
    {
        'title': 'Бегущий по лезвию',
        'img': GetImgDir('bladeRunner.jpg'),
        'isStaticImage': True,
        'category': 'Боевик',
    },
    {
        'title': 'Наблюдающий',
        'img': GetImgDir('watcher.jpg'),
        'isStaticImage': True,
        'category': 'Трилер',
    },
    {
        'title': 'Поездка на выходные',
        'img': GetImgDir('TheWeekendAway.jpg'),
        'isStaticImage': True,
        'category': 'Трилер',
    },
    {
        'title': 'Нечестивые',
        'img': GetImgDir('Wicked.jpg'),
        'isStaticImage': True,
        'category': 'Ужасы',
    },
    {
        'title': 'Шкатулка Дьявола',
        'img': GetImgDir('DevilBox.jpg'),
        'isStaticImage': True,
        'category': 'Ужасы',
    },
]

filmDetail = [
    {
        'name': 'Драйв',
        'img': GetImgDir('drive.jpeg'),
        'isStaticImage': True,
        'category': 'Боевик',
        'raiting': 4,
        'rangeYellow': range(4),
        'rangeBlack': range(1),
        'about': 'Фильм-сенсация Каннского кинофестиваля 2011 года, за который датчанин Николас Виндинг Рефн получил приз за режиссуру, а Райан Гослинг укрепился не только в статусе "секс-символа", но и очень серьезного драматического актера. Чтобы составить собственное мнение о фильме, предлагаем посмотреть "Драйв" онлайн. Райан Гослинг играет драйвера без имени, водителя без страха и упрека, который работает каскадером на съемках фильмов, а по ночам подрабатывает молчаливым перевозчиком, что приносит куда большую прибыль. У него жесткие условия, нарушение которых чревато провалом любой операции. Он лишь перевозит пассажиров из точки А в точку Б, ему нет дела до того, что происходит на заднем сидении. Встретив однажды обворожительную Айрин, парень оказывается вовлечен в опасную игру, замешанную на деньгах мафии. В результате цепочки кровавых разборок он теряет близкого человека, а его собственная жизнь и жизнь Айрин оказывается под угрозой. Постепенно становится ясно, что внешние холодность, молчаливость и равнодушие героя – лишь маска.'
    },
    {
        'name': "Бегущий по лезвию",
        'img': GetImgDir('bladeRunner.jpg'),
        'isStaticImage': True,
        'category': 'Боевик',
        'raiting': 3,
        'rangeYellow': range(3),
        'rangeBlack': range(2),
        'about': 'Начав просмотр фильма «Бегущий по лезвию 2049», зритель узнает о том, что Рик Декард долгое время пытался оставить свою работу ловца сбежавших андроидов. Надеясь уйти на заслуженный отпуск, он был вызван начальство, требующим отыскать репликантов, обладающих высоким уровнем интеллекта и самосознанием.'
    },
    {
        'name': 'Наблюдающий',
        'img': GetImgDir('watcher.jpg'),
        'isStaticImage': True,
        'category': 'Трилер',
        'raiting': 4,
        'rangeYellow': range(4),
        'rangeBlack': range(1),
        'about': 'Джулия со своим парнем переезжает в новую квартиру, где девушку начинает преследовать тревожное чувство, что за ней постоянно кто-то следит. Хотя окружающие не придают её беспокойствам значения, вскоре по соседству начинают происходить пугающие события.'
    },
    {
        'name': "Поездка на выходные",
        'img': GetImgDir('TheWeekendAway.jpg'),
        'isStaticImage': True,
        'category': 'Трилер',
        'raiting': 3,
        'rangeYellow': range(3),
        'rangeBlack': range(2),
        'about': 'Лучшая подруга Бет исчезает в Хорватии, где женщины устраивают девичник, и героиня спешит выяснить правду. С каждой новой зацепкой ей открывается все более жуткий обман.'
    },
    {
        'name': 'Нечестивые',
        'img': GetImgDir('Wicked.jpg'),
        'isStaticImage': True,
        'category': 'Ужасы',
        'raiting': 5,
        'rangeYellow': range(5),
        'rangeBlack': range(0),
        'about': 'В мире с огромной скоростью стали распространяться слухи о девушке Элис, которая обрела удивительные способности, впустив в свою душу Деву Марию. Божество вернуло ей возможность слышать и наделило даром исцеления. Эти чудеса привлекли католиков с разных уголков планеты и даже заинтересовали представителей Ватикана.'
    },
    {
        'name': "Шкатулка Дьявола",
        'img': GetImgDir('DevilBox.jpg'),
        'isStaticImage': True,
        'category': 'Ужасы',
        'raiting': 2,
        'rangeYellow': range(2),
        'rangeBlack': range(3),
        'about': 'Американский историк приезжает в британскую глубинку, чтобы поработать куратором музея, где случайно находит и открывает древнюю шкатулку. '
    },
]

categoryes = [
    {
        'name': "Все",
        'genre': "All",
        'isCurrent': True
    },
    {
        'name': "Боевики",
        'genre': "Боевик",
        'isCurrent': False
    },
    {
        'name': "Трилеры",
        'genre': "Трилер",
        'isCurrent': False
    },
    {
        'name': "Ужасы",
        'genre': "Ужасы",
        'isCurrent': False
    }
]
