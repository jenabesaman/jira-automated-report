from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
import glob
import csv
from skpy import Skype

# Set up the web driver
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("http://172.16.40.178:8080/login.jsp")

# Enter your credentials and log in
# find_element(By.NAME, ‘name’)
username = driver.find_element(By.NAME, "os_username")
# username = driver.find_element_by_name("os_username")

# password = driver.find_element_by_name("os_password")
password = driver.find_element(By.NAME, "os_password")
username.send_keys("jirauser")
password.send_keys("Kahkeshan@123")
# driver.find_element_by_name("login").click()
driver.find_element(By.NAME, "login").click()

# Navigate to the page with the CSV file
driver.get("http://172.16.40.178:8080/sr/jira.issueviews:searchrequest-csv-all-fields/10635/SearchRequest-10635.csv")
time.sleep(5)

# Change directory to the Downloads folder
os.chdir(r'C:\Users\tabrizi\Downloads')

# Find the latest .csv file that starts with "Done issues"
latest_file = max(glob.glob('Done issues*.csv'), key=os.path.getctime)
# summary_column = ''

# Extract the 'Summary' column from the .csv file
# with open(latest_file, 'r') as f:
#     reader = csv.DictReader(f)
#     # for row in reader:
#     #     summary_column += f"{row['Creator']} : {row['Summary']}\n"
#         # summary_column += row['Summary'] + ", " + row['Creator'] + "\n"
#     summary_column = [row['Summary'] for row in reader]
# with open(latest_file, 'r') as f1:
#     reader1 = csv.DictReader(f1)
#     creator_column = [row1['Creator'] for row1 in reader1]
# print(summary_column)
# print(creator_column)
#
# final_list=[]
# for item1 , item2 in zip(summary_column,creator_column):
#     final_list.append((item1,item2))


from collections import defaultdict
grouped_data = defaultdict(list)
with open(latest_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        grouped_data[row['Creator']].append(row['Summary'])
result_list = []
for creator, summaries in grouped_data.items():
    # Append the creator to the result list
    result_list.append(creator)
    # Extend the result list with the summaries
    result_list.extend(summaries)

# Print the result list
print(result_list)

# Connect to Skype
skype = Skype("samanamman@gmail.com", "Saboondaroogar@1100")
# Select the user
# contact_skype_id = "live:bd852ab72d1b0190"
contact_skype_id = "live:bd852ab72d1b0190"
contact = skype.contacts[contact_skype_id]

# Send the message
message = '\n'.join(result_list)
contact.chat.sendMsg(message)
