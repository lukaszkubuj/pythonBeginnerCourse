print('FR')
print('FR','USA','PL','ESP')
France = 'FR'
print(France,'USA','PL','ESP')

pi=3.14
r=10
print('pi=',pi,'; r=',r,'pr*r**=',pi*r**2)
print('area with radius',r,'=',pi*r**2)

print(1,2,3)
#w takim przypadku możemy użyc dodatkowego parametru separatora, np. srednika.
print(1,2,3, sep=' ;')
#można i tak
print(1,2,3, sep=' @@@ ')

#backslash n to rozpoczęcie z nowego wersu
print(France,'USA','PL','ESP', sep='\n')


#z kolei za TAB odpowiada \t
print(France,'USA','PL','ESP', sep='\t')

#\a to bell, czyli dzwonek, przypomnienie dźwiękowe !!cudzysłów zamiast apostrofa!!
print("this is bell: \a")
#w idle akurat nie działa, ale działa w okienku pythona.

#polecenie print rozumie również kody ASCII
#  "\u" - (unicode)
print("\u03A3")

#sam backslash jako znak, a nie element funkcji wyświetlamy używając podwójnego znaku "\\"
print("\\")
print('this is backslash: \\')


