################################################################
#                                                              #
#                        [ Creditos ]                          #
#                                                              #
################################################################
#                                                              #
#                  Codigo hecho por xNetting                   #         
#                                                              #
#              Dev: xNetting / Grupo: Panic Squad              #
#                                                              #
################################################################

# Dev: xNetting / xFullCode
# PanicSquad
# Version - 1.0.0

from dns.tsig import _digest
import nmap
import requests
import socket
import dns.resolver
from urllib import request
import re
import hashlib
import string
import json
from itertools import product
from colorama import *
import time
import ctypes
import os
import sys

os.system('cls || clear')
ctypes.windll.kernel32.SetConsoleTitleW('Devine Tool | xNetting | Panic Squad')
print(f'''

{Fore.LIGHTCYAN_EX}    ┌──────────────────────────────────────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                                                      │  
{Fore.LIGHTCYAN_EX}    │  {Fore.LIGHTRED_EX} ██████╗░{Fore.LIGHTGREEN_EX}███████╗{Fore.LIGHTRED_EX}██╗░░░██╗{Fore.LIGHTGREEN_EX}██╗{Fore.LIGHTCYAN_EX}███╗░░██╗{Fore.LIGHTRED_EX}███████╗  {Fore.LIGHTGREEN_EX}████████╗{Fore.LIGHTRED_EX}░█████╗░░█████╗░{Fore.LIGHTGREEN_EX}██╗░░░░░   {Fore.LIGHTCYAN_EX}│ 
{Fore.LIGHTCYAN_EX}    │  {Fore.LIGHTRED_EX} ██╔══██╗{Fore.LIGHTGREEN_EX}██╔════╝{Fore.LIGHTRED_EX}██║░░░██║{Fore.LIGHTGREEN_EX}██║{Fore.LIGHTCYAN_EX}████╗░██║{Fore.LIGHTRED_EX}██╔════╝  {Fore.LIGHTGREEN_EX}╚══██╔══╝{Fore.LIGHTRED_EX}██╔══██╗██╔══██╗{Fore.LIGHTGREEN_EX}██║░░░░░   {Fore.LIGHTCYAN_EX}│
{Fore.LIGHTCYAN_EX}    │  {Fore.LIGHTRED_EX} ██║░░██║{Fore.LIGHTGREEN_EX}█████╗░░{Fore.LIGHTRED_EX}╚██╗░██╔╝{Fore.LIGHTGREEN_EX}██║{Fore.LIGHTCYAN_EX}██╔██╗██║{Fore.LIGHTRED_EX}█████╗░░  {Fore.LIGHTGREEN_EX}░░░██║░░░{Fore.LIGHTRED_EX}██║░░██║██║░░██║{Fore.LIGHTGREEN_EX}██║░░░░░   {Fore.LIGHTCYAN_EX}│
{Fore.LIGHTCYAN_EX}    │  {Fore.LIGHTRED_EX} ██║░░██║{Fore.LIGHTGREEN_EX}██╔══╝░░{Fore.LIGHTRED_EX}░╚████╔╝░{Fore.LIGHTGREEN_EX}██║{Fore.LIGHTCYAN_EX}██║╚████║{Fore.LIGHTRED_EX}██╔══╝░░  {Fore.LIGHTGREEN_EX}░░░██║░░░{Fore.LIGHTRED_EX}██║░░██║██║░░██║{Fore.LIGHTGREEN_EX}██║░░░░░   {Fore.LIGHTCYAN_EX}│
{Fore.LIGHTCYAN_EX}    │  {Fore.LIGHTRED_EX} ██████╔╝{Fore.LIGHTGREEN_EX}███████╗{Fore.LIGHTRED_EX}░░╚██╔╝░░{Fore.LIGHTGREEN_EX}██║{Fore.LIGHTCYAN_EX}██║░╚███║{Fore.LIGHTRED_EX}███████╗  {Fore.LIGHTGREEN_EX}░░░██║░░░{Fore.LIGHTRED_EX}╚█████╔╝╚█████╔╝{Fore.LIGHTGREEN_EX}███████╗   {Fore.LIGHTCYAN_EX}│
{Fore.LIGHTCYAN_EX}    │  {Fore.LIGHTRED_EX} ╚═════╝░{Fore.LIGHTGREEN_EX}╚══════╝{Fore.LIGHTRED_EX}░░░╚═╝░░░{Fore.LIGHTGREEN_EX}╚═╝{Fore.LIGHTCYAN_EX}╚═╝░░╚══╝{Fore.LIGHTRED_EX}╚══════╝  {Fore.LIGHTGREEN_EX}░░░╚═╝░░░{Fore.LIGHTRED_EX}░╚════╝░░╚════╝░{Fore.LIGHTGREEN_EX}╚══════╝   {Fore.LIGHTCYAN_EX}│
{Fore.LIGHTCYAN_EX}    │                                                                                      │
{Fore.LIGHTCYAN_EX}    │                         {Fore.LIGHTWHITE_EX}Dev:{Fore.LIGHTGREEN_EX} xNetting / {Fore.LIGHTWHITE_EX}Grupo: {Fore.LIGHTGREEN_EX}Panic Squad    {Fore.LIGHTCYAN_EX}                       │
{Fore.LIGHTCYAN_EX}    │                                                                                      │
{Fore.LIGHTCYAN_EX}    └──────────────────────────────────────────────────────────────────────────────────────┘ 

    ''')

def searchGoogle(requete='', requete2=''):

	encodeDic = {
		"%21": "!",
		"%23": "#",
		"%24": "$",
		"%26": "&",
		"%27": "'",
		"%28": "(",
		"%29": ")",
		"%2A": "*",
		"%2B": "+",
		"%2C": ",",
		"%2F": "/",
		"%3A": ":",
		"%3B": ";",
		"%3D": "=",
		"%3F": "?",
		"%40": "@",
		"%5B": "[",
		"%5D": "]", 
		"%20": " ",
		"%22": "\"",
		"%25": "%",
		"%2D": "-",
		"%2E": ".",
		"%3C": "<",
		"%3E": ">",
		"%5C": "\\",
		"%5E": "^",
		"%5F": "_",
		"%60": "`",
		"%7B": "{",
		"%7C": "|",
		"%7D": "}",
		"%7E": "~",
	}

	if requete2 != '':
		content = requete2.text
		urls = re.findall('url\\?q=(.*?)&', content)
		for url in urls:
			for char in encodeDic:
				find = re.search(char, url)
				if find:
					charDecode = encodeDic.get(char)
					url = url.replace(char, charDecode)
			if not "googleusercontent" in url:
				if not "/settings/ads" in url:
					if not "/policies/faq" in url:
						print(str(f"""
                        
    {Fore.LIGHTCYAN_EX}[ + ] Posible conexion : {Fore.LIGHTWHITE_EX}{url}"""))
	else:
		pass

	content = requete.text
	urls = re.findall('url\\?q=(.*?)&', content)
	for url in urls:
		for char in encodeDic:
			find = re.search(char, url)
			if find:
				charDecode = encodeDic.get(char)
				url = url.replace(char, charDecode)
		if not "googleusercontent" in url:
			if not "/settings/ads" in url:
				if not "/policies/faq" in url:
					print(str(f"""
                        
    {Fore.LIGHTCYAN_EX}[ + ] Posible conexion : {Fore.LIGHTWHITE_EX}{url}"""))

def google():
    print(f'''
    
{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                  {Fore.LIGHTRED_EX}Ingrese el nombre{Fore.LIGHTCYAN_EX}                  │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    nombre = input(f'''
    
    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')
    print(str(f'''
            
    {Fore.LIGHTCYAN_EX}[ + ] Buscando informacion de : {Fore.LIGHTWHITE_EX}{nombre}'''))
    
    url = "https://www.google.com/search?num=20&q=\\%s\\"
    try:
        lista = ""
        nom2 = nombre.split()
        if len(nom2) == 0:
            print(f'''
            
    {Fore.LIGHTCYAN_EX}[ ! ] : {Fore.LIGHTWHITE_EX}Faltan argumentos''')
            return
        longi = str(nom2[-1])
        for argumento in nom2:
            if argumento == longi:
                lista += str(argumento)
                continue
            lista += str(argumento) + "+"
    except:
        pass
    requete = requests.get(url % (lista))
    searchGoogle(requete=requete)


def searchUserName():
    print(f'''
    
{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                   {Fore.MAGENTA}Ingrese el Nick{Fore.LIGHTCYAN_EX}                   │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')
    
    name = input(f'''
    
    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    print(str(f'''
            
    {Fore.LIGHTCYAN_EX}[ + ] Buscando informacion de : {Fore.LIGHTWHITE_EX}{name}'''))
    url = "https://www.google.com/search?num=100&q=\\%s\\"
    url2 = "https://www.google.com/search?num=100&q=\\intitle:\"%s\"\\"
    requete = requests.get(url % (name))
    requete2 = requests.get(url2 % (name))
    searchGoogle(requete=requete, requete2=requete2)

def deleterequest(url):
	headers = {"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
	req = request.Request(url,headers=headers,method="DELETE")
	request.urlopen(req)

def nmapscan():
    print(f'''
    
    {Fore.LIGHTCYAN_EX}┌─────────────────────────────────────────────────────┐
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│           {Fore.LIGHTGREEN_EX}Ponga la IP que desea escanear{Fore.LIGHTCYAN_EX}            │                      
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}└─────────────────────────────────────────────────────┘

    ''')

    target_2 = str(input(f'''
    
    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}'''))

    nm = nmap.PortScanner()
    results = nm.scan(hosts=target_2, arguments='-sT -n -Pn -T4')
    open_ports = '-p '

    num = 0

    print(f'''

    {Fore.LIGHTCYAN_EX}[ + ] Host : {Fore.LIGHTWHITE_EX}%s''' % target_2)
    print(f'''

    {Fore.LIGHTCYAN_EX}[ + ] Estado : {Fore.LIGHTWHITE_EX}%s''' % nm[target_2].state())

    for protocolo in nm[target_2].all_protocols():
        print(f'''
        
    {Fore.LIGHTCYAN_EX}[ + ] Protocolo : {Fore.LIGHTWHITE_EX}%s''' % protocolo)
        puerto = nm[target_2][protocolo].keys()
        sorted(puerto)

        for port in puerto:
            print(f'''
            
    {Fore.LIGHTCYAN_EX}[ + ] Puerto : {Fore.LIGHTWHITE_EX}%s, {Fore.LIGHTCYAN_EX}[ + ] Estado : {Fore.LIGHTWHITE_EX}%s''' % (port, nm[target_2][protocolo][port]['state']))
            if num == 0:
                open_ports = open_ports+str(port)
                num = 1
            else:
                open_ports = open_ports+", "+str(port)

    print(f'''
    
    {Fore.LIGHTCYAN_EX}[ + ] Puertos abiertos : {Fore.LIGHTWHITE_EX}{open_ports} en {target_2}''')  

def scan5():
    print(f'''
    
    {Fore.LIGHTCYAN_EX}┌─────────────────────────────────────────────────────┐
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│         {Fore.LIGHTRED_EX}Ingrese la url que quiere escanear{Fore.LIGHTCYAN_EX}          │                      
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}└─────────────────────────────────────────────────────┘

    ''')

    target_7 = input(f'''
    
    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    try:
        obj = requests.get(url=target_7)
        ca = dict(obj.headers)
        for x in ca:
            print(f'''
            
    {Fore.LIGHTCYAN_EX}[ + ] : {Fore.LIGHTWHITE_EX}{x} {ca[x]}''')
    
    except:
        print(f'''
        
    {Fore.LIGHTCYAN_EX}[ ! ] : {Fore.LIGHTWHITE_EX}No se encontro informacion ''')

def dnsscan4():
    print(f'''
    
    {Fore.LIGHTCYAN_EX}┌─────────────────────────────────────────────────────┐
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│       {Fore.LIGHTGREEN_EX}Ingrese el dominio que quiere escanear{Fore.LIGHTCYAN_EX}        │                      
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}└─────────────────────────────────────────────────────┘

    ''')

    target_6 = input(f'''
    
    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    try:
        scan = dns.resolver.resolve(target_6, 'MX')
        for a in scan:
            print(f'''
            
    {Fore.LIGHTCYAN_EX}[ + ] : {Fore.LIGHTWHITE_EX}{a}''')

    except:
        print(f'''
        
    {Fore.LIGHTCYAN_EX}[ ! ] : {Fore.LIGHTWHITE_EX}No se encontro informacion ''')

def dnsscan3():
    print(f'''
    
    {Fore.LIGHTCYAN_EX}┌─────────────────────────────────────────────────────┐
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│       {Fore.LIGHTRED_EX}Ingrese el dominio que quiere escanear{Fore.LIGHTCYAN_EX}        │                      
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}└─────────────────────────────────────────────────────┘

    ''')

    target_5 = input(f'''
    
    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    try:
        scan = dns.resolver.resolve(target_5, 'SOA')
        for a in scan:
            print(f'''
            
    {Fore.LIGHTCYAN_EX}[ + ] : {Fore.LIGHTWHITE_EX}{a}''')

    except:
        print(f'''
        
    {Fore.LIGHTCYAN_EX}[ ! ] : {Fore.LIGHTWHITE_EX}No se encontro informacion ''')

def dnsscan2():
    print(f'''
    
    {Fore.LIGHTCYAN_EX}┌─────────────────────────────────────────────────────┐
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│       {Fore.LIGHTWHITE_EX}Ingrese el dominio que quiere escanear{Fore.LIGHTCYAN_EX}        │                      
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}└─────────────────────────────────────────────────────┘

    ''')

    target_4 = input(f'''
    
    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    try:
        scan = dns.resolver.resolve(target_4, 'NS')
        for a in scan:
            print(f'''
            
    {Fore.LIGHTCYAN_EX}[ + ] : {Fore.LIGHTWHITE_EX}{a}''')
    
    except:
        print(f'''
        
    {Fore.LIGHTCYAN_EX}[ ! ] : {Fore.LIGHTWHITE_EX}No se encontro informacion ''')

def dnsscan1():
    print(f'''
    
    {Fore.LIGHTCYAN_EX}┌─────────────────────────────────────────────────────┐
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│       {Fore.LIGHTGREEN_EX}Ingrese el dominio que quiere escanear{Fore.LIGHTCYAN_EX}        │                      
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}└─────────────────────────────────────────────────────┘

    ''')

    target_3 = input(f'''
    
    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    try:
        scan = dns.resolver.resolve(target_3, 'A')
        for a in scan:
            print(f'''
            
    {Fore.LIGHTCYAN_EX}[ + ] : {Fore.LIGHTWHITE_EX}{a}''')

    except:
        print(f'''
        
    {Fore.LIGHTCYAN_EX}[ ! ] : {Fore.LIGHTWHITE_EX}No se encontro informacion ''')   

def otrosscan():
    print(f'''

    {Fore.LIGHTCYAN_EX}┌─────────────────────────────────────────────────────┐
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│   {Fore.LIGHTWHITE_EX}Eliga su tipo de scan{Fore.LIGHTCYAN_EX}                             │                      
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│        {Fore.LIGHTGREEN_EX}1 - Direccion Host{Fore.LIGHTCYAN_EX}                           │
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│        {Fore.LIGHTRED_EX}2 - Obtener DNS{Fore.LIGHTCYAN_EX}                              │
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│        {Fore.LIGHTCYAN_EX}3 - Informacion DNS de la zona{Fore.LIGHTCYAN_EX}               │   
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│        {Fore.LIGHTGREEN_EX}4 - Informacion de Intercambio{Fore.LIGHTCYAN_EX}               │   
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│        {Fore.LIGHTRED_EX}5 - All Info{Fore.LIGHTCYAN_EX}                                 │                     
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}└─────────────────────────────────────────────────────┘

    ''')

    opcion = input(f'''
    
    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    if opcion == '1':
        dnsscan1()
    elif opcion == '2':
        dnsscan2()
    elif opcion == '3':
        dnsscan3()
    elif opcion == '4':
        dnsscan4()
    elif opcion == '5':
        scan5()
    else:
        sys.exit()

def portscan():
    open_ports = []
    port_min = 0
    port_max = 65535
    patrones_puertos = re.compile("([0-9]+)-([0-9]+)")

    while True:
        print(f'''
    
    {Fore.LIGHTCYAN_EX}┌─────────────────────────────────────────────────────┐
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│           {Fore.LIGHTGREEN_EX}Ponga la IP que desea escanear{Fore.LIGHTCYAN_EX}            │                      
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}└─────────────────────────────────────────────────────┘
    
        ''')

        target_1 = str(input(f'''
    
    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}'''))
        break

    while True:
        print(f'''
    
    {Fore.LIGHTCYAN_EX}┌─────────────────────────────────────────────────────┐
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│      {Fore.LIGHTRED_EX}Ponga el rango de Puertos para escanear{Fore.LIGHTCYAN_EX}        │                      
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}│                                                     │
    {Fore.LIGHTCYAN_EX}└─────────────────────────────────────────────────────┘
    
        ''')

        port_1 = str(input(f'''
    
    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}'''))

        port_validacion = patrones_puertos.search(port_1.replace(" ",""))
        if port_validacion:
            port_min = int(port_validacion.group(1))
            port_max = int(port_validacion.group(2))
        break

    for port in range(port_min, port_max + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scan:
                scan.settimeout(0.5)
                scan.connect((target_1, port))
                open_ports.append(port)
        except:
            pass
    for port in open_ports:
        print(f'''
        
    {Fore.LIGHTCYAN_EX}[ + ] : {Fore.LIGHTWHITE_EX}El puerto {port} esta abierto en {target_1}''')

def scanning():
    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │   {Fore.LIGHTWHITE_EX}Eliga el tipo de scan que quiere realizar{Fore.LIGHTCYAN_EX}         │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │   {Fore.MAGENTA}     1 - Port Scan{Fore.LIGHTCYAN_EX}                                │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │   {Fore.LIGHTGREEN_EX}     2 - Nmap Scan{Fore.LIGHTCYAN_EX}                                │                     
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │   {Fore.LIGHTCYAN_EX}     3 - Otros Scans{Fore.LIGHTCYAN_EX}                              │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    op_scan = input(f'''
    
    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    if op_scan == '1':
        portscan()
    elif op_scan == '2':
        nmapscan()
    elif op_scan == '3':
        otrosscan()
    else:
        sys.exit() 

def wordlistgen():
    print(f'''
    
{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │    {Fore.LIGHTRED_EX}Ingrese el minimo de letras de las contraseñas{Fore.LIGHTCYAN_EX}   │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    min_let = int(input(f'''
    
    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}'''))

    print(f'''
    
{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │    {Fore.LIGHTGREEN_EX}Ingrese el maximo de letras de las contraseñas{Fore.LIGHTCYAN_EX}   │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘
    
    ''')

    max_let = int(input(f'''
    
    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}'''))

    contador = 0

    caracter = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

    archivo = open('wordlist.txt', 'w')

    for i in range(min_let, max_let+1):
        for j in product(caracter, repeat=i):
            let = ''.join(j) 
            archivo.write(let)
            archivo.write('\n')
            contador += 1
    print(f'''
    
    {Fore.LIGHTCYAN_EX}[ + ] : {Fore.LIGHTWHITE_EX}WordList ha sido creado, genero {contador} contraseñas''') 

def decode_sha1():
    f = 0
    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │             {Fore.LIGHTGREEN_EX}Ingrese el hash en SHA1{Fore.LIGHTCYAN_EX}                 │                      
 {Fore.LIGHTCYAN_EX}   │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    sha1_hash = input(f'''

    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')    

    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │            {Fore.LIGHTWHITE_EX}Escriba la wordlist (.txt){Fore.LIGHTCYAN_EX}               │                        
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    sha1_wordlist = input(f'''

    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    try:
        archivo = open(sha1_wordlist, 'r')
    except:
        print(f'''
        
    {Fore.LIGHTCYAN_EX}[ ! ] : {Fore.LIGHTWHITE_EX}No se encontro la wordlist ''')

    for l in archivo:
        le = l.encode('utf-8')
        d = hashlib.sha1(le.strip()).hexdigest()

        if d == sha1_hash:
            print(f'''
        
    {Fore.LIGHTCYAN_EX}[ + ] Hash : {Fore.LIGHTWHITE_EX}{l}''')
            f = 1

    if f == 0:
        print(f'''
        
    {Fore.LIGHTCYAN_EX}[ ! ] : {Fore.LIGHTWHITE_EX}No se encontro la wordlist ''')

def decode_sha256():
    f = 0
    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │            {Fore.LIGHTRED_EX} Ingrese el hash en SHA256{Fore.LIGHTCYAN_EX}               │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    sha256_hash = input(f'''

    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')    

    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │           {Fore.LIGHTWHITE_EX} Escriba la wordlist (.txt){Fore.LIGHTCYAN_EX}               │                        
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    sha256_wordlist = input(f'''

    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    try:
        archivo = open(sha256_wordlist, 'r')
    except:
        print(f'''
        
    {Fore.LIGHTCYAN_EX}[ ! ] : {Fore.LIGHTWHITE_EX}No se encontro la wordlist ''')

    for l in archivo:
        le = l.encode('utf-8')
        d = hashlib.sha256(le.strip()).hexdigest()

        if d == sha256_hash:
            print(f'''
        
    {Fore.LIGHTCYAN_EX}[ + ] Hash : {Fore.LIGHTWHITE_EX}{l}''')
            f = 1

    if f == 0:
        print(f'''
        
    {Fore.LIGHTCYAN_EX}[ ! ] : {Fore.LIGHTWHITE_EX}No se encontro la wordlist ''')

def decode_sha224():
    f = 0
    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │           {Fore.LIGHTRED_EX} Ingrese el hash en SHA224{Fore.LIGHTCYAN_EX}                │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    sha224_hash = input(f'''

    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')    

    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │            {Fore.LIGHTGREEN_EX}Escriba la wordlist (.txt){Fore.LIGHTCYAN_EX}               │                        
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    sha224_wordlist = input(f'''

    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    try:
        archivo = open(sha224_wordlist, 'r')
    except:
        print(f'''
        
    {Fore.LIGHTCYAN_EX}[ ! ] : {Fore.LIGHTWHITE_EX}No se encontro la wordlist ''')

    for l in archivo:
        le = l.encode('utf-8')
        d = hashlib.sha224(le.strip()).hexdigest()

        if d == sha224_hash:
            print(f'''
        
    {Fore.LIGHTCYAN_EX}[ + ] Hash : {Fore.LIGHTWHITE_EX}{l}''')
            f = 1

    if f == 0:
        print(f'''
        
    {Fore.LIGHTCYAN_EX}[ ! ] : {Fore.LIGHTWHITE_EX}No se encontro la wordlist ''')

def decode_sha3_256():
    f = 0
    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │           {Fore.LIGHTRED_EX}  Ingrese el hash en SHA3_256{Fore.LIGHTCYAN_EX}             │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    sha3_256_hash = input(f'''

    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')    

    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │          {Fore.LIGHTWHITE_EX}  Escriba la wordlist (.txt){Fore.LIGHTCYAN_EX}               │                        
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    sha3_256_wordlist = input(f'''

    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    try:
        archivo = open(sha3_256_wordlist, 'r')
    except:
        print(f'''
        
    {Fore.LIGHTCYAN_EX}[ ! ] : {Fore.LIGHTWHITE_EX}No se encontro la wordlist ''')

    for l in archivo:
        le = l.encode('utf-8')
        d = hashlib.sha3_256(le.strip()).hexdigest()

        if d == sha3_256_hash:
            print(f'''
        
    {Fore.LIGHTCYAN_EX}[ + ] Hash : {Fore.LIGHTWHITE_EX}{l}''')
            f = 1

    if f == 0:
        print(f'''
        
    {Fore.LIGHTCYAN_EX}[ ! ] : {Fore.LIGHTWHITE_EX}No se encontro la wordlist ''')

def decode_blakeb2():
    f = 0
    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │             {Fore.LIGHTGREEN_EX}Ingrese el hash en blake 2b{Fore.LIGHTCYAN_EX}             │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    blakeb2_hash = input(f'''

    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')    

    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │          {Fore.LIGHTRED_EX}  Escriba la wordlist (.txt){Fore.LIGHTCYAN_EX}               │                        
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    blakeb2_wordlist = input(f'''

    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    try:
        archivo = open(blakeb2_wordlist, 'r')
    except:
        print(f'''
        
    {Fore.LIGHTCYAN_EX}[ ! ] : {Fore.LIGHTWHITE_EX}No se encontro la wordlist ''')

    for l in archivo:
        le = l.encode('utf-8')
        d = hashlib.blake2b(le.strip()).hexdigest()

        if d == blakeb2_hash:
            print(f'''
        
    {Fore.LIGHTCYAN_EX}[ + ] Hash : {Fore.LIGHTWHITE_EX}{l}''')
            f = 1

    if f == 0:
        print(f'''
        
    {Fore.LIGHTCYAN_EX}[ ! ] : {Fore.LIGHTWHITE_EX}No se encontro la wordlist ''')

def decode_md5():
    f = 0
    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │          {Fore.LIGHTWHITE_EX}    Ingrese el hash en MD5{Fore.LIGHTCYAN_EX}                 │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    md5_hash = input(f'''

    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')    

    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │          {Fore.LIGHTRED_EX}  Escriba la wordlist (.txt){Fore.LIGHTCYAN_EX}               │                        
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    md5_wordlist = input(f'''

    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    try:
        archivo = open(md5_wordlist, 'r')
    except:
        print(f'''
        
    {Fore.LIGHTCYAN_EX}[ ! ] : {Fore.LIGHTWHITE_EX}No se encontro la wordlist ''')

    for l in archivo:
        le = l.encode('utf-8')
        d = hashlib.md5(le.strip()).hexdigest()

        if d == md5_hash:
            print(f'''
        
    {Fore.LIGHTCYAN_EX}[ + ] Hash : {Fore.LIGHTWHITE_EX}{l}''')
            f = 1

    if f == 0:
        print(f'''
        
    {Fore.LIGHTCYAN_EX}[ ! ] : {Fore.LIGHTWHITE_EX}No se encontro la wordlist ''')


def encode_sha3_256():
    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │ {Fore.LIGHTGREEN_EX}Escriba el texto que quiere encriptar en SHA3_256{Fore.LIGHTCYAN_EX}   │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    sha3_256_encrypted = input(f'''

    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    print(f'''

    {Fore.LIGHTCYAN_EX}[ + ] : {Fore.LIGHTWHITE_EX} ''' + hashlib.sha3_256(sha3_256_encrypted.encode('utf-8')).hexdigest())

def encode_blake2b():
    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │  {Fore.LIGHTWHITE_EX}Escriba el texto que quiere encriptar en blake2b{Fore.LIGHTCYAN_EX}   │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    blake2b_encrypted = input(f'''

    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    print(f'''

    {Fore.LIGHTCYAN_EX}[ + ] : {Fore.LIGHTWHITE_EX} ''' + hashlib.blake2b(blake2b_encrypted.encode('utf-8')).hexdigest())

def algoritmos():
    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │        {Fore.LIGHTGREEN_EX}Aqui tiene la lista de algoritmos{Fore.LIGHTCYAN_EX}            │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    print(f'''
    
    {Fore.LIGHTCYAN_EX}[ + ] : {Fore.LIGHTWHITE_EX}{hashlib.algorithms_available}''')

def encode_sha224():
    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │ {Fore.LIGHTRED_EX} Escriba el texto que quiere encriptar en SHA224{Fore.LIGHTCYAN_EX}    │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    sha224_encrypted = input(f'''

    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    print(f'''

    {Fore.LIGHTCYAN_EX}[ + ] : {Fore.LIGHTWHITE_EX} ''' + hashlib.sha224(sha224_encrypted.encode('utf-8')).hexdigest())

def encode_sha256():
    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │ {Fore.LIGHTWHITE_EX} Escriba el texto que quiere encriptar en SHA265{Fore.LIGHTCYAN_EX}    │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    sha256_encrypted = input(f'''

    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    print(f'''

    {Fore.LIGHTCYAN_EX}[ + ] : {Fore.LIGHTWHITE_EX} ''' + hashlib.sha256(sha256_encrypted.encode('utf-8')).hexdigest())

def encode_sha1():
    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │   {Fore.LIGHTRED_EX}Escriba el texto que quiere encriptar en SHA1{Fore.LIGHTCYAN_EX}     │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    sha1_encrypted = input(f'''

    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    print(f'''

    {Fore.LIGHTCYAN_EX}[ + ] : {Fore.LIGHTWHITE_EX} ''' + hashlib.sha1(sha1_encrypted.encode('utf-8')).hexdigest())


def encode_md5():
    print(f'''
    
{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │  {Fore.LIGHTWHITE_EX} Escriba el texto que quiere encriptar en MD5{Fore.LIGHTCYAN_EX}      │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    md5_encrypted = input(f'''

    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    print(f'''

    {Fore.LIGHTCYAN_EX}[ + ] : {Fore.LIGHTWHITE_EX} ''' + hashlib.md5(md5_encrypted.encode('utf-8')).hexdigest())

def tans():
    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │  {Fore.LIGHTWHITE_EX} Eliga el metodo que quiere{Fore.LIGHTCYAN_EX}                        │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │     {Fore.LIGHTWHITE_EX}   1 - Encrypt{Fore.LIGHTCYAN_EX}                                  │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │        {Fore.LIGHTGREEN_EX}2 - Decrypt{Fore.LIGHTCYAN_EX}                                  │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │   {Fore.LIGHTRED_EX}     3 - Generar diccionario{Fore.LIGHTCYAN_EX}                      │                     
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    opcion = input(f'''
    
    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')   

    if opcion == '1':
        encrypt()
    elif opcion == '2':
        decrypt()
    elif opcion == '3':
        wordlistgen()
    else:
        sys.exit()

def decrypt():
    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │  {Fore.LIGHTWHITE_EX} Eliga el metodo que quiere para su desencriptacion{Fore.LIGHTCYAN_EX}│                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │        {Fore.LIGHTGREEN_EX}1 - MD5{Fore.LIGHTCYAN_EX}                                      │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │      {Fore.LIGHTRED_EX}  2 - SHA1{Fore.LIGHTCYAN_EX}                                     │                     
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │        {Fore.LIGHTGREEN_EX}3 - SHA256{Fore.LIGHTCYAN_EX}                                   │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │      {Fore.LIGHTWHITE_EX}  4 - SHA224{Fore.LIGHTCYAN_EX}                                   │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │        {Fore.LIGHTGREEN_EX}5 - blake2b{Fore.LIGHTCYAN_EX}                                  │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │       {Fore.LIGHTRED_EX} 6 - SHA3_256{Fore.LIGHTCYAN_EX}                                 │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    opcion = input(f'''
    
    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    if opcion == '1':
        decode_md5()
    elif opcion == '2':
        decode_sha1()
    elif opcion == '3':
        decode_sha256()
    elif opcion == '4':
        decode_sha224()
    elif opcion == '5':
        decode_blakeb2()
    elif opcion == '6':
        decode_sha3_256()
    else:
        sys.exit()

def encrypt():
    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │  {Fore.LIGHTWHITE_EX} Eliga el metodo que quiere para su encriptacion{Fore.LIGHTCYAN_EX}   │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │        {Fore.LIGHTRED_EX}1 - MD5{Fore.LIGHTCYAN_EX}                                      │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │      {Fore.LIGHTGREEN_EX}  2 - SHA1{Fore.LIGHTCYAN_EX}                                     │                     
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │      {Fore.LIGHTWHITE_EX}  3 - SHA256{Fore.LIGHTCYAN_EX}                                   │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │       {Fore.LIGHTRED_EX} 4 - SHA224{Fore.LIGHTCYAN_EX}                                   │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │      {Fore.LIGHTWHITE_EX}  5 - blake2b{Fore.LIGHTCYAN_EX}                                  │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │        {Fore.LIGHTRED_EX}6 - SHA3_256{Fore.LIGHTCYAN_EX}                                 │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │      {Fore.LIGHTGREEN_EX}  10 - Todos los Algoritmos{Fore.LIGHTCYAN_EX}                    │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    opcion = input(f'''
    
    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    if opcion == '1':
        encode_md5()
    elif opcion == '2':
        encode_sha1()
    elif opcion == '3':
        encode_sha256()
    elif opcion == '4':
        encode_sha224()
    elif opcion == '5':
        encode_blake2b()
    elif opcion == '6':
        encode_sha3_256()
    elif opcion == '10':
        algoritmos()
    else:
        sys.exit()

def webhook():
    print(f'''
    
{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │           {Fore.LIGHTWHITE_EX}Ingrese la URL de su webhook{Fore.LIGHTCYAN_EX}              │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    webhookurl = input(f'''
    
    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    print(f'''
    
{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │        {Fore.LIGHTRED_EX}  Ingrese el nombre para su webhook{Fore.LIGHTCYAN_EX}          │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    webhooknombre = input(f'''
    
    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    print(f'''
    
{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │        {Fore.LIGHTGREEN_EX}  Ingrese el contenido de su webhook {Fore.LIGHTCYAN_EX}        │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    webhookcontenido = input(f'''
    
    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    data = {
        "content" : webhookcontenido,
        "username" : webhooknombre
    }

    def send(i):
        res = requests.post(webhookurl, data=data)
        try:
            print(f'''
            
    {Fore.LIGHTCYAN_EX}[ ! ] Tiempo en rehabilitacion, espere :{Fore.LIGHTWHITE_EX} {str(res.json()["retry_after"])} ms''')
            
            time.sleep(res.json()["retry_after"]/1000)
            res = f'''
            
    {Fore.LIGHTCYAN_EX}[ ! ] Espere : {str(res.json()["retry_after"])} ms'''
        except:
            i += 1
        print(f'''
        
    {Fore.LIGHTCYAN_EX}[ + ] Cantidad de mensajes enviados :{Fore.LIGHTWHITE_EX} {str(i)}''')
        return i
    i = 0
    while True:
        i = send(i)

def discord():
    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │   {Fore.LIGHTWHITE_EX}Eliga el tipo de mensaje webhook que quiere{Fore.LIGHTCYAN_EX}       │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │        {Fore.LIGHTGREEN_EX}1 - Spammer{Fore.LIGHTCYAN_EX}                                  │                 
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    opciones = input(f'''
    
    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    if opciones == '1':
        webhook()
    else:
        sys.exit()

def ddos():
    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │   {Fore.LIGHTWHITE_EX}Eliga su tipo de DDoS{Fore.LIGHTCYAN_EX}                             │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │        {Fore.LIGHTGREEN_EX}1 - DDoS Thread {Fore.LIGHTCYAN_EX}[{Fore.LIGHTWHITE_EX} PREMIUM{Fore.LIGHTCYAN_EX} ]{Fore.LIGHTCYAN_EX}                  │     
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │        {Fore.MAGENTA}2 - DDoS Proxies {Fore.LIGHTCYAN_EX}[{Fore.LIGHTWHITE_EX} PREMIUM{Fore.LIGHTCYAN_EX} ]{Fore.LIGHTCYAN_EX}                 │                     
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    opciones = input(f'''
    
    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    if opciones == '1':
        print(f'''
    
    {Fore.LIGHTCYAN_EX}[ X ] : {Fore.RED}Al parecer tu no has comprado la Devine Tool Premium{Fore.LIGHTWHITE_EX}''')
    elif opciones == '2':
        print(f'''
    
    {Fore.LIGHTCYAN_EX}[ X ] : {Fore.RED}Al parecer tu no has comprado la Devine Tool Premium{Fore.LIGHTWHITE_EX}''')
    else:
        sys.exit()

def ipinfo():
    print(f'''
    
{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                   {Fore.LIGHTGREEN_EX}Ingrese el IP{Fore.LIGHTCYAN_EX}                     │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    aipi = input(f'''
    
    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    url = ("http://ip-api.com/json/")
    response = requests.get(url + aipi)
    data = response.text
    jso = json.loads(data)
    print(str(f'''
    
    {Fore.LIGHTCYAN_EX}[ + ] IP : {Fore.LIGHTWHITE_EX}{aipi}'''))
    print(str(f'''
    
    {Fore.LIGHTCYAN_EX}[ + ] ISP : {Fore.LIGHTWHITE_EX}'''+(jso["isp"])))
    print(str(f'''
    
    {Fore.LIGHTCYAN_EX}[ + ] Pais : {Fore.LIGHTWHITE_EX}'''+(jso["country"])))
    print(str(f'''
    
    {Fore.LIGHTCYAN_EX}[ + ] TimeZone : {Fore.LIGHTWHITE_EX}'''+(jso["timezone"])))
    print(str(f'''
    
    {Fore.LIGHTCYAN_EX}[ + ] Region : {Fore.LIGHTWHITE_EX}'''+(jso["regionName"])))
    print(str(f'''
    
    {Fore.LIGHTCYAN_EX}[ + ] Zip : {Fore.LIGHTWHITE_EX}'''+(jso["zip"])))
    print(str(f'''
    
    {Fore.LIGHTCYAN_EX}[ + ] Cuidad : {Fore.LIGHTWHITE_EX}'''+(jso["city"])))

def doxing():
    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │   {Fore.LIGHTWHITE_EX}Eliga su tipo de Dox{Fore.LIGHTCYAN_EX}                              │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │        {Fore.LIGHTRED_EX}1 - Redes{Fore.LIGHTCYAN_EX}                                    │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │        {Fore.LIGHTGREEN_EX}2 - Nick{Fore.LIGHTCYAN_EX}                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │        {Fore.LIGHTWHITE_EX}3 - IP Info{Fore.LIGHTCYAN_EX}                                  │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')
    
    opciones = input(f'''
    
    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    if opciones == '1':
        searchUserName()
    elif opciones == '2':
        google()
    elif opciones == '3':
        ipinfo()
    else:
        sys.exit()

def main():
    print(f'''

{Fore.LIGHTCYAN_EX}    ┌─────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │   {Fore.LIGHTWHITE_EX}Eliga la herramienta que quiere usar{Fore.LIGHTCYAN_EX}              │                      
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │   {Fore.LIGHTGREEN_EX}     1 - Scanning{Fore.LIGHTCYAN_EX}                                 │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │   {Fore.LIGHTWHITE_EX}     2 - Encrypt & Decrypt{Fore.LIGHTCYAN_EX}                        │                     
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │   {Fore.YELLOW}     3 - Discord{Fore.LIGHTCYAN_EX}                                  │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │   {Fore.LIGHTCYAN_EX}     4 - DDoS & DoS{Fore.LIGHTCYAN_EX}                               │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │   {Fore.MAGENTA}     5 - Doxing{Fore.LIGHTCYAN_EX}                                   │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    │                                                     │
{Fore.LIGHTCYAN_EX}    └─────────────────────────────────────────────────────┘

    ''')

    opciones = input(f'''
    
    {Fore.LIGHTCYAN_EX}[ ? ] : {Fore.LIGHTWHITE_EX}''')

    if opciones == '1':
        scanning()
    elif opciones == '2':
        tans()
    elif opciones == '3':
        discord()
    elif opciones == '4':
        ddos()
    elif opciones == '5':
        doxing()
    else:
        sys.exit()

main()
