import lxml.etree as et

doc = et.parse('../DATA/solar.xml')  # parse XML file

root = doc.getroot()
print(f"root: {root}")

for planet in doc.findall('.//planet'):  # find all elements (relative to root element) with tag "planet"
    planet_name = planet.get('planetname')
    print(planet_name)      # get XML attribute value
    if planet_name == "Earth":
        new_moon = et.Element('moon')
        new_moon.text = "Luna"
        planet.append(new_moon)
        et.SubElement(planet, "moon", color="pale white").text = "Serena"
    for moon in planet.findall('moon'):  # find all child elements with tag "moon"
        print('\t{}'.format(moon.text))  # print text contained in "moon" tag

doc.write("newsolar.xml", pretty_print=True, xml_declaration=True)

xml_text = et.tostring(doc.getroot(), pretty_print=True, xml_declaration=True).decode()
print(xml_text)
