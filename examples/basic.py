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

with open('credentials.json', 'r') as f:
    credentials = json.load(f)

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
    linkedin.print_out_conversations()
    # results = linkedin.search({'keywords': 'machine learning'}, 200)
    # print(len(results), "results found")
    # for element in results[:100]:
    #     profile = element["hitInfo"]["com.linkedin.voyager.search.SearchProfile"]["miniProfile"]
    #     message = "Hi " + profile["firstName"] + ", I am recruiting for Google, Pinterest, Uber, and a few other pre-IPO companies, with a special focus on machine learning positions. I have a few great opportunities and hope to connect so we can talk more!"
    #
    #     time.sleep(random.randint(20,60))
    #     linkedin.connect_with_someone( profile["publicIdentifier"],message)
    #     # print(profile["firstName"], profile["lastName"],)
    #     print("request for", profile["firstName"],profile["lastName"], "sent, message", message)
    # with open('result_search.json', 'w') as fp:
    #     json.dump(results, fp)
    # print(results)

