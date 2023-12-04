from pyucwa import PyUCWA

# Create a new instance of PyUCWA
client = PyUCWA('tabrizi@kahkeshan.net', 'ardin@kahkeshan.net', 'your_domain')  # replace with your credentials and domain

# Authenticate and establish a session
client.authenticate()

# Send a message to a contact
client.message('contact_email', 'Your message here')  # replace with the recipient's email and your message