import requests
from bs4 import BeautifulSoup

def get_corona_summary():
    url = "http://ncov.mohw.go.kr/"

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    patients = soup.select(".liveNum span.num")

    results={
        '확진환자' : int(patients[0].text.replace(',','').replace('(누적)','')),
        '완치' : int(patients[1].text.replace(',','')),
        '치료중' : int(patients[2].text.replace(',','')),
        '사망' : int(patients[3].text.replace(',',''))
    }
    return results


#if __name__ == "__main__":
# print(get_corona_summary())

