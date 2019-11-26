import requests
from selenium import webdriver as wd
from bs4 import BeautifulSoup


def jumpLink(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    return soup


def main():

    origin = 'http://cotoba.sijisuru.com/'
    url = origin
    # res = requests.get('http://cotoba.sijisuru.com/')

    soup = jumpLink(origin)
    title = soup.title

    query = input('\n***検索したい文字を入力してください***\n')
    searchLetter = ''
    searchNum = ''
    for i in range(len(query)):
        letter = query[i]
        if letter.isalpha():
            searchLetter += letter
        elif letter.isdigit():
            searchNum += letter

    # searchNum = int(searchNum)

    # print("Letter %s, Num %d" % (searchLetter, searchNum))

    letters = soup.find_all('a', {'class': 'btn-app'})
    for letter in letters:
        if letter.string == searchLetter:
            url = url[:-1]
            url += letter['href']
            break

    soup = jumpLink(url)
    divContainer = soup.find('div', {'class': 'let_nar'})

    for link in divContainer.find_all('a'):
        if link.string == searchNum + '字':
            url = origin[:-1]
            url += link['href']
            break

    soup = jumpLink(url)
    td = soup.find_all('td')

    for item in td:

        if item.string != None and len(item.string) == int(searchNum):
            if item.string[-1] != 'ん' and item.string[-1] != 'ン':
                print(item.string)


while True:
    main()
