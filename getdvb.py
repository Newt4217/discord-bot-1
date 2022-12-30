import requests
import json


def get_stop(city, stop, mif, limits):
    a = ""
    try:
        response = requests.get(
        url='http://widgets.vvo-online.de/abfahrtsmonitor/Abfahrten.do',
        params={
            'ort': city,
            'hst': stop,
            'vz': mif,
            'lim': limits
        },
        ).json()
    except:
        a = "Die Haltestelle existiert nicht!"
        return a
    i = 0
    for i in range(len(response)):
        if response[i][2] == "":
            response[i][2] = "Jetzt"
        elif response[i][2] == "1":
            response[i][2] = "in 1 Minute"
        else:
            temp = response[i][2]
            response[i][2] = f"in {temp} Minuten"
        a = a + f"**{response[i][0]}** Richtung **{response[i][1]}** {response[i][2]}\n"
        i += 1
    if a == "":
        a = """In den nächsten Stunden fährt an dieser Haltestelle kein ÖPNV!"""
    if len(a) >= 2000:
        a = "Die Antwort wäre zu lang für Discord! Versuche, weniger Ergebnisse anzufragen!"
    return a
