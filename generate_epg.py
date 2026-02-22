import requests
import xml.etree.ElementTree as ET

SOURCE_URL = "http://epg.team/tvteam.3.1.xml"

response = requests.get(SOURCE_URL)
response.raise_for_status()

root = ET.fromstring(response.content)

new_tv = ET.Element("tv")

# ქართული არხების ID ფილტრი (რეალურ XML ID-ს უნდა დაემთხვეს)
ge_channels = {
    "1tv",
    "Rustavi2",
    "mtavari.ge",
    "formula",
    "adjara",
    "palitra",
    "pos",
    "imedi"
}

# Channel copy
for channel in root.findall("channel"):
    if channel.get("id") in ge_channels:
        new_tv.append(channel)

# Programme copy
for programme in root.findall("programme"):
    if programme.get("channel") in ge_channels:
        new_tv.append(programme)

tree = ET.ElementTree(new_tv)

tree.write("epg-ge.xml",
           encoding="utf-8",
           xml_declaration=True)

print("✅ ქართული EPG წარმატებით განახლდა")
