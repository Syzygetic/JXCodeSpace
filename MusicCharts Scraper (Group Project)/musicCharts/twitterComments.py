import tweepy
import json
import requests
import csv

# Authentication information
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth, wait_on_rate_limit=True)

# print(tweepy.API.rate_limit_status())


def twitterComments(file):
    filename = f'./exports/{file}.csv'

    song = []
    songs = []
    with open(filename, newline='', encoding='utf-8') as r:
        data = csv.DictReader(r)
        for row in data:
            dict2 = {}
            dict2['songRank'] = row['songRank']
            dict2['songName'] = row['songName']
            dict2['songArtist'] = row['songArtist']
            song.append(dict2)

    for i in song[:10]:
        comments = []
        # print(song[0])
        query = i['songName']
        count = 10
        results = tweepy.Cursor(api.search, q=query).items(count)
        list = [[tweet.text] for tweet in results]
        dict = {}
        dict['songRank'] = i['songRank']
        dict['songName'] = i['songName']

        for k in list:
            # print(k)
            comments.append(k[0])
        dict['songComment'] = '\n'.join(comments)
        songs.append(dict)

    with open(f'./exports/twitterComments_{file}.csv', 'w', newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, ['songRank', 'songName', 'songComment'])
        writer.writeheader()
        for item in songs:
            print(item)
            writer.writerow(item)


twitterComments('spotify')
