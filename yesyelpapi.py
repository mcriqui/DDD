from yelpapi import YelpAPI
from pprint import pprint

yelp_api = YelpAPI('V4oXt-CDFMUXzPerVYXWnA', 'omnmWvy6KQNOSt1o9qD0YwMtKiQ', '_WuvOb1mMpmTdhuh9LwvyY_RQzsiLt3B', 'yAbsrRApeXzSIO_KK1dbDzbw0oA')

# response = yelp_api.business_query(id='oohhs-and-aahhs-washington')
# pprint(response)

# print response['rating']

# response = yelp_api.business_query(id='mac-and-ernies-roadside-eatery-tarpley')
# response = yelp_api.business_query(id="brints-diner-wichita")
try:
    response = yelp_api.business_query(id="pizza-palace-knoxville")
    print response['rating']
except KeyError:
    print "Key Error"

