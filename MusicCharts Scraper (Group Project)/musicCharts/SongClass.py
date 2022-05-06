class Song:
    chartSource = ''
    songName = ''
    songArtist = ''
    songRank = 0
    songStreams = 0

    def __init__(self, chartSource, songRank, songName, songArtist, songStreams):
        self.chartSource = chartSource
        self.songRank = songRank
        self.songName = songName
        self.songArtist = songArtist
        self.songStreams = songStreams

    # def setSongName(self, songName):
    #     self.songName = songName

    # def setSongArtist(self, songArtist):
    #     self.songArtist = songArtist

    # def setSongRank(self, songRank):
    #     self.songRank = songRank

    # def setSongStream(self, songStream):
    #     self.songStream = songStream

    # def getSongName(self):
    #     return self.songName

    # def getSongArtist(self):
    #     return self.songArtist

    # def getSongRank(self):
    #     return self.songRank

    # def getSongStreams(self):
    #     return self.songStreams
