# NFT-Transaction-System
Project for CS 6360 Database design



Frontend of the project is built/developed on Angular Framework using Node.js runtime environment. The name of the project folder is “NFT-transaction-system" with all the code in “src/” folder. The “src/” folder contains primary HTML, TS, SCSS files with other components in “src/app/” folder containing routing module for all the routes to specific component, app.component has selectors for header and router outlet, auth and data services and authentication guard. Auth and data services contains api calls consumed by all the components in the app folder for validation and data retrieval purposes. 


Backend of the project is developed using Flask (a Python Framework). The name of the project file is “app.py” which contains the entire project code. This file contains all the import statements for importing various libraries, APIs that have been built for all the necessary functionalities, dynamically retrieving values of ETH and other necessary logics are included in the file.


For the storing all the data logs generated we used MySQL. The script files are in the subfolder called “Database” in the parent folder “NFT-transaction-system”. It contains script used to create database and associated tables, script to drop the tables and data such as commission rates, NFT’s for the marketplace and manager credentials. 
