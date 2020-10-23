Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> print("Mijn naam is Amber")
Mijn naam is Amber
>>> naam = "Amber"
>>> print(naam)
Amber
>>> print(naam.upper())
AMBER
>>> print(naam[0:2])
Am
>>> print(naam[::-1])
rebmA
>>> 
>>> leeftijd = 19
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Amber ben je al 19 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
20
>>> leeftijd-=1
>>> leeftijd
19
>>> if leeftijd < 18:
    hoelang_tot18jaar = 18 - leeftijd
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')

    
Het is alweer 1 jaar geleden dat je 18 werd ;-)
>>> 
>>> from random import randint
>>> randint(0,1000)
512
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
528
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 528
>>> 
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-10-23 15:11:04.533014
>>> datum.strftime('%A %d %B %Y')
'Friday 23 October 2020'
>>> 
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'vrijdag 23 oktober 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'Venerdì 23 Ottobre 2020'
>>> 