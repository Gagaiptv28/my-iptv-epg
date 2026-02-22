
import requests
import xml.etree.ElementTree as ET

SOURCE_URL = "https://iptv-org.github.io/epg/guides/ge.xml"

response = requests.get(SOURCE_URL)
root = ET.fromstring(response.content)

new_tv = ET.Element("tv")

# ქართული არხების ID-ები (სურვილის მიხედვით შეგიძლია დაამატო)
ge_channels = [
    "1tv.ge",
    "rustavi2.ge",
    "imeditv.ge",
    "mtavari.tv",
    "formula.tv",
    "adjara.tv",
    "palitra.tv",
    "pos.tv"
]

# ვტოვებთ მხოლოდ არხებს
for channel in root.findall("channel"):
    if channel.get("id") in ge_channels:
        new_tv.append(channel)

# ვტოვებთ მხოლოდ შესაბამის პროგრამებს
for programme in root.findall("programme"):
    if programme.get("channel") in ge_channels:
        new_tv.append(programme)

tree = ET.ElementTree(new_tv)
tree.write("epg-ge.xml", encoding="utf-8", xml_declaration=True)

print("ქართული EPG განახლდა წარმატებით")
