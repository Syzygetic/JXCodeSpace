from bs4 import BeautifulSoup
import BaseScraperClass
import SongClass
import general


class SpotifyScraper(BaseScraperClass.BaseScraper):
    date_list = []

    def __init__(self, url):
        super().__init__(url)

    def getDateRange(self):
        response = self.get_HTML_data()
        soup = BeautifulSoup(response, 'html.parser')

        date_list_soup = soup.findAll(
            class_='responsive-select')[2].findAll('li')

        for i in date_list_soup:
            self.date_list.append(i.get('data-value'))

    def getChartData(self):
        response = self.get_HTML_data()
        soup = BeautifulSoup(response, 'html.parser')
        songs_table = soup.find('tbody').findAll('tr')

        songClassList = []

        for song in songs_table:
            song_rank = song.find(class_='chart-table-position').text
            song_title = song.find('strong', text=True).text
            song_artist = song.find('span').text.replace('by ', '')
            song_streams = song.find(
                class_='chart-table-streams').text.replace(',', '')
            tempSongClass = SongClass.Song(
                'Spotify', int(song_rank), song_title, song_artist, int(song_streams))
            songClassList.append(tempSongClass)
        return songClassList


getDates = SpotifyScraper(
    'https://spotifycharts.com/regional/sg/weekly/latest')
getDates.getDateRange()
print(getDates.date_list[:10])

# scrape first 10 date ranges
allWeeks = []
for index, i in enumerate(getDates.date_list[:10]):
    newSongClass = SpotifyScraper(
        f'https://spotifycharts.com/regional/global/weekly/{getDates.date_list[index]}')
    print(f'{newSongClass.getChartData()}\n')
    allWeeks += newSongClass.getChartData()
general.saveToFile(allWeeks, f'spotify')
