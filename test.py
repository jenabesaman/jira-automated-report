# from collections import defaultdict
# grouped_data = defaultdict(list)
# with open(latest_file, 'r') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         grouped_data[row['Creator']].append(row['Summary'])
# result_list = []
# for creator, summaries in grouped_data.items():
#     # Append the creator to the result list
#     result_list.append(creator)
#     # Extend the result list with the summaries
#     result_list.extend(summaries)
#
# # Print the result list
# print(result_list)


from skpy import Skype
skype = Skype("samanamman@gmail.com", "Saboondaroogar@1100")



# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# # Set up the SMTP server and login credentials
# smtp_server = 'smtp.office365.com'
# smtp_port = 587
# username = 'tabrizi@kahkeshan.ir'
# password = 'SaTa@123#'
#
# # Create the message
# msg = MIMEMultipart()
# msg['From'] = username
# msg['To'] = 'tabrizi@kahkeshan.ir'
# msg['Subject'] = 'Subject of the email'
#
# # Add the email body
# body = 'This is the body of the email.'
# msg.attach(MIMEText(body, 'plain'))
#
# # Send the email
# server = smtplib.SMTP(smtp_server, smtp_port)
# server.starttls()  # Secure the connection
# server.login(username, password)  # Login to the server
# server.sendmail(msg['From'], msg['To'], msg.as_string())  # Send the email
# server.quit()  # Logout of the server
