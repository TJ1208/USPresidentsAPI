import requests

query = "presidents of the united states"
url = "https://api.duckduckgo.com/?q="+query+"&format=json"
response = requests.get(url).json()['RelatedTopics']
print(response)


def test_presidents_api():
    presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe",
                  "Jackson", "Buren", "Harrison", "Tyler", "Polk", "Taylor",
                  "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson", "Grant",
                  "Hayes", "Garfield", "Arthur", "Cleveland", "McKinley",
                  "Roosevelt", "Taft", "Wilson", "Harding", "Coolidge", "Hoover",
                  "Truman", "Eisenhower", "Kennedy", "Johnson", "Nixon", "Ford",
                  "Carter", "Reagan", "Bush", "Clinton", "Bush", "Obama", "Trump",
                  "Biden"]
    for i in response:
        president = i['FirstURL']
        for i in presidents:
            if president.__contains__(i):
                presidents.remove(i)
                break
    assert len(presidents) == 0

