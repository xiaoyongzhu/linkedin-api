
import sqlite3
import time
import random
import datetime
import json
from linkedin_api import Linkedin

#
# def print_out_all_conversations(linkedin):
#     all_id = linkedin.get_all_converstaion_public_id(linkedin)
#     for individual_id in all_id:
#         profile = linkedin.get_profile(individual_id)
#         profile_urn_id = profile['profile_id']
#         print("profile_urn_id", profile_urn_id)
#
#         conversation = linkedin.get_conversation_details(profile_urn_id)
#         conversation_id = conversation['id']
#
#         conversations = linkedin.get_message(conversation_id)
#         for individual_conversation in conversations['elements']:
#             # the response is a list and each item is an element in the list
#             conversation_time_stamp = int(individual_conversation['createdAt']/1000)
#             human_readable_time = datetime.datetime.fromtimestamp(conversation_time_stamp).strftime('%c')
#             text = individual_conversation['eventContent']["com.linkedin.voyager.messaging.event.MessageEvent"]['body']
#             from_people_firstname = individual_conversation['from']["com.linkedin.voyager.messaging.MessagingMember"]['miniProfile']['firstName']
#             from_people_lastname = individual_conversation['from']["com.linkedin.voyager.messaging.MessagingMember"]['miniProfile']['lastName']
#
#             print(human_readable_time, from_people_firstname +" " + from_people_lastname, "says:", text)

with open('credentials_test.json', 'r') as f:
    credentials = json.load(f)

def init():
    conn = sqlite3.connect('connections.db')
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE connections
                 (GUID varchar(255), invitation_sent bool, invitation_accepted bool, jd_sent bool, deeper_discussion bool)''')

    # Insert a row of data
    c.execute("INSERT INTO connections VALUES ('xiaoyzhu','T','T','T', 'T')")

    # Save (commit) the changes
    conn.commit()


    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()

# init()
conn = sqlite3.connect('connections.db')
c = conn.cursor()
for row in c.execute('SELECT * FROM connections ORDER BY GUID'):
    print(row)

#I want to introduce a great opportunity with Foxconn in Milwaukee. Now they are hiring great talents in IOT to join them. Please connect to discuss further. Thanks!
if credentials:
    linkedin = Linkedin(credentials['username'], credentials['password'])

    # linkedin.print_out_conversations()
    # results = linkedin.search_people(
    #     keywords='machine learning',
    #     connection_of='AC679287721',
    #     network_depth='S',
    #     regions=["seattle"],
    #     # industries=[29, 1]
    # )
    # linkedin.print_out_conversations()
    results = linkedin.search({'keywords': 'iot Milwaukee'}, 200)

    # print(len(results), "results found")
    # for element in results[:100]:
    #     profile = element["hitInfo"]["com.linkedin.voyager.search.SearchProfile"]["miniProfile"]
    #     message = "Hi " + profile["firstName"] + ", I am recruiting for Google, Pinterest, Uber, and a few other pre-IPO companies, with a special focus on machine learning positions. I have a few great opportunities and hope to connect so we can talk more!"
    #
    #     time.sleep(random.randint(20,60))
    #     linkedin.connect_with_someone( profile["publicIdentifier"],message)
    #     # print(profile["firstName"], profile["lastName"],)
    #     print("request for", profile["firstName"],profile["lastName"], "sent, message", message)
    with open('search_iot_Milwaukee.json', 'w') as fp:
        json.dump(results, fp)
    print(results)

