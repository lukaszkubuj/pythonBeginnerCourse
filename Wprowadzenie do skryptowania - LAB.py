{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h1>Wprowadzenie do skryptowania - LAB</h1>\n",
    "<h2>Ćwiczenia Pythona na przykładzie obliczeń figur geometrycznych</h2>\n",
    "<ul>\n",
    "    <li>wprowadzam wartości zmienne (WartośćPi i PromienOkregu)</li>\n",
    "    <li>obliczamy kolejno:</li>\n",
    "    <ul>\n",
    "        <li>PoleKola (Pi*rkwadrat)</li>\n",
    "        <li>Obwód okręgu (2pi*r)</li>\n",
    "        <li>Pole prostokąta</li>\n",
    "        <li>Pole trapezu</li>\n",
    "        <li>dodatkowo można obwód walca lub graniastosłupa o określonej wysokości i podstawie będącej kołem, prostokątem, trapezem</li></ul>\n",
    "    </ul>\n",
    "        \n",
    "      "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "#w tym zadaniu liczymy pole koła (WartośćPi*(PromienOkregu**2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "WartośćPi = 3.14"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "PromienOkregu = 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "PoleKola = WartośćPi*(PromienOkregu**2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "78.5\n"
     ]
    }
   ],
   "source": [
    "print(PoleKola)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "#liczymy obwód okręgu (2Pi*r)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "ObwodOkregu = 2*WartośćPi*PromienOkregu"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "31.400000000000002\n"
     ]
    }
   ],
   "source": [
    "print(ObwodOkregu)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "#liczymy pole prostokąta (bokA*bokB)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "bokA=7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "bokB=2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "PoleProstokata = bokA*bokB"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "14\n"
     ]
    }
   ],
   "source": [
    "print(PoleProstokata)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "#liczymy pole trapezu (a+b)*h/2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "#bokA i bokB jak w prostokącie"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "hTrapezu = 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "PoleTrapezu= (bokA+bokB)*hTrapezu/2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "13.5\n"
     ]
    }
   ],
   "source": [
    "print(PoleTrapezu)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "#liczymy pole powierchni walca: podstawa to koło z początku skryptu, h walca = 12"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "#pole powierzchni walca = 2*pole podstawy (koła) + pole powierzchni bocznej (prostokąt o boku1 = obwód podstawy, bok2 = h walca)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "hWalca = 12"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "PolePowierzchniWalca=2*PoleKola+ObwodOkregu*hWalca"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "533.8\n"
     ]
    }
   ],
   "source": [
    "print(PolePowierzchniWalca)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "#starczy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "press enter to exit\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "''"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "input('press enter to exit')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
