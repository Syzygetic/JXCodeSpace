import csv
from os import read
import flask
from flask import render_template
from flask import request
from pathlib import Path
from csv import reader
import json
import urllib
import requests
import urllib.request
import urllib.parse
from shutil import copyfile


app = flask.Flask(__name__)
app.config["DEBUG"] = True

exportPath = f'{Path(__file__).parents[2]}/exports'

spotifyChart = []
billboardChart = []
redditCommentsBillboard = []
redditCommentsSpotify = []
twitterCommentsBillboard = []
twitterCommentsSpotify = []

apiKey = ""


def searchVideo(searchTerm):

    searchQuery = urllib.parse.quote(searchTerm)

    r = requests.get(
        url=f'https://www.googleapis.com/youtube/v3/search?q={searchQuery}&type=video&key={apiKey}')
    data = json.loads(r.content)

    if data['items']:
        return data['items'][0]['id']['videoId']
    else:
        return None


def readCSVfile(filename):
    if filename == 'billboard':
        n = 100
    elif filename == 'spotify':
        n = 200
    fullChartList = []
    with open(f"{exportPath}/{filename}.csv", "r", encoding="utf-8") as read_obj:
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
    # print(chartList)


def readRedditComments(choice):
    fullCommentsList = []
    with open(f"{exportPath}/redditComments_{choice}.csv", "r", encoding="utf-8") as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        if header != None:
            for row in csv_reader:
                songDict = {}
                songDict['songRank'] = int(row[0])
                songDict['songName'] = row[1]
                songDict['songPosts'] = int(row[2])
                songDict['songLikes'] = int(row[3])
                songDict['songComments'] = int(row[4])
                songDict['songSampleTitles'] = list(set(row[5].splitlines()))
                fullCommentsList.append(songDict)
    return fullCommentsList
    # print(chartList)


def readTwitterComments(choice):
    fullCommentsList = []
    with open(f"{exportPath}/twitterComments_{choice}.csv", "r", encoding="utf-8") as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        if header != None:
            for row in csv_reader:
                songDict = {}
                songDict['songRank'] = int(row[0])
                songDict['songName'] = row[1]
                songDict['songComment'] = list(set(row[2].splitlines()))
                fullCommentsList.append(songDict)
    return fullCommentsList
    # print(chartList)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/topcharts")
def topcharts():
    return render_template("topcharts.html", spotifyChart=spotifyChart[0], billboardChart=billboardChart[0])


@app.route("/weeklycharts")
def weeklycharts():

    if request.args.get('week'):
        weekid = int(request.args.get('week'))
    else:
        weekid = 0
    return render_template("weeklycharts.html", spotifyChart=spotifyChart[weekid], billboardChart=billboardChart[weekid])


@app.route("/stats")
def stats():
    copyfile(f'{exportPath}/images/topArtistspotify.png',
             f'{Path(__file__).parents[0]}/static/topArtistspotify.png')
    copyfile(f'{exportPath}/images/topSongspotify.png',
             f'{Path(__file__).parents[0]}/static/topSongspotify.png')
    copyfile(f'{exportPath}/images/topArtistbillboard.png',
             f'{Path(__file__).parents[0]}/static/topArtistbillboard.png')
    return render_template("stats.html")


@app.route("/song")
def song():
    songid = int(request.args.get('id'))
    chartSource = request.args.get('chartSource')
    twitterComment = None
    if chartSource == 'billboard':
        song = billboardChart[0][songid-1]
        redditComment = redditCommentsBillboard[songid-1]
        if songid < len(twitterCommentsBillboard):
            twitterComment = twitterCommentsBillboard[songid-1]
    elif chartSource == 'Spotify':
        song = spotifyChart[0][songid-1]
        redditComment = redditCommentsSpotify[songid-1]
        if songid < len(twitterCommentsSpotify):
            twitterComment = twitterCommentsSpotify[songid-1]
    videoLink = searchVideo(song['songName'] + song['songArtist'])
    return render_template("single_song.html", song=song, videoLink=videoLink, redditComment=redditComment, twitterComment=twitterComment)


if __name__ == '__main__':
    spotifyChart = readCSVfile('spotify')
    billboardChart = readCSVfile('billboard')
    redditCommentsBillboard = readRedditComments('Billboard')
    redditCommentsSpotify = readRedditComments('Spotify')
    twitterCommentsBillboard = readTwitterComments('Billboard')
    twitterCommentsSpotify = readTwitterComments('Spotify')
    app.run(host='0.0.0.0', port=5888)
