1.	Download and install latest version of MongoDB
2.	Download and install latest version of Node JS
3.	terminal 1:	open command prompt, and cd to extracted folder.
4.	This step is optional as i have already included necessary packages. If in case you want to start form scratch,
	delete node_modules in the extacted folder.
	run "npm install", so that it installs all necessary packages. 
5.	once all the necessary packages has downloaded, make sure node_modules package is created. (only if npm install has run)
6.	terminal2:	open one more command prompt terminal and type "mongod", this initializes our mongo database session with port 27017
7. 	navigate to terminal 1 and type "node server"
	you should see a success message saying port has initialized on the port 3000. (this is where express is bought up)
8.	navigate to browser and hit url "http://localhost:3000/app.html"