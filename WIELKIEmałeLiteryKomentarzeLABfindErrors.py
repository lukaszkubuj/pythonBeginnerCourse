# znajdź błąd w skrypcie:
'''
#definitionOfVariables
daysOfWorkPerMonth = 20
monthsInYear = 12
vacation = 26
yearsOfWOrk = 40
#result
print((daysOfWorkPermonth * monthsInYear - Vacation)*yearsOfWOrk)
'''

#po uruchomieniu następujący komentarz:

'''
Traceback (most recent call last):
  File "C:/Scripts/WIELKIEmałeLiteryKomentarzeLABfindErrors.py", line 7, in <module>
    print((daysOfWorkPermonth * monthsInYear - Vacation)*yearsOfWOrk)
NameError: name 'daysOfWorkPermonth' is not defined
'''

#czyli jest błąd w nazwie 'daysOfWorkPermonth' bo month powinno być z dużej litery
#poprawiamy błąd i uruchamiamy:
'''
#definitionOfVariables
daysOfWorkPerMonth = 20
monthsInYear = 12
vacation = 26
yearsOfWOrk = 40
#result
print((daysOfWorkPerMonth * monthsInYear - Vacation)*yearsOfWOrk)
'''

# teraz jeszcze vacaion nie wykrywa, znów wielkośc liter

'''Traceback (most recent call last):
  File "C:/Scripts/WIELKIEmałeLiteryKomentarzeLABfindErrors.py", line 29, in <module>
    print((daysOfWorkPerMonth * monthsInYear - Vacation)*yearsOfWOrk)
NameError: name 'Vacation' is not defined
'''

#do trzech razy sztuka

#definitionOfVariables
daysOfWorkPerMonth = 20
monthsInYear = 12
vacation = 26
yearsOfWOrk = 40
#result
print('ile dni pracujemy w życiu uwzględniając nastepujące dane: daysOfWorkPerMonth = 20, monthsInYear = 12vacation = 26, yearsOfWOrk = 40')
print((daysOfWorkPerMonth * monthsInYear - vacation)*yearsOfWOrk)


#i gitara
#sprawdziłem czy nie ma też błędu w formule mnożenia, ale jest ok!

input('enter')
