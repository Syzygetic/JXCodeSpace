from bs4 import BeautifulSoup
from BaseScraperClass import BaseScraper
from SongClass import Song
from general import *


class billboardScraper(BaseScraper):

    def scrapeData(self):
        tempArr = []
        response = self.get_HTML_data()
        soup = BeautifulSoup(response, 'html.parser')

        container = soup.find_all('ol', class_='chart-list__elements')
        index = 1

        for items in container:
            result = items.find_all(
                'li', class_='chart-list__element display--flex')
            for i in result:
                # artist
                songName = (i.find_all(
                    class_='chart-element__information__song')[0].getText())
                artist = (i.find_all(
                    class_='chart-element__information__artist')[0].getText())
                print(f"Creating song object: {index} {songName}")
                song = Song("billboard", index, songName, artist, 0)
                tempArr.append(song)

                index += 1

        return tempArr


numberWeeks = 10
base_url = "https://www.billboard.com/charts/hot-100"

# main---------------------------------------------------------------------------
dateRange = getDateRange()
dates = getMyDate(numberWeeks, dateRange)
check = False
objectArray = []

for elements in dates:
    if check == False:
        url = base_url
        check = True
    else:
        url = base_url + '/' + elements

    scraper = billboardScraper(url)
    objectArray.extend(scraper.scrapeData())

saveToFile(objectArray, 'billboard')
