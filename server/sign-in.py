from flask import Flask, request, jsonify
from queue import Queue
import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from flask_cors import CORS




app = Flask(__name__)
CORS(app)
request_queue = Queue()
lock = threading.Lock()

def login(email, password):
    driver = webdriver.Chrome()
    try:
        # Navigate to the login page
        driver.get('https://cn.mystudio.io/attendance/#/classesprogram')

        # Wait for the email input field to be present
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login"]/div/input[1]'))
        )

        # Find the password input field
        password_input = driver.find_element(By.XPATH, '//*[@id="login"]/div/input[2]')

        # Type the email and password into the input fields
        email_input.send_keys(email)
        password_input.send_keys(password)

        # Find and click the login button
        login_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="login"]/div/button'))
        )
        login_button.click()

        # Wait for the page to load after login
        time.sleep(2)
        

    except Exception as e:
        print(f"Error during login: {e}")

    return driver
    pass


def process_request(data):
    # Extracting necessary data from the request
    name = data.get('name')
    time_value = data.get('time')
    sensei_value = data.get('sensei')
    
    email = os.environ.get("EMAIL")
    password = os.environ.get("PASSWORD")

    driver = login(email, password)
    time.sleep(2)
    
    num_hours = 6
    num_sensei = 11
    sensei_found = False
    
    try:

        for participant_id in range(0, num_hours*num_sensei):
            if(sensei_found):
                break
            try:
                xpath_participant = f'//*[@id="participant_{participant_id}"]/p[1]'
                
                
                # Find the element corresponding to participant_0
                participant_element = driver.find_element(By.XPATH, xpath_participant)
                
                senseiName = participant_element.text.split(" ")[0] + " " + participant_element.text.split(" ")[1]
                
                if(sensei_value == senseiName):
                    # Check to see if the first child of the parent element has text that matches the time_value
                        
                    try: 
                        time_element = participant_element.find_element(By.XPATH, '../../div[@class="timecol ng-binding"]')
  # Get the parent element
                        if(time_element.text == time_value):
                            sensei_found = True
                            
                            participant_element.click()
                            # Works
                            time.sleep(2)
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

                                        if(student_name == name):
                                            try:
                                                name_xpath = f"//span[text()='{student_name}']"

                                                # Wait for the name element to be present
                                                name_element = WebDriverWait(driver, 3).until(
                                                    EC.presence_of_element_located((By.XPATH, name_xpath))
                                                )

                                                # Construct the relative XPath for the button element
                                                button_xpath = f"{name_xpath}/ancestor::div[@class='card-cstm align-items-center']/descendant::button[@type='button' and text()='Check in']"

                                                # Wait for the button element to be clickable
                                                button_element = WebDriverWait(driver, 3).until(
                                                    EC.element_to_be_clickable((By.XPATH, button_xpath))
                                                )

                                                # Click the button
                                                button_element.click()
                                                print(f"Checked in {student_name}")
                                                
                                            except:
                                                # Construct the relative XPath for the button element
                                                button_xpath = f"{name_xpath}/ancestor::div[@class='card-cstm align-items-center']/descendant::button[@type='button' and contains(@class, 'cancel_checkin')]"

                                                # Check if the "Cancel check-in" button exists
                                                cancel_checkin_button_exists = driver.find_elements(By.XPATH, button_xpath)

                                                if cancel_checkin_button_exists:
                                                    print(f"Already Checked in: {student_name}")
                                                else:
                                                    print(f"Something went wrong Checking in {student_name}")
                                    except Exception as e:
                                        # If no more elements found, break the inner loop
                                        break
                            break
                    except:
                        print("Student not found")
            except Exception as e:
                print(f"And error: {e}")



    except Exception as e:
        print(f"Error during interaction: {e}")

    finally:
        # Close the WebDriver
        
        driver.quit()

    greeting = f"Hello {name}, it is {time_value}. Your sensei is {sensei_value}."

    return greeting

def worker():
    while True:
        data = request_queue.get()
        try:
            with lock:
                result = process_request(data)
                print(result)
        finally:
            request_queue.task_done()

@app.route('/greet', methods=['POST'])
def add_to_queue():
    data = request.get_json()

    if 'name' not in data or 'time' not in data or 'sensei' not in data:
        return jsonify({'error': 'Invalid request. Please provide name, time, and sensei.'}), 400

    request_queue.put(data)
    return jsonify({'message': 'Request added to the queue.'}), 200

if __name__ == '__main__':
    worker_thread = threading.Thread(target=worker)
    worker_thread.daemon = True
    worker_thread.start()
    app.run(debug=True, port=5000)



