from yelpapi import YelpAPI
from pprint import pprint

yelp_api = YelpAPI('V4oXt-CDFMUXzPerVYXWnA', 'omnmWvy6KQNOSt1o9qD0YwMtKiQ', '_WuvOb1mMpmTdhuh9LwvyY_RQzsiLt3B', 'yAbsrRApeXzSIO_KK1dbDzbw0oA')

with open('test.csv', 'r') as original_file:
    episodes = original_file.read().split('\n')
    season_one_dictionary = {}
    for index, line in enumerate(episodes):
        episode_items = line.split(',')
        individual_episode = {}

        #gets the individual episode number
        individual_episode['episode'] = episode_items[0]

        #gets and cleans the title of the episode
        episode_items[1] = episode_items[1].replace('*', '')
        individual_episode['title'] = episode_items[1]

        #gets the restaurant info and puts it in format compatable for yelp api business id
        episode_items[2] = episode_items[2].replace(' ', '-').replace('&', 'and').replace("'", '').replace('\xc3', 'e').replace('\xa9', '')
        individual_episode['restaurant'] = episode_items[2]

        #gets and cleans city name
        episode_items[3] = episode_items[3].replace('"', '').replace(' ', '-').replace('St.', 'saint-')
        individual_episode['city'] = episode_items[3]

        #gets anc cleans the state
        episode_items[4] = episode_items[4].replace('"', '').strip(' ')
        individual_episode['state'] = episode_items[4]

        #gets the date
        individual_episode['date'] = episode_items[5]

        #creates business id key
        business_id = "{0}-{1}".format(episode_items[2], episode_items[3])
        individual_episode['id'] = business_id


        season_one_dictionary[index] = individual_episode

    for dictionary in season_one_dictionary:
        print dictionary.key()

    # business_id = season_one_dictionary[0]['id']
    # response = yelp_api.business_query(id=business_id)
    # print response['rating']




