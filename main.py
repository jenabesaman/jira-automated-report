# import csv
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# # Set up the web driver
# driver = webdriver.Chrome()
#
# # Navigate to the login page
# driver.get("http://172.16.40.178:8080/login.jsp")
#
# # Enter your credentials and log in
# # find_element(By.NAME, ‘name’)
# username = driver.find_element(By.NAME,"os_username")
# # username = driver.find_element_by_name("os_username")
#
# # password = driver.find_element_by_name("os_password")
# password = driver.find_element(By.NAME,"os_password")
# username.send_keys("jirauser")
# password.send_keys("Kahkeshan@123456")
# # driver.find_element_by_name("login").click()
# driver.find_element(By.NAME,"login").click()
#
# # Navigate to the page with the CSV file
# driver.get("http://172.16.40.178:8080/sr/jira.issueviews:searchrequest-csv-all-fields/10635/SearchRequest-10635.csv")
# time.sleep(5)

import os
import glob
import csv
from skpy import Skype

# Change directory to the Downloads folder
os.chdir(r'C:\Users\tabrizi\Downloads')

# Find the latest .csv file that starts with "Done issues"
latest_file = max(glob.glob('Done issues*.csv'), key=os.path.getctime)

# Extract the 'Summary' column from the .csv file
with open(latest_file, 'r') as f:
    reader = csv.DictReader(f)
    summary_column = [row['Summary'] for row in reader]

# Connect to Skype
skype = Skype("samanamman@gmail.com","Saboondaroogar@1100")

# Select the user
user = skype.contacts['MV Ardin']
if user is None:
    print('None')

# Send the message
message = '\n'.join(summary_column)
user.chat.sendMsg(message)





# import os
# import glob
# import csv
# from skpy import Skype
#
# # Change directory to the Downloads folder
# os.chdir(r'C:\Users\tabrizi\Downloads')
#
# # Find the latest .csv file that starts with "Done issues"
# latest_file = max(glob.glob('Done issues*.csv'), key=os.path.getctime)
#
# # Extract the 'Summary' column from the .csv file
# with open(latest_file, 'r') as f:
#     reader = csv.DictReader(f)
#     summary_column = [row['Summary'] for row in reader]
#
# # Connect to Skype
# skype = Skype('samanamman@gmail.com', '')
#
# # Select the user
# user = skype.contacts['MV Ardin']
#
# # Send the message
# message = '\n'.join(summary_column)
# # user.chat.sendMsg(message)



# Download the CSV file
# csv_file = driver.find_element(By.NAME,"body").text
# # csv_file = driver.find_element_by_tag_name("body").text
# with open("output.csv", "w") as f:
#     f.write(csv_file)
#
# with open("output.csv", "r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row["Summary"])
#
# # Close the web driver
# driver.quit()
