# Setupper

The interactive task calendar with the stupid name. 

This is my first Django project. It is intended to be an interative calendar application for tracking event and classroom equipment setups in the audio-visual/IT department at the University where I work. 



## Notes, primarily for my working reference

- Data shall be stored in a MySQL database. The primary table will be a table of individual resource requests, each with an associated date-time, place, resource name, event number and name, user responsible for setting up/striking, and some other stuff, mostly as foreign keys. 

- The main page framework, consisting of a grid of rooms on the vertical axis and times in half hour increments on the horizontal axis, will be generated on GETting the page, probably using Django's templating. 

- Time will span three days, the present and one day ahead and behind (tentatively, might be too much), and the rooms will be pulled from the database, which will contain their relative positions on the grid (since this will likely need to be tweaked, plus I need to accomodate some special 'meta'-rooms which are actually combinations of other rooms). 

- After this frame has loaded the contents will be pulled in with AJAX and rendered using React (I think. I still have to learn both of those things). 

- Thereafter the calendar will be regularily refreshed by Ajax. I still have to figure this out. I'm assuming there is some database flag I can check to alert me when changes are made so I don't have to fetch the entire day's data every time.

- Also, a thin vertical red line will show the current time, and eventually, and alarm will go off if an unset event is getting close. 
