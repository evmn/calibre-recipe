import xml.etree.ElementTree as ET
tree = ET.parse('rss.xml')
root = tree.getroot()
for child in root:
    title = child.find('title').text
    link = child.find('link').text
    print title, link
