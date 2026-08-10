import requests
from bs4 import BeautifulSoup
import html
import json


class Api:
    def __init__(self, stop_number, operator):
        self.url = f"https://www.mpvnet.cz/{operator}/tab/departures"
        self.headers = {"origin": "https://www.mpvnet.cz"}
        self.payload = {
            "isDepartures": True,
            "StopKey": f'{{"cat":2,"subCat":0,"stopNum":{stop_number},"departures":null}}'
        }


    def parse_html(self, text):
        soup = BeautifulSoup(text, "html.parser")
        rows = soup.select(".timetable-row")[1:]  

        output = []

        for row in rows:
            line_val = row.select_one(".timetable-line .timetable-value")
            line_number = line_val.find_all("div")[0].get_text(strip=True)
            line_internal = line_val.find_all("div")[1].get_text(strip=True)
            dest_val = row.select_one(".timetable-destination .timetable-value")
            dest_main = dest_val.contents[0].strip()
            dest_detail = dest_val.select_one(".grey-text").get_text(strip=True)
            departure = row.select_one(".timetable-item:nth-of-type(4) .timetable-value").get_text(strip=True)
            platform = row.select_one(".timetable-item:nth-of-type(5) .timetable-value").get_text(strip=True)
            delay = row.select_one(".timetable-delay .timetable-value span").get_text(strip=True)

            item = {
                "line": html.unescape(line_number),
                "line_internal": html.unescape(line_internal),
                "destination": html.unescape(dest_main),
                "destination_detail": html.unescape(dest_detail),
                "departure": html.unescape(departure),
                "platform": html.unescape(platform),
                "delay": html.unescape(delay)
            }

            output.append(item)

        return output


    def get_data(self, url, headers, payload):
        return requests.post(url, headers=headers, json=payload).text

    def sync(self):
        return self.parse_html(self.get_data(self.url, self.headers, self.payload))


class Stop:
    @staticmethod
    def get_num(stop_name, operator):
        return requests.post(f"https://www.mpvnet.cz/{operator}/tab/stops", headers={"origin": "https://www.mpvnet.cz"}, json={"value":f"{stop_name}"}).text

        