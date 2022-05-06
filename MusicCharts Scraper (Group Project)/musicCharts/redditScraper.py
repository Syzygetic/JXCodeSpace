from bs4 import BeautifulSoup
import requests
import csv
from collections import defaultdict
import pandas
import time
from datetime import datetime
from BaseScraperClass import BaseScraper
import unittest


class TestUserInputMethod(unittest.TestCase):
    def test_isString(self):
        inputFileType = type(inputFile)
        inputPeriodType = type(scrapePeriod)
        expectedStringType = str
        self.assertEqual(inputFileType, expectedStringType)
        self.assertEqual(inputPeriodType, expectedStringType)

    def test_isInt(self):
        inputSizeType = type(inputSize)
        expectedIntType = int
        self.assertEqual(inputSizeType, expectedIntType)

    def test_isDateTime(self):
        inputStartDateType = type(startSearchDate)
        inputEndDateType = type(endSearchDate)
        expectedDateTimeType = datetime
        self.assertEqual(inputStartDateType, expectedDateTimeType)
        self.assertEqual(inputEndDateType, expectedDateTimeType)


class RedditScraper(BaseScraper):
    def __init__(self, url):
        super().__init__(url)

    def get_HTML_data(self):
        req = requests.get(self.url, headers=self.headers)
        response = BeautifulSoup(req.text, 'html.parser')
        return response


def getRedditData(inputFile, inputSize, scrapePeriod, startSearchDate, endSearchDate):
    # Main Function of the whole program that passes in input data according to user's choice
    # and calls the sub function scrapeReddit()
    with open(f'./exports/{inputFile}', 'rt', encoding='utf-8', newline='') as src:
        reader = csv.reader(src)
        for row in reader:
            for (i, v) in enumerate(row):
                columns[i].append(v)

        for items in columns[2]:
            if items == 'songName':
                continue
            else:
                searchTitle = "%s" % (items.replace(
                    ' ', '+').replace(',', '%2C').replace('(', '%28').replace(')', '%29'))
                searchTitleList.append(searchTitle)
        print(searchTitleList)

        for items in columns[3]:
            if items == 'songArtist':
                continue
            else:
                searchArtist = "%s" % (items.replace(
                    ' ', '+').replace(',', '%2C').replace('(', '%28').replace(')', '%29'))
                searchArtistList.append(searchArtist)
        print(searchArtist)

        scrapeReddit(inputSize, scrapePeriod, startSearchDate, endSearchDate)


def scrapeReddit(inputSize, scrapePeriod, startSearchDate, endSearchDate):
    counter = 1

    # Function uses input data to search Reddit and scrape Reddit, then after storing the scraped data into a CSV file
    for i in range(inputSize):
        searchSong = searchTitleList[i] + "+" + searchArtistList[i]

        if scrapePeriod == 'Day':
            songUrl = 'https://old.reddit.com/search?q=' + \
                searchSong + '&include_over_18=on&t=day&sort=relevance'
        elif scrapePeriod == 'Week':
            songUrl = 'https://old.reddit.com/search?q=' + \
                searchSong + '&include_over_18=on&t=week&sort=relevance'
        elif scrapePeriod == 'Month':
            songUrl = 'https://old.reddit.com/search?q=' + \
                searchSong + '&include_over_18=on&t=month&sort=relevance'
        else:
            songUrl = 'https://old.reddit.com/search?q=' + \
                searchSong + '&include_over_18=on&t=year&sort=relevance'

        # documentation: Using imported BaseScraper Class to set URL to scrape,
        # include headers to access websites as a user, request from URL and to get response from URL
        redditScraper = RedditScraper(songUrl)
        songSoup = redditScraper.get_HTML_data()

        songPostCounter = 0
        totalSongPostLikes = 0
        totalSongPostComments = 0
        songPostTitles = ""

        nextButtonExist = True
        while nextButtonExist is True:
            allSongPostList = songSoup.find_all('div', class_='contents')

            if len(allSongPostList) == 2:
                for post in allSongPostList[1]:
                    print(post)
                    postDateTime = post.time['datetime'].replace(
                        "T", " ").replace("+00:00", "")
                    postDateTime = datetime.strptime(
                        postDateTime, '%Y-%m-%d %H:%M:%S')
                    if startSearchDate <= postDateTime <= endSearchDate:
                        likes = post.find('span', class_='search-score')
                        if likes is not None:
                            likes = likes.text.split()[0]
                            likes = likes.replace(",", "")
                        elif likes == "•" or likes is None:
                            likes = 0
                        print(likes)
                        totalSongPostLikes += int(likes)

                        comments = post.find(
                            'a', class_='search-comments may-blank')
                        if comments is not None:
                            comments = comments.text.split()[0]
                            comments = comments.replace(",", "")
                        elif comments == "comment" or comments is None:
                            comments = 0
                        print(comments)
                        totalSongPostComments += int(comments)

                        if songPostCounter < 10:
                            postTitle = post.find(
                                'a', class_='search-title may-blank')
                            songPostTitles += postTitle.text + "\r\n"
                        songPostCounter += 1
                    else:
                        continue

            elif len(allSongPostList) == 1:
                for post in allSongPostList[0]:
                    print(post)
                    postDateTime = post.time['datetime'].replace(
                        "T", " ").replace("+00:00", "")
                    postDateTime = datetime.strptime(
                        postDateTime, '%Y-%m-%d %H:%M:%S')
                    if startSearchDate <= postDateTime <= endSearchDate:
                        likes = post.find('span', class_='search-score')
                        if likes is not None:
                            likes = likes.text.split()[0]
                            likes = likes.replace(",", "")
                        elif likes == "•" or likes is None:
                            likes = 0
                        print(likes)
                        totalSongPostLikes += int(likes)

                        comments = post.find(
                            'a', class_='search-comments may-blank')
                        if comments is not None:
                            comments = comments.text.split()[0]
                            comments = comments.replace(",", "")
                        elif comments == "comment" or comments is None:
                            comments = 0
                        print(comments)
                        totalSongPostComments += int(comments)

                        if songPostCounter < 10:
                            postTitle = post.find(
                                'a', class_='search-title may-blank')
                            songPostTitles += postTitle.text + "\r\n"
                            #print("HELLO" + songPostTitles)
                        songPostCounter += 1
                    else:
                        continue

            resultTypes = songSoup.find_all(
                'div', class_='listing search-result-listing')
            if len(resultTypes) == 2:
                nextButton = resultTypes[1].findAll(
                    'a', {'rel': 'nofollow next'})
            else:
                nextButton = resultTypes[0].findAll(
                    'a', {'rel': 'nofollow next'})
            if len(nextButton) == 1:
                for result in nextButton:
                    nextPageLink = result.attrs['href']
                    redditScraper.url = nextPageLink
                    songSoup = redditScraper.get_HTML_data()
            else:
                nextButtonExist = False

            time.sleep(2)

        backSong = searchSong.replace(
            '+', ' ').replace('%2C', ',').replace('%28', '(').replace('%29', ')')
        songName = backSong
        songPosts = songPostCounter
        songLikes = totalSongPostLikes
        songComments = totalSongPostComments
        songTitles = songPostTitles

        trackLine = [counter, songName, songPosts,
                     songLikes, songComments, songTitles]

        with open('redditComments_' + inputFile, 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(trackLine)

        counter += 1

    df = pandas.read_csv('redditComments_' + inputFile, header=None)
    df.to_csv('redditComments_' + inputFile, header=["songRank", "songName", "songPosts", "songLikes",
                                                     "songComments", "songSampleTitles"], index=False)


# Main() body of the program
continueScrape = True

while continueScrape == True:
    searchTitleList = []
    searchArtistList = []

    inputFile = ''
    dataSelected = False
    while dataSelected == False:
        dataSelect = int(input(
            "1) Spotify.csv\n2) Billboard.csv\nPlease enter index of data to scrape Reddit with: "))
        if dataSelect == 1:
            inputFile = 'Spotify.csv'
            dataSelected = True
        elif dataSelect == 2:
            inputFile = 'Billboard.csv'
            dataSelected = True

    inputSize = -1
    inpSizeEntered = False
    while inpSizeEntered == False:
        inputSize = int(
            input("\nNumber of Songs to use as input to search and scrape Reddit: "))
        if inputSize > 0:
            inpSizeEntered = True

    scrapePeriod = ''
    endSearchDate = datetime.now()
    startSearchDate = datetime.min
    scrapeDateSelected = False
    while scrapeDateSelected == False:
        scrapeDate = int(input("\nScrape Reddit data within\n1) Past 24 Hours\n2) Past Week"
                               "\n3) Past Month\n4) Past Year\n5) Self-specified Period (within the period of past 1 year)"
                               "\nPlease enter index of the time period to scrape Reddit with: "))
        if scrapeDate == 1:
            scrapePeriod = 'Day'
            scrapeDateSelected = True
        elif scrapeDate == 2:
            scrapePeriod = 'Week'
            scrapeDateSelected = True
        elif scrapeDate == 3:
            scrapePeriod = 'Month'
            scrapeDateSelected = True
        elif scrapeDate == 4:
            scrapePeriod = 'Year'
            scrapeDateSelected = True
        elif scrapeDate == 5:
            scrapePeriod = 'Specific'
            scrapeSpecificStart = input(
                "Please enter the Start Date, in the format (DD/MM/YYYY): ")
            startSearchDate = datetime.strptime(
                scrapeSpecificStart, '%d/%m/%Y')
            scrapeSpecificEnd = input(
                "Please enter the End Date, in the format (DD/MM/YYYY)): ")
            endSearchDate = datetime.strptime(scrapeSpecificEnd, '%d/%m/%Y')
            scrapeDateSelected = True

    columns = defaultdict(list)
    getRedditData(inputFile, inputSize, scrapePeriod,
                  startSearchDate, endSearchDate)

    continueMsg = ''
    continueDetermined = False
    while continueDetermined == False:
        continueMsg = input(
            "\n\n\nContinue Scraping? Enter Y for Yes, and N for No. ")
        if continueMsg == 'N':
            continueScrape = False
            continueDetermined = True
        elif continueMsg == 'Y':
            continueDetermined = True

unittest.main()