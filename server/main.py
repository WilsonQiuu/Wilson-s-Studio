from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from colorama import Fore, Style
from dotenv import load_dotenv
import os
import json

load_dotenv()


while True:
    scheduledTimes = {}

    # Initialize the Chrome driver
    driver = webdriver.Chrome()

    # Navigate to the login page
    driver.get('https://cn.mystudio.io/attendance/#/classesprogram')

    # Wait for the email input field to be present
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="login"]/div/input[1]'))
    )

    # Find the password input field
    password_input = driver.find_element(By.XPATH, '//*[@id="login"]/div/input[2]')


    email = os.environ.get("EMAIL")
    password = os.environ.get("PASSWORD")
    # Type the email and password into the input fields
    email_input.send_keys(email)
    password_input.send_keys(password)

    # Find and click the login button (replace 'xpath-to-login-button' with the actual XPath)
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="login"]/div/button'))
    )
    login_button.click()

    time.sleep(2)

    num_hours = 6
    num_sensei = 11
    # num_hours*num_sensei
    for participant_id in range(0, num_hours*num_sensei):
        try:
            time.sleep(1)
            xpath_participant = f'//*[@id="participant_{participant_id}"]/p[1]'
            
            
            # Find the element corresponding to participant_0
            participant_element = driver.find_element(By.XPATH, xpath_participant)
            
            senseiName = participant_element.text
            
            # Click on the participant_0 element
            participant_element.click()
            
            # Add a delay to allow time for the action to be visible (adjust this as needed)
            time.sleep(1)
            
            SessionTime = driver.find_element(By.XPATH, '//*[@id="nav-bar-content"]/nav[5]/p[2]')
            
            # Store student names in a list
            student_names = []

            # Loop through the alphabet and indices to extract student names
            for char in range(ord('A'), ord('Z')+1):  # Loop through characters 'A' to 'Z'
                for idx in range(5):  # Assuming a maximum of 5 students per alphabet
                    try:
                        # Construct the XPath dynamically for each student name element
                        xpath = f'//*[@id="participant_name_{chr(char)}{idx}"]'
                        
                        # Find the student name element using the constructed XPath
                        student_name_element = driver.find_element(By.XPATH, xpath)
                        
                        # Extract the text containing the student's name
                        student_name = student_name_element.text
                        
                        # Append the student's name to the list
                        student_names.append(student_name)
                        
                    except Exception as e:
                        # If no more elements found, break the inner loop
                        break
            # Print all the collected student names
            print(SessionTime.text.split(" ")[0] + " " + SessionTime.text.split(" ")[1])
            print("Sensei Name:" + senseiName)
            print("Student Names:")
            print(student_names)
            scheduledTime = SessionTime.text.split(" ")[0] + " " + SessionTime.text.split(" ")[1]
            
            if len(senseiName.split(" ")) > 2: 
                senseiName =  senseiName.split(" ")[0] + " " + senseiName.split(" ")[1]
            else:
                senseiName = senseiName.split(" ")[0]
            
            # Initialize an empty list if scheduledTime key doesn't exist
            if scheduledTime not in scheduledTimes:
                scheduledTimes[scheduledTime] = []

            for student in student_names:
                pair = {student: senseiName}
                scheduledTimes[scheduledTime].append(pair)
                
                
            back_button = driver.find_element(By.XPATH, '//*[@id="nav-bar-content"]/nav[5]/p[1]/img')
                
            back_button.click()
            
                
            
        except Exception as e:
            print(f"")


    # Close the browser when done
    driver.quit()



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
    
    print("Updated schedule")
    print("Time is: " + time.strftime("%H:%M:%S", time.localtime()))

    time.sleep(60*60*1) # Every half hour hours






  