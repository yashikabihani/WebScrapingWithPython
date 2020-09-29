import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05361000000005&lon=-118.24549999999999#.X3KzGpMzafU');
soup = BeautifulSoup(page.content, 'html.parser')

# print(soup)
# print(soup.find_all('a'))
week = soup.find(id='seven-day-forecast-list')
# print(week)

items = week.find_all(class_='tombstone-container')
# print(items[0])

print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())

period_names = [(item.find(class_='period-name').get_text()).encode('utf-8') for item in items]
short_descs = [(item.find(class_='short-desc').get_text()).encode('utf-8') for item in items]
temps = [(item.find(class_='temp').get_text()).encode('utf-8') for item in items]
print(period_names)
print(short_descs)
print(temps)


weather_stuff = pd.DataFrame({
    'periods' : period_names,
    'short_descriptions' : short_descs,
    'temperatures' : temps
})

print(weather_stuff)

weather_stuff.to_csv('weather.csv')