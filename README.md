# MAP APP
User inputs profile name, whose friends s/he wants to see. If the input is empty or there is no profile with such name or this profile has no friends user sees a message. If the input is correct map is generated. On the map there is 15 markers of locations of the first 15 profiles that are friends of input profile. If input profile has less than 15 friends with added location than there is less markers on the map. If point cursor on the marker, user can see a profile name of that friend.

## INSTALLATION
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install following libraries:
- `pip install flask`
- `pip install folium`
- `pip install geopy`

## Structures of HTML files
Files consist of three parts (head, body, script).
- `<head> <\head> - includes header of the HTML file`
- `<body> <\body> - includes main part (map or message)`
- `<script> <\script> - includes process to complete (functions etc.)`

## Example of running program
![](1.png)
![](2.png)
![](3.png)
![](4.png)

## Conclusion
Map shows information about location of friends of given profile.
