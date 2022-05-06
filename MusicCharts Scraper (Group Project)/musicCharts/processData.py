from csv import reader
from os import read
import matplotlib.pyplot as plot
import csv
from collections import Counter


def readCSVfile(filename):
    if filename == 'billboard':
        n = 100
    elif filename == 'spotify':
        n = 200
    fullChartList = []
    with open(f"./exports/{filename}.csv", "r", encoding="utf-8") as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        if header != None:
            for row in csv_reader:
                songDict = {}
                songDict['chartSource'] = row[0]
                songDict['songRank'] = int(row[1])
                songDict['songName'] = row[2]
                songDict['songArtist'] = row[3]
                songDict['songStreams'] = int(row[4])
                fullChartList.append(songDict)
    weeksChartList = [fullChartList[i:i + n]
                      for i in range(0, len(fullChartList), n)]
    return weeksChartList


def topArtistStats(type, count, generateImage=False):
    chartList = readCSVfile(type)[0]
    artistCount = []
    for song in chartList:
        artistCount.append(song['songArtist'])
    uniqueArtists = dict(Counter(artistCount))

    sortedUnique = {k: v for k, v in sorted(
        uniqueArtists.items(), key=lambda item: item[1])}

    # get last 5 items from the sortedUnique list
    if generateImage == True:
        plot.cla()
        plot.clf()
        plot.plot(list(sortedUnique.keys())
                  [-5:], list(sortedUnique.values())[-5:])
        plot.xlabel("Artist Name")
        plot.ylabel("Number of Top Songs")
        plot.savefig("./exports/images/topArtist" + type + ".png")


def topSongStats(type, count, generateImage=False):
    chartList = readCSVfile(type)[0]
    sortedSongs = sorted(
        chartList, key=lambda i: i['songStreams'], reverse=True)
    # print(sortedSongs[-10:])
    uniqueTopSongs = []
    for song in sortedSongs:
        if uniqueTopSongs:
            if not uniqueTopSongs[-1]['songName'] == song['songName']:
                uniqueTopSongs.append(song)
        else:
            uniqueTopSongs.append(song)
            # print(uniqueTopSongs[-1]['songName'])

    songs = []
    songsFreq = []
    for song in uniqueTopSongs[:count]:
        songs.append(song['songName'])
        songsFreq.append(song['songStreams'])

    if generateImage == True:
        plot.cla()
        plot.clf()
        plot.plot(songs, songsFreq)
        plot.xlabel("Song Name")
        plot.ylabel("Number of Streams")
        plot.savefig("./exports/images/topSong" + type + ".png")
    return uniqueTopSongs[:count]


def compareCharts():
    billboardChart = readCSVfile(1)
    spotifyChart = readCSVfile(2)
    mergedChartList = []
    for index, song in enumerate(range(0, 10)):
        mergedSong = {}
        mergedSong['rank'] = index + 1
        mergedSong['billboard'] = billboardChart[song]['songName']
        mergedSong['spotify'] = spotifyChart[song]['songName']
        mergedChartList.append(mergedSong)
        # print(mergedSong)
    return mergedChartList


def spotifySongFeq():
    songName = []
    songFeq = []
    artistName = []
    artistNameCount = []
    top = 0
    with open("exports/spotify.csv", "r", encoding="utf-8") as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        if header != None:
            for row in csv_reader:
                songName.append(row[2])
                artistName.append(row[3])
                top += 1
                if top == 101:
                    break
    for i in range(0, 100):
        countSong = 0
        countArtist = 0
        with open("exports/spotify.csv", "r", encoding="utf-8") as read_obj:
            csv_reader = reader(read_obj)
            header = next(csv_reader)
            if header != None:
                for row in csv_reader:
                    if songName[i] == row[2]:
                        countSong += int(row[4])
                    if artistName[i] == row[3]:
                        countArtist += 1
                songFeq.append(countSong)
                artistNameCount.append(countArtist)

    with open("exports/spotifyFeq.csv", "w", encoding="utf-8", newline='') as write_obj:
        feq_write = csv.writer(write_obj)

        feq_write.writerow(["songName", "songFeq", "artistName", "artistFeq"])
        for i in range(0, 100):
            feq_write.writerow(
                [songName[i], str(songFeq[i]), artistName[i], str(artistNameCount[i])])


def spotifySongTop():
    songName1 = []
    songFeq1 = []
    artistName1 = []
    songName2 = []
    songFeq2 = []
    artistName2 = []
    songName3 = []
    songFeq3 = []
    artistName3 = []
    songName4 = []
    songFeq4 = []
    artistName4 = []
    songName5 = []
    songFeq5 = []
    artistName5 = []
    songName6 = []
    songFeq6 = []
    artistName6 = []
    songName7 = []
    songFeq7 = []
    artistName7 = []
    songName8 = []
    songFeq8 = []
    artistName8 = []
    songName9 = []
    songFeq9 = []
    artistName9 = []
    songName10 = []
    songFeq10 = []
    artistName10 = []
    weekCount = 0
    with open("exports/spotify.csv", "r", encoding="utf-8") as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        if header != None:
            for row in csv_reader:
                weekCount += 1
                if (int(row[1]) / 100) <= 1:
                    if weekCount > 1800:
                        songName10.append(row[2])
                        artistName10.append(row[3])
                        songFeq10.append(row[4])
                    elif weekCount > 1600:
                        songName9.append(row[2])
                        artistName9.append(row[3])
                        songFeq9.append(row[4])
                    elif weekCount > 1400:
                        songName8.append(row[2])
                        artistName8.append(row[3])
                        songFeq8.append(row[4])
                    elif weekCount > 1200:
                        songName7.append(row[2])
                        artistName7.append(row[3])
                        songFeq7.append(row[4])
                    elif weekCount > 1000:
                        songName6.append(row[2])
                        artistName6.append(row[3])
                        songFeq6.append(row[4])
                    elif weekCount > 800:
                        songName5.append(row[2])
                        artistName5.append(row[3])
                        songFeq5.append(row[4])
                    elif weekCount > 600:
                        songName4.append(row[2])
                        artistName4.append(row[3])
                        songFeq4.append(row[4])
                    elif weekCount > 400:
                        songName3.append(row[2])
                        artistName3.append(row[3])
                        songFeq3.append(row[4])
                    elif weekCount > 200:
                        songName2.append(row[2])
                        artistName2.append(row[3])
                        songFeq2.append(row[4])
                    elif weekCount > 0:
                        songName1.append(row[2])
                        artistName1.append(row[3])
                        songFeq1.append(row[4])

    with open("exports/spotifyTop.csv", "w", encoding="utf-8", newline='') as write_obj:
        feq_write = csv.writer(write_obj)

        feq_write.writerow(["week1", "songName", "artistName", "streams", "week2", "songName", "artistName", "streams", "week3", "songName", "artistName", "streams", "week4", "songName", "artistName", "streams", "week5", "songName", "artistName",
                            "streams", "week6", "songName", "artistName", "streams", "week7", "songName", "artistName", "streams", "week8", "songName", "artistName", "streams", "week9", "songName", "artistName", "streams", "week10", "songName", "artistName", "streams"])
        for i in range(0, 100):
            feq_write.writerow([str(i+1), songName1[i], artistName1[i], songFeq1[i],
                                str(i +
                                    1), songName2[i], artistName2[i], songFeq2[i],
                                str(i +
                                    1), songName3[i], artistName3[i], songFeq3[i],
                                str(i +
                                    1), songName4[i], artistName4[i], songFeq4[i],
                                str(i +
                                    1), songName5[i], artistName5[i], songFeq5[i],
                                str(i +
                                    1), songName6[i], artistName6[i], songFeq6[i],
                                str(i +
                                    1), songName7[i], artistName7[i], songFeq7[i],
                                str(i +
                                    1), songName8[i], artistName8[i], songFeq8[i],
                                str(i +
                                    1), songName9[i], artistName9[i], songFeq9[i],
                                str(i+1), songName10[i], artistName10[i], songFeq10[i]])


# print(readCSVfile('spotify'))
# first parameter is the chart type, billboard or spotify
# second parameter is top x artists to get
# third parameter is whether you want to generate plot or not
topArtistStats('spotify', 5, True)
topArtistStats('billboard', 5, True)
topSongStats("spotify", 5, True)
topSongStats("billboard", 5, True)
spotifySongFeq()
spotifySongTop()
# print(topSongStats('spotify', 5, True))
# topSongStats('spotify', 5, True)
