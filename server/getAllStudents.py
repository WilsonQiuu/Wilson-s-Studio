# takes a json file with the sensei info and updates the database

import os
import json
import time


with open("schedule.txt", "r") as file:
        jsonFile = file.read()
        
        # get a list of all students for the sensei
        listOfSenseis = []
        
        listOfStudents = []
        
        
        
        
        # get a list of all senseis
        for key in json.loads(jsonFile):
            for senseiPairs in json.loads(jsonFile)[key]:
                for key in senseiPairs:
                    if senseiPairs[key] == "Sensei Michael":
                        if(key not in listOfStudents):
                            listOfStudents.append(key)
                    
                 
                        
        
        
                
        
        file.close()
        print(listOfStudents)
        
        

    