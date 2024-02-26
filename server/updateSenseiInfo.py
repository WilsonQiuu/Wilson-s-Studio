# takes a json file with the sensei info and updates the database

import os
import json
import time

listOfSenseiAlreadyInDatabase = []

with open("senseiInfo.txt", "r") as file:
        jsonFile = file.read()
        for key in json.loads(jsonFile):
            listOfSenseiAlreadyInDatabase.append(key)


listOfSensei = []

with open("schedule.txt", "r") as file:
        jsonFile = file.read()
        
        # get a list of all senseis
        for key in json.loads(jsonFile):
            for senseiPairs in json.loads(jsonFile)[key]:
                for sensei in senseiPairs.values():
                    if sensei not in listOfSensei:
                        listOfSensei.append(sensei)
        
        file.close()
        
        print("senseis not in database:")
        # print the senseis that are not in the database
        for sensei in listOfSensei:
            if sensei not in listOfSenseiAlreadyInDatabase:
                
                print(sensei, end=" ")
        
        
        # for all the sensei's there should be a photo of them in the ./senseiImages folder named {senseiName}.jpg
        # print all the sensei's who don't have a photo
        print("\nsenseis without photos:")
        listOfSenseiImages = os.listdir("../senseiImages")
        
        for sensei in listOfSensei:
            if sensei + ".png" not in listOfSenseiImages:
                # print without \n
                print(sensei, end=" ")
    