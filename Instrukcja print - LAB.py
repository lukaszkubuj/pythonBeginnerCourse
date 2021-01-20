#1. Wyświetl napisy: TVP1, TVP2, TVN, Polsat, BBC, HBO, MTV. Użyj jednego polecenia print

print('TVP1, TVP2, TVN, Polsat, BBC, HBO, MTV')

#2. Wyświetl w/w teksty używając jako separatora znaku ";"

print('TVP1', 'TVP2', 'TVN', 'Polsat', 'BBC', 'HBO', 'MTV', sep=' ;')

#3. Korzystając z jednego polecenia print wyświetl napis (bez podtekstów!):

print('I like computers','TVP1','TVP2','TVN','Polsat','BBC','HBO','MTV', sep=' but better is ')

#4. Zadeklaruj zmienne ProgramName o wartości 'BBC', Item o wartości 'News'' i Time o wartości '18:00'

ProgramName = 'BBC'
Item = 'News'
Time = '18:00'

#5. Uwaga: W tym zadaniu nie używaj konkatenacji napisów (łączenia napisów).
#Użyj tylko polecenia print!Wyświetl napis (zwróć uwagę na kropkę na końcu!):
#I like watching News at 18:00 on BBC .

print('I','like','watching',Item,'at',Time,'on',ProgramName,'.')

#6.  Zmień napis tak, aby kropka była zaraz za  BBC. Nadal nie korzystamy z
#konkatenacji ale z pojedyńczego polecenia print.

print('I',' like',' watching ',Item,' at ',Time,' on ',ProgramName,'.', sep='')

