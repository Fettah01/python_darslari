#------------------ 1-"DARS"--LISTS-----------------------------------------------------------
#cars = ['bmw', 'mercides', 'chevrolet']
#cars.insert(4, 'hyundai')
#cars.append('tracker')
#del cars [1]
#print('men bugun ' + cars[1] + ' oldim ' + 'lekin ' + cars[0] + ' pulim yetmadi')

#------------------ 2-"DARS"--WORK WITH LISTS-----------------------------------------------------------

#SORTING
#countries = ['uzb', 'kzx', 'tjk', 'abj', 'nth']
#countries.sort()
#print(countries[1].title())

#Capital later and smal later
#countries = ['uzb', 'Kzx', 'tjk', 'abj', 'nth']
#world = countries[1].lower()
#print(countries)

#REVERSE SORT
#cars = ['bmw', 'mercides', 'chevrolet', 'audi']
#cars.sort(reverse=True)
#print(cars)

#SORTED
#cars = ['bmw', 'mercides', 'chevrolet', 'audi', 'hyundai']
#print(sorted(cars, reverse=True))

#ROYHATNI ORTIDAN BOSHLAB CHIQARISH
#cars = ['bmw', 'mercides', 'chevrolet', 'audi', 'hyundai']
#cars.reverse()
#print(cars)


#RAGNE
#sonlar = list(range(0,11))
#print(sonlar)

#RANGE VA QADAM
#toq_sonlar = list(range(1,100, 2))
#print(toq_sonlar)

#juft_sonlar = list(range(0,100,2 ))
#print(juft_sonlar)

#MAX() MIN() SUM()
#narhlar = [12000, 22500,23456, 9800,10200,11000,5897]
#arzon = min(narhlar)
#qimmat = max(narhlar)
#summasi = sum(narhlar)
#print('arzon narx: ' , arzon,  'qimmat narx: ', qimmat , 'obshiy qoshganda ' , summasi)

#ROYHATNI KESISH
#narhlar = [12000, 22500,23456, 9800,10200,11000,5897]
#print(narhlar[1:5])
#print(narhlar[1:])
#print(narhlar[:2])

#ROYHATDAN NUSXA OLSIH
#my_narhlar = narhlar[:]
#my_narhlar = tuple(my_narhlar) #ozgarmas royhat
#my_narhlar = list(my_narhlar) #list ozgaruvchi royhat
#print(my_narhlar)


#--------------------------------- 3-DARS -----------------------------------------------------

#TSIKL

#dostlar = ['elbe', 'jasur', 'said', 'anvar']
#for dost in dostlar:
#   print('salom', dost)

#sonlar = list(range(1,11))
#for son in sonlar:
#    print(f"{son} ning kvadrati {son**2} ga teng")


#sonlar = list(range(11))
#sonlar_kvadrati = []
#for son in sonlar:
#    sonlar_kvadrati.append(son**2)
#print(sonlar)
#print(sonlar_kvadrati)

#dostlar = []
#print("Eng yaqin dostlaringizni kriting")
#for n in range(5):
#    dostlar.append(input(f'{n+1} dostingizni kriting: '))
#print(dostlar)



#dostlar = []
#print('dostlarizni kriting: ')
#for h in range(5):
#    dostlar.append(input(f'{h+1} dostingizni kriting:'))
#for n in dostlar:
#    print('salom' , n)


#------------------------------------4-DARS-----------------------------------------------------------------------
#IF ELSE SHARTLARI VA TARMOQLASH

#mashinalar = []
#print('5 ta mashinani kriting: ')
#for h in range(1):
#    mashinalar.append(input(f'{h+1} mashinani kriting: '))
#for n in mashinalar:
#    if n == 'bmw':
#        print(n.upper())
#    else:
#        print(n, 'is best car in the world')

#ism = input('Ismingiz nima? ')
#if ism.lower() != 'ali':
#    print(f'uzur {ism.title()} biz alini kutyapmiz')
#else:
#    print('salom ali')

#login = input('yangi login tanlang:')
#if len(login)>=5:
#    print('welcome')
#else:
#    print('login should be minimum 5 laters')


#yil = int(input('tugilgan yilingizni tanlang: '))
#if 2023-yil>18:
#    print(f'sizni yoshingiz ', {2023-yil}, 'ekan')
#    print('hush kelibsiz')
#else:
#    print('kirish mumkin emas')


#---------------------5-DARS------------------------------------------------------------------------
#IF-ELSE-ELIF

#son = int(input('Istalgan sonni kriting: '))
#if son < 0:
#    print('manfiy son')
#else:
#    print('Musbat son')


#yosh = int(input('yoshingizni kriting: '))
#if yosh<=7:
#    print('sizga krish bepul!')
#elif yosh<=12:
#    print('sizga kirish 5 ming som')
#else:
#    print('sizga kirish 10 ming som')


#yosh = int(input('yoshingizni kriting: '))
#if yosh<=8:
#    narh=0
#elif yosh<=12:
#    narh=5000
#elif yosh<=15:
#    narh = 10000
#else:
#    narh = 15000
#print(f"sizga kirish {narh} so'm")


#kun = input('bugungi kunni kriting: ')
#if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#    print('bugun dam olish kuni')
#else:
#    print('bugun ish kuni')


#kun = input('Bugun qaysi kun: ')
#harorat = float(input('Havo qanday: '))
#if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=30:
#    print('chomilgani kettik!')
#elif kun.lower()=='yakshanba'or kun.lower()=='shanba' and harorat<30:
#    print('uyda dam olamiz')
#else:
#    print('Ishlash kerak!')


#narh = 15000
#choy = 1
#non = 1
#salat = 1
#assorti = 0
#ovqat = 1
#kola = 0
#limon = 0
#if choy:
#    print('mijoz choy oldi')
#    narh = narh + 5000
#if non:
#    print('mijoz non oldi')
#    narh = narh + 4000
#if salat:
#    print('mijoz salat oldi')
#    narh = narh + 20000
#if assorti:
#    print('mijoz assorti oldi')
#    narh = narh + 25000
#if ovqat:
#    print('mijoz ovqat oldi')
#    narh = narh + 10000
#if limon:
#    print('mijoz limon oldi')
#    narh = narh + 2000
#print(f'jami: {narh}')


#menu = ['manti' , 'osh', 'norin', 'somsa', 'kabob',  'dum' ]
#ovqat = input('nima ovqat yeysiz: ')
#if ovqat.lower() in menu:
#    print('buyurtmangiz qabul qilindi')
#else:
#    print('afsuski bizda unday ovqat yoq')


#menu = ['manti' , 'osh', 'norin', 'somsa', 'kabob',  'dum' ]
#buyurtmalat = ['dumba', 'norin', 'assorti', 'non']
#for taom in buyurtmalat:
#    if taom in menu:
#        print(f'menyuda {taom} bor')
#    else:
#      print(f'kechirasiz menyuda {taom} yoq')



#menu = ['manti' , 'osh', 'norin', 'somsa', 'kabob',  'dum' ]
#buyurtmalar = ['osh', 'meva', 'kabob']

#if buyurtmalar:
#    for taom in buyurtmalar:
#        if taom in menu:
#            print(f'menyuda {taom} bor')
#        else:
#            print(f'kechirasiz menyuda {taom} yoq')
#------------------------HOMEWORK----------------------------------------------------
#son = int(input('juft sonni kriting:'))
#if son % 2 == 0:
#    print('raxmat')
#else:
#    print('bu juft son emas')


#print('Amir Temur muzeyiga hush kelibsiz!')
#yosh = int(input('Yoshingizni kriting: '))
#
#if yosh<= 4 or yosh>= 60:
#    print('Sizga kirish bepul!')
#elif yosh<18:
#    print('sizga kirish 10000')
#else:
#    print('sizha krish 15000')


#first = float(input('brinchi sonni kriting: '))
#second = float(input('ikkinchi sonni kriting'))
#if first>second:
#    print(f'{first} greater than {second}')
#else:
#    print(f'{second} greater than {first}')

#mahsulotlar = ['olma', 'anor', 'bugdoy', 'uzum', 'ananas']
#savat = []

#for n in range(5):
#    savat.append(input(f'savatga {n+1} mahsulot qoshing: '))
#bor_mah = []
#yoq_mah = []
#for mahsulot in savat:
#    if mahsulot in mahsulotlar:
#        savat.append(mahsulotlar)
#    else:
#        yoq_mah.append(mahsulotlar)
#if yoq_mah:
#    print(f'dokonimizda unday mahsulot yoq!')
#    if mahsulotlar in bor_mah:
#        print(mahsulotlar)
#else:
#    print('siz soragan barcha mahsulot dokonda bor')

#login = []

#loginlar = input('login kriting: ')
#for n in login:
#    if loginlar in login:
#        login.append(n)
#    else:
#        print('boshqa login tanlang')
#if loginlar in login:
#    print('boshqa login tanlang')
#else:
#    print('hush kelibsiz')

#--------------------------------------6-dars----------------------------------------------------------

#son = int(input('son kriting: '))
#son = son**2
#print(f'son')


