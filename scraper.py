import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen
r = urlopen("https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions")


beaut_soup = BeautifulSoup(r.read(),'html.parser')
table_S = beaut_soup.findAll("table",{"class" : "wikitable sortable"})
tab=table_S[1]

## Importing to a CSV file ###


with open('result.csv','w') as csvfile:
    fun =['Game_No' ,'Year','Winning_team','Score','Losing_team','Venue']
    w = csv.writer(csvfile,delimiter =',')
    w.writerow(fun)
    for row in tab.findAll('tr')[1:51]:
       column = row.findAll('td')
       game_number = column[0].find('a').get_text()
       year = column[1].get_text()
       year_s = year[-4:]
       winning_team = column[2].get_text()
       winning_team_s=(winning_team.split("!"))
       win = winning_team_s[0]
       score = (column[3].get_text().split("!"))[1]
      # score_s = sc.split("!")
       #score = score_s[1]
       losing_team = column[4].find('a').get_text()
       ven = column[5].get_text()
       venue_s = ven.split("!")
       venue = venue_s[0]
       w.writerow((game_number ,year_s , win , score , losing_team ,venue))
       print (game_number + ',' + year_s + ',' +win+',' +score +',' +losing_team +','+venue)
