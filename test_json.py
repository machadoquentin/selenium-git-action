import csv
import random
from colorama import Fore, deinit, init
init()
def load_data():
    with open('anime.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        ligne = list(reader)
        randomMovie(ligne)
def randomMovie(ligne):
    for i in range(0,10):
        print_movie(ligne,i) 
def print_movie(ligne,i):
    if i % 2  == 0:
        print(Fore.RED + "Le nom du film est ",Fore.WHITE + random.choice(ligne)['Name'], Fore.RED + " et il est noté : ",Fore.WHITE +random.choice(ligne)['Rating'],Fore.RED+ " pour ",Fore.WHITE+random.choice(ligne)['Votes'], Fore.RED +" votes")
    else: 
        print(Fore.GREEN + "Le nom du film est ",Fore.WHITE + random.choice(ligne)['Name'] ,Fore.GREEN+ " et il est noté :  ",Fore.WHITE +random.choice(ligne)['Rating'],Fore.GREEN+" pour ",Fore.WHITE +random.choice(ligne)['Votes'],Fore.GREEN+" votes")
load_data()
deinit()

