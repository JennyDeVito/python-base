#!/usr/bin/env python3

"""E-mail machine.

Sends multiples e-mails. For now, just prints the e-mail message on the screen.

DO NOT SPAM!"""

__version__ = "0.1.0" 

import sys
import os

#colects the name of the e-mail and template file from the CLI arguments
arguments = sys.argv[1:]
if not arguments:
    print("Por favor, informe o nome do arquivo de e-mails e template!")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

#reads the e-mail addresses from a file
path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)

clientes =[]
for line in open(filepath):
    name, email = line.split(",")

    #TODO: substituir por envio de email
    print(f"Enviando email para: {email}")
    print(
        open(templatepath).read()
	    % {
	        "nome": name, 
	        "produto": "caneta", 
	        "texto": "Escrever muito bem", 
	        "link": "https://canetaslegais.com", 
	        "quantidade": 1, 
	        "preco": 50.5,
	       } 
	)
    print("-" * 50)
