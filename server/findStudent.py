import time
from colorama import Fore, Style
import json


# Paste in the student array

scheduledTimes = {
    '9:00 AM':[{'Charlie Austria':'INTERMEDIATE'},], 
    '10:00 AM':[{'Oliver Chan':'Sensei Michael'},{'Rexanna Fung':'Sensei Michael'},{'Summer Wong':'Sensei Michael'},{'Ellanie Logalakshan':'Sensei Joshua'},{'Risha Singam':'Sensei Joshua'},{'Vannes Sum':'Sensei Joshua'},{'Nathan Wong':'Sensei Joshua'},{'ethan duggal':'Sensei Jacky'},{'William leung':'Sensei Jacky'},{'Vithunan Murugathas':'Sensei Jacky'},{'Noah Zhai':'Sensei Jacky'},{'Brendan Chan':'Sensei Philip'},{'Damon Mai':'Sensei Philip'},{'Mithunan Murugathas':'Sensei Philip'},{'Leila Shahin':'Sensei Philip'},{'Natasha Chan':'Sensei Kevin'},{'Alyona Lee':'Sensei Kevin'},{'Megan Poon':'Sensei Kevin'},{'Dhylan Singam':'Sensei Kevin'},{'Jayden Wong':'Sensei Kevin'},{'Trevor Hoffmann':'Sensei Ernest'},{'Wyatt Jiang':'Sensei Ernest'},{'Jordan Kwan':'Sensei Ernest'},{'Kynton Lam':'Sensei Ernest'},{'hannah lin':'Sensei Ernest'},{'Catherine Cargason':'Sensei George'},{'Jeremy Cheung':'Sensei George'},{'Avery Tam':'Sensei George'},{'Connor Tsang':'Sensei George'},{'Henry Utomo':'Sensei George'},{'Cody Chau':'Sensei Juan'},{'Ethan Chu':'Sensei Juan'},{'Yashveer VSK Mummidi':'Sensei Juan'},{'Jayden Poon':'Sensei Juan'},{'Steve Jeyapal':'BEGINNER'},{'Nathanael Wan':'BEGINNER'},{'Kayleigh Wong':'BEGINNER'},{'Weston Wong':'BEGINNER'},],
    '11:00 AM':[{'Oliver Chan':'Sensei Michael'},{'Rexanna Fung':'Sensei Michael'},{'Carsten Li':'Sensei Michael'},{'Chelsea Luk':'Sensei Michael'},{'Summer Wong':'Sensei Michael'},{'Ellanie Logalakshan':'Sensei Joshua'},{'Theodore Luk':'Sensei Joshua'},{'Vannes Sum':'Sensei Joshua'},{'Nathan Wong':'Sensei Joshua'},{'ethan duggal':'Sensei Jacky'},{'William leung':'Sensei Jacky'},{'Cameron Wong':'Sensei Jacky'},{'Noah Zhai':'Sensei Jacky'},{'Brendan Chan':'Sensei Philip'},{'Braydon Ma':'Sensei Philip'},{'Damon Mai':'Sensei Philip'},{'Annabella Persaud':'Sensei Philip'},{'Leila Shahin':'Sensei Philip'},{'Natasha Chan':'Sensei Kevin'},{'Brayden Choi':'Sensei Kevin'},{'Alyona Lee':'Sensei Kevin'},{'Megan Poon':'Sensei Kevin'},{'Jayden Wong':'Sensei Kevin'},{'Michael Lawrence':'Sensei Ernest'},{'Lucas Zhong':'Sensei Ernest'},{'Catherine Cargason':'Sensei George'},{'Jeremy Cheung':'Sensei George'},{'Robert Rada':'Sensei George'},{'Avery Tam':'Sensei George'},{'Henry Utomo':'Sensei George'},{'Ethan Chu':'Sensei Juan'},{'Yashveer VSK Mummidi':'Sensei Juan'},{'Jayden Poon':'Sensei Juan'},{'Xiaoyang Samuel Shi':'Sensei Juan'},{'Lucas Li':'BEGINNER'},{'Bella Li':'BEGINNER'},{'darren wu':'BEGINNER'},{'stephanie yin':'BEGINNER'},],
    '12:00 PM':[{'vito kin Lam':'Sensei Michael'},{'Chelsea Luk':'Sensei Michael'},{'Connor Wu':'Sensei Michael'},{'Brayden Chiu':'Sensei Joshua'},{'Kaden Junior':'Sensei Joshua'},{'Theodore Luk':'Sensei Joshua'},{'Charlie Luong':'Sensei Joshua'},{'Sabastian Baptiste':'Sensei Jacky'},{'Leo Zheng':'Sensei Jacky'},{'Brayden Choi':'Sensei Philip'},{'Braydon Ma':'Sensei Philip'},{'Sormeh Mojabi':'Sensei Philip'},{'Jayden Ngai':'Sensei Philip'},{'Annabella Persaud':'Sensei Philip'},{'Michael Lawrence':'Sensei Ernest'},{'Aidan Yu':'Sensei Ernest'},{'Lucas Zhong':'Sensei Ernest'},{'Robert Rada':'Sensei George'},{'Stella Shen':'Sensei Juan'},{'Xiaoyang Samuel Shi':'Sensei Juan'},{'Killian Choi':'BEGINNER'},{'Aarnna Sudahar':'BEGINNER'},],
    '1:00 PM':[{'Titomi Adebayo':'Sensei Michael'},{'Bayley Nguyen':'Sensei Michael'},{'Connor Wu':'Sensei Michael'},{'Sabastian Baptiste':'Sensei Jacky'},{'Leo Zheng':'Sensei Jacky'},{'Sormeh Mojabi':'Sensei Philip'},{'Jayden Ngai':'Sensei Philip'},{'Sullivan Gray':'Sensei Kevin'},{'Ryan Joshy':'Sensei Kevin'},{'Cayden Yip':'Sensei Kevin'},{'Camden Kwan':'Sensei Ernest'},{'Tytus Brayden Leung':'Sensei Ernest'},{'Aidan Yu':'Sensei Ernest'},{'Aaron Zhou':'Sensei Ernest'},{'Eugene CHIANG':'Sensei George'},{'Owen Chen':'Sensei Juan'},{'Charmaine CHIANG':'Sensei Juan'},{'Alexander Fomenko':'Sensei Juan'},{'Stella Shen':'Sensei Juan'},{'Giselle Chen':'INTERMEDIATE'},{'Katniss Li':'INTERMEDIATE'},{'Makayla Ngai':'INTERMEDIATE'},{'Aiden Wan':'INTERMEDIATE'},{'Liam Zheng':'INTERMEDIATE'},],
    '2:00 PM':[{'Titomi Adebayo':'Sensei Michael'},{'Bryan Huang':'Sensei Michael'},{'Bayley Nguyen':'Sensei Michael'},{'Jacob Tseng':'Sensei Michael'},{'Alison Wong':'Sensei Michael'},{'Darren So':'Sensei Philip'},{'Livvy Zhang':'Sensei Philip'},{'Charlotte Won':'Sensei Kevin'},{'Marco Yan':'Sensei Kevin'},{'Cayden Yip':'Sensei Kevin'},{'Teagan Hum':'Sensei Ernest'},{'Brandon Lin':'Sensei Ernest'},{'Aaron Zhou':'Sensei Ernest'},{'Eugene CHIANG':'Sensei George'},{'Bernice Huang':'Sensei George'},{'Sebastien LaLonde':'Sensei George'},{'Kingsley Yue':'Sensei George'},{'Randy Zhang':'Sensei George'},{'Owen Chen':'Sensei Juan'},{'Charmaine CHIANG':'Sensei Juan'},{'Alexander Fomenko':'Sensei Juan'},{'Brianna Tsang':'Sensei Juan'},{'Vic Wong':'Sensei Juan'},],
    '3:00 PM':[{'Bryan Huang':'Sensei Michael'},{'Hayden Ngo':'Sensei Michael'},{'Jacob Tseng':'Sensei Michael'},{'Alison Wong':'Sensei Michael'},{'Shawn Gong':'Sensei Philip'},{'Darren So':'Sensei Philip'},{'Livvy Zhang':'Sensei Philip'},{'AYAZ Vural':'Sensei Kevin'},{'Marco Yan':'Sensei Kevin'},{'Timothy Goncharov':'Sensei Ernest'},{'Teagan Hum':'Sensei Ernest'},{'Brandon Lin':'Sensei Ernest'},{'Bernice Huang':'Sensei George'},{'Sebastien LaLonde':'Sensei George'},{'Kingsley Yue':'Sensei George'},{'Randy Zhang':'Sensei George'},{'Brianna Tsang':'Sensei Juan'},{'Vic Wong':'Sensei Juan'},],
}

# Paste in the student array

times = {
    8: "8:00 AM",
    9: "9:00 AM",
    10: "10:00 AM",
    11: "11:00 AM",
    12: "12:00 PM",
    1: "1:00 PM",
    2: "2:00 PM",
    3: "3:00 PM",
    4: "4:00 PM",
    5: "5:00 PM",
    6: "6:00 PM",
    7: "7:00 PM"
}

for key in scheduledTimes:
    # Sort the list of students for each scheduled time
    scheduledTimes[key].sort(key=lambda x: list(x.keys())[0])
    
json_data = json.dumps(scheduledTimes, indent=2)  # 'indent' for pretty formatting

print("Updated schedule")

# copy the previous content from the file to backup.txt
with open("schedule.txt", "r") as file:
    backup = file.read()
    file.close()

with open("backup.txt", "w") as file:
    file.write(backup)
    file.close()

# Write JSON string to a file
with open("schedule.txt", "w") as file:
    file.write(json_data)
    file.close()
    