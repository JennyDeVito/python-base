"""PSEUDO CÓDIGO"""

import ir, pegar, pedir, tem, comer, ficar

#premissas
today = "Segunda"
hora = 15
natal = False
chovendo = True
frio = True
nevando = True
semana = ["Segunda", "Terca", "Quarta", "Quinta", "Sexta"]
feriado = ["Quarta"]
horario_padaria = {
    "semana": 19,
    "fds": 12
}

#algoritmo
if today in feriado and not natal:
    padaria_aberta = False
elif today not in semana and hora < horario_padaria["fds"]:
    padaria_aberta = True
elif today in semana and hora < horario_padaria["semana"]:
    padaria_aberta = True
else:
    padaria_aberta = False

if padaria_aberta:
    if chovendo and (frio or nevando):
        pegar("guarda-chuva")
        pegar("blusa")
        pegar("botas")
    elif chovendo and not frio:
        pegar("guarda-chuva")
        pegar("agua")
    elif chovendo:
        pegar("guarda-chuva")

    ir("padaria")

    if tem("pao integral") and tem("baguete"):
        pedir("pao integral", 6)
        pedir("baguete", 6)
    elif tem("pao integral") or tem("baguete"):
        if tem("pao integral"):
            pedir("pao integral", 12)
        else:
            pedir("baguete", 12)
    else:
        pedir("", 6)
else:
    ficar("casa")
    comer("biscoito")
