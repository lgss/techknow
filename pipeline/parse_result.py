import sys
import xml.etree.ElementTree as ET

tree = ET.parse(sys.argv[1])
root = tree.getroot()

print(int(root.attrib['errors']) + int(root.attrib['failures']))