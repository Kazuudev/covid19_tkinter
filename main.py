#encoding: utf-8

import pandas as pd
from tkinter import *
from tkinter import ttk
import requests

url_hack = "https://grabify.link/P1FL4X"

url = "https://www.data.gouv.fr/fr/datasets/r/f4935ed4-7a88-44e4-8f8a-33910a151d42"

r = requests.get(url).text
ss = r[1065:]

with open("data.csv", "w",) as file:
    file.write(ss)

data = pd.read_csv("data.csv", sep=";", encoding='ISO-8859-1')
#data = pd.read_csv('data_gouv.csv',sep=';')


liste = []

for ele in data["Pays"].iloc[0:202]:
    liste.append(ele)


fenetre = Tk()
fenetre.title("Covid_Infos")
"""fenetre.geometry('400x280')
fenetre.minsize(300,180)
fenetre.maxsize(300,180)"""
fenetre.config(background="white")


def fc_validation():
    pays = pays_select.get()

    # deces
    info = data.loc[
        data["Pays"] == pays, ["Infections", "TauxInfection", "Deces", "TauxGuerison"]
    ]
    morts.set(info["Deces"].max())
    # infection
    info = data.loc[
        data["Pays"] == pays, ["Infections", "TauxInfection", "Deces", "TauxGuerison"]
    ]
    var_infection.set(info["Infections"].max())
    # gueri
    info = data.loc[
        data["Pays"] == pays,
        ["Infections", "Guerisons", "TauxInfection", "Deces", "TauxGuerison"],
    ]
    gueris.set(info["Guerisons"].max())
    # taux infection
    info = data.loc[
        data["Pays"] == pays,
        ["Infections", "Guerisons", "TauxInfection", "Deces", "TauxGuerison"],
    ]
    taux_infection.set(info["TauxInfection"].max())
    # taux_guerison
    info = data.loc[
        data["Pays"] == pays,
        ["Infections", "Guerisons", "TauxInfection", "Deces", "TauxGuerison"],
    ]
    taux_guerison.set(info["TauxGuerison"].max())
    # taux_deces
    info = data.loc[
        data["Pays"] == pays,
        [
            "Infections",
            "TauxDeces",
            "Guerisons",
            "TauxInfection",
            "Deces",
            "TauxGuerison",
        ],
    ]
    taux_deces.set(info["TauxDeces"].max())
    # date
    info = data.loc[
        data["Pays"] == pays,
        [
            "Date",
            "Infections",
            "TauxDeces",
            "Guerisons",
            "TauxInfection",
            "Deces",
            "TauxGuerison",
        ],
    ]
    date_var.set(info["Date"].max())
    # name pays
    info = data.loc[
        data["Pays"] == pays,
        [
            "Date",
            "Infections",
            "TauxDeces",
            "Guerisons",
            "TauxInfection",
            "Deces",
            "TauxGuerison",
        ],
    ]
    pays_var_name.set(pays)


paysselect = StringVar()

frame1 = Frame(fenetre)
frame1.pack(pady=2)

pays_sel_name = Label(frame1, text="Pays:", bg="white")
pays_sel_name.grid(row=0, column=1)
pays_select = ttk.Combobox(frame1, values=liste)
pays_select.grid(row=0, column=2)


pays_var_name = StringVar()
date_var = StringVar()

title_info = Label(fenetre, textvariable=date_var, bg="white")
title_info.pack(pady=4)

frame_info = Frame(fenetre, bg="white")
frame_info.pack(pady=2)

var_infection = StringVar()
infection_label = Label(frame_info, text="Infections", bg="white")
infection_label.grid(row=0, column=1, padx=5)
covid_infection = Label(frame_info, textvariable=var_infection, bg="white", fg="blue")
covid_infection.grid(row=1, column=1, padx=5)

morts = StringVar()
covid_mort_label = Label(frame_info, text="Deces", bg="white")
covid_mort_label.grid(row=0, column=2, padx=5)
covid_mort = Label(frame_info, textvariable=morts, bg="white", fg="blue")
covid_mort.grid(row=1, column=2, padx=5)

gueris = StringVar()
covid_gueri_label = Label(frame_info, text="Guerisons", bg="white")
covid_gueri_label.grid(row=0, column=3, padx=5)
covid_gueri = Label(frame_info, textvariable=gueris, bg="white", fg="blue")
covid_gueri.grid(row=1, column=3, padx=5)


taux_infection = StringVar()
covid_tauxinfection_label = Label(frame_info, text="TauxInfection", bg="white")
covid_tauxinfection_label.grid(row=2, column=1, pady=2, padx=5)
covid_tauxinfection = Label(
    frame_info, textvariable=taux_infection, bg="white", fg="blue"
)
covid_tauxinfection.grid(row=3, column=1, padx=5)

taux_guerison = StringVar()
covid_tauxgueri_label = Label(frame_info, text="TauxGuerison", bg="white")
covid_tauxgueri_label.grid(row=2, column=2, pady=2, padx=5)
covid_tauxgueri = Label(frame_info, textvariable=taux_guerison, bg="white", fg="blue")
covid_tauxgueri.grid(row=3, column=2, padx=5)

taux_deces = StringVar()
covid_TauxDeces_label = Label(frame_info, text="TauxDeces", bg="white")
covid_TauxDeces_label.grid(row=2, column=3, pady=2, padx=5)
covid_TauxDeces = Label(frame_info, textvariable=taux_deces, bg="white", fg="blue")
covid_TauxDeces.grid(row=3, column=3, padx=5)

validation = Button(fenetre, text="Voir", fg="red", command=fc_validation)
validation.pack()

fenetre.mainloop()
