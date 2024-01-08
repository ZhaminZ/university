import re
import urllib.request
import csv

url = "https://msk.spravker.ru/avtoservisy-avtotehcentry"
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
pattern = r"(?:class=\"org-widget-header__title-link\">)(?P<name>.+)(?:<)(?:[^+]+)(?:location\">\s+)(?P<adr>.+)(?:[^+]+)(?P<phone>[^<]+)(?:<)(?:[^А-я]+)(?:.+[^А-я]+)(?P<time>.+)(?:<)"

match = re.findall(pattern, html)

with open("data.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Название", "Адрес", "Телефон", "Часы работы"])

    for i in match:
        writer.writerow(i)
