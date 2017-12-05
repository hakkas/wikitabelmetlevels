list = """namen van de leerlingen"""

print ("""
{| class="wikitable sortable"
! Naam style='width: 200px;'|
! style="text-align: center; background-color: white;" | Level 1
! style="text-align: center; background-color: yellow;" | Level 2
! style="text-align: center; background-color: orange;" | Level 3
! style="text-align: center; background-color: green;" | Level 4
! style="text-align: center; background-color: blue;" | Level 5
|-
""")
for line in list.split(','):
  print ("| style='width: 200px;' |" , end="")
  print (line)
  print ("""| style="text-align: center; background-color: white;" | [[Bestand:VinkjeGroen.png]]
| style="text-align: center; background-color: yellow;" |
| style="text-align: center; background-color: orange;" |
| style="text-align: center; background-color: green;" |
| style="text-align: center; background-color: blue;" |
|-""")

print ("|}")
