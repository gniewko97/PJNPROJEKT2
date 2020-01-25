import re
import os
import webbrowser

Odpalanie = r'^(((W|w)(ł|l)(ą|a)cz)|((U|u)ruchom)|(W(L|Ł)(Ą|A)CZ)|URUCHOM|ODPAL|(O|o)dpal|WYSTARTUJ|(W|w)ystartuj) (.+)$'
Zamykanie = r'^(((W|w)y(ł|l)(ą|a)cz)|((Z|z)amknij)|(WY(L|Ł)(Ą|A)CZ)|(ZAMKNIJ)|(ZABIJ)|((Z|z)abij)) (.+)$'
Dokument = r'^(((O|o)tw(ó|o)rz)|((P|p)oka(ż|z))|(OTW(Ó|O)RZ)|(POKA(Z|Ż))|(WY(S|Ś)WIETL)|((W|w)y(s|ś)wietl)) (.+)$'
Strona = r'^(((Z|z)najd(ź|z))|(ZNAJD(Z|Ź))|(WYSZUKAJ)|((W|w)yszukaj)) (.+)$'
Wyjscie = r'^((Do widzenia)|(DO WIDZENIA)|((c|C)ze(ś|s)(ć|c)))$'


def otworz_plik(plik):
    try:
        os.startfile(plik)
    except Exception as er:
        print(str(er))


def otworz_url(url):
    try:
        webbrowser.open("https://www." + url, new=0)
    except Exception as er:
        print(str(er))


def otworz_app(plik):
    try:
        os.startfile(plik)
    except Exception as er:
        print(str(er))


def zamknij_app(nazwa):
    try:
        os.system("taskkill /f /IM " + nazwa + ".exe")
    except Exception as er:
        print(str(er))


def main():
    while True:
        command = input("Podaj polecenie: ")
        if re.match(Wyjscie, command):
            break
        nazwa = command.split()[1]
        if re.match(Dokument, command):
            otworz_plik(nazwa)
        if re.match(Strona, command):
            otworz_url(nazwa)
        if re.match(Odpalanie, command):
            otworz_app(nazwa)
        if re.match(Zamykanie, command):
            zamknij_app(nazwa)


main()
