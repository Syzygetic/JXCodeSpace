import datetime
import csv

from numpy import number


def getDateRange():
    # get some date
    dateArray = []
    for i in range(1, 1825):
        factor = i
        x = (datetime.datetime.now() -
             datetime.timedelta(days=factor)).strftime('%Y-%m-%d')
        dateArray.append(x)
    return dateArray


def saveToFile(objectArray, fileName):
    songList = []

    for song in objectArray:
        songDict = {}
        songDict['chartSource'] = song.chartSource
        songDict['songRank'] = song.songRank
        songDict['songName'] = song.songName
        songDict['songArtist'] = song.songArtist
        songDict['songStreams'] = song.songStreams
        songList.append(songDict)

    with open(f'./exports/{fileName}.csv', 'w', encoding='utf-8') as csvFile:
        writer = csv.DictWriter(
            csvFile, ['chartSource', 'songRank', 'songName', 'songArtist', 'songStreams'])
        writer.writeheader()
        for item in songList:
            writer.writerow(item)


def getMyDate(numberWeeks, dateRange):
    index = 0
    dateArray = []
    while index < numberWeeks:
        dateArray.append(dateRange[numberWeeks*index])
        index += 1
    return dateArray
