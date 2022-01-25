# ForkLotus
A fork of pylotus (https://github.com/alex-claman/pylotus). 

This project started out as personal modifications to expand upon and update pylotus to include parts of the warframe api that hadn't been implemented yet. It eventually turned into a project in its own right when additional funtionality and changes went beyond the scope of the original. As such, forklotus occasionally changes the format of incoming api information to make it easier to customize. For example, the 'node' key in the warframe api's fissure information is in the combined format of "node_name (planet_name)". The Fissure response class in forklotus retains this information in a location variable but also splits the information into node and planet variables for easier customization. Forklotus also fixes a host of other problems such as certain keys not always being present in the api and the removal of keys that are no longer present in the warframe api.
## Installation
Going to have to go old school on this until I get this set up on pip, just download the forklotus directory from this repository and place it in your project's directory. Requirements are the same as PyLotus. Importing the project depends on where it is placed in your project directory. For example, if forklotus is placed in your project directory directly then the following can be used to import it.
```python
from forklotus import *
```
If you don't want the response classes and wish to work directly with json from the warframestats api you can specifically import
```python
from forklotus import wf_api
```
## Usage
Initialization of the API for a specific platform is the same as with PyLotus. ```wf_api``` accepts ```'pc'```, ```'xb1'```, ```'ps4'```, and ```'swi'``` as valid platforms.
```python
pc_wf = wf_api('pc') #Creates an instance with your preferred platform
```
You can get json formatted dict objects from the warframestats api by calling specific functions from the ```wf_api``` instance you just created.
```python
fissures_json = pc_wf.get_current_fissures() #Gets a list of JSON response dicts
```
You can use the built in response classes, like ```Fissures``` to wrap common api responses and make then easier to work with.
```python
fissures = Fissures(fissures_json) #Feed it the list of JSON response dicts
```
Alternatively you can do this at the same time by calling them together
```python
pc_wf = wf_api('pc') #Creates an instance with your preferred platform
fissures = Fissures(wf_api.get_current_fissures()) #Interpret fissure response json from the Warframestats API
```
You can even add error checking using the built in error classes
```python
try:
  pc_wf = wf_api('pc') #Attempt to initialize the Warframestats API
  fissures = Fissures(wf_api.get_current_fissures()) #Attempt to interpret fissure response json from Warframestats API
except LotusError as e:
  print(f"Warframe API Error: {e}") #Catch any errors that might occur
  #Fail successfully
else:
  #Op Success
```
Using the resulting ```fissures``` object is straightforward.
```python
print(len(fissures.list)
for fissure in fissures.list:
  print(f"{fissure.tier}, {fissure.enemy}, {fissure.missionType}, {fissure.node}, {fissure.planet}") 
  #Note: fissure.location can be used to get the node and planet in the combined form of "node (planet)"
```
```python
>>> 5
>>> Lith, Grineer, Rescue, Martialis, Mars
>>> Meso, Grineer, Interception, Rhea, Saturn
>>> Neo, Grineer, Interception, Umbriel, Uranus
>>> Axi, Infested, Extermination, Saxis, Eris
>>> Requiem, Grineer, Disruption, Tamu, Kuva Fortress
```


