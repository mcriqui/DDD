# encoding: utf-8
import csv
import time
from yelpapi import YelpAPI

yelp_api = YelpAPI('V4oXt-CDFMUXzPerVYXWnA', 'omnmWvy6KQNOSt1o9qD0YwMtKiQ', '_WuvOb1mMpmTdhuh9LwvyY_RQzsiLt3B', 'yAbsrRApeXzSIO_KK1dbDzbw0oA')

episodes_numbers_list = []
titles_list = []
restaurants_list = []
cities_list = []
states_list = []
dates_list = []
business_ids_list = []
rating_list = []
rating_business_id_list = []

with open('master_list.csv', 'r') as original_file:
    episodes = original_file.read().split('\n')
    for index, episode in enumerate(episodes):
        episodes[index] = episodes[index].split(',')
        episodes_numbers_list.append(episodes[index][0])
        titles_list.append(episodes[index][1].replace('*', '').replace("'", ''))
        restaurants_list.append(episodes[index][2].replace("'", "").replace('&', 'and').replace('\xc3', 'e').replace('\xa9', ''))
        cities_list.append(episodes[index][3].replace('"', '').replace('St.', 'Saint'))
        states_list.append(episodes[index][4].replace('"', '').strip(' '))
        # dates_list.append(episodes[index][5])replace('\xe2\x80\x99', "")

for restaurant, city in zip(restaurants_list, cities_list):
    business_id = "{0}-{1}".format(restaurant.replace(' ', '-'), city.replace(' ', '-'))
    business_ids_list.append(business_id)

for biz_id in business_ids_list:
    response = yelp_api.business_query(id=biz_id)
    if 'error' in response.keys():
        rating_business_id_list.append(biz_id)
        rating_list.append('KeyError')
        print "{0} Key Error".format(biz_id)
    elif 'is_claimed' in response.keys():
        rating_business_id_list.append(biz_id)
        rating_list.append(response['rating'])
        print biz_id, response['rating']
    else:
        print "huh?"
    time.sleep(.5)


clean_file = open('new_clean_master_with_rating.csv', 'w')
writer = csv.writer(clean_file)
for episode_number, title, restaurant, city, state, business_id, rating, rating_business_id in zip(episodes_numbers_list, titles_list, restaurants_list, cities_list, states_list, business_ids_list, rating_list, rating_business_id_list):
    writer.writerow((episode_number, title, restaurant, city, state, business_id, rating, rating_business_id))
clean_file.close()
