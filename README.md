# NFT-Transaction-System
Project for CS 6360 Database design


# Project description
In this project, we implemented a web based NFT trading application that can support buying and selling NFT’s with ease. The trader can choose to buy or sell the NFT’s by paying a minimal commission to the system. From time to time, trader can transfer money/Ethereum to their account so that they can buy more NFTs. In this system traders can cancel certain payment and NFT transactions, system will allow such cancellations up to 15 mins after the transaction submission. For this system we have a manager who can see what all transactions performed by traders for daily, weekly, and monthly total transactions based on the dates entered by the manager. For the front end we are using a typescript based Angular Framework and for backend we are using a python-based application framework called flask. For storing traders’ data and transaction data we are using MySQL database. 

# ER Diagram 
![This is an image](https://github.com/varunpotluri8/NFT-Transaction-System/blob/main/DB_P1.png)

# Relational Schema
![This is an image](https://github.com/varunpotluri8/NFT-Transaction-System/blob/main/RS.png)

# How to Run

## BackEnd Installation:

1. Download and install VS Code
2. To install the latest version of Python, visit the given website: https://www.python.org/downloads/
3. Open a terminal window in the project folder and head on to the "Backend" directory. After that, run the following command to install the requirements file: pip install -r requirements.txt
4. All modules listed as libraries in the requirements.txt file will be installed.
    
    Libraries:
    eth_account==0.5.9
    Flask==2.0.2
    Flask_Cors==3.0.10
    Flask_MySQLdb==1.0.1
    phonenumbers==8.12.57
    PyJWT==2.6.0
    requests==2.28.1

5. Run the following command to build, deploy, and serve: "python app.py" or for production use: production WSGI server
6. The Python script would be accessible at http://localhost:5000. 



## FrontEnd Installation:

1. Install VS Code
2. Download Node.js https://nodejs.org/en/download/
3. To install the Angular CLI, open a terminal window in VS code and run the following command: npm install -g @angular/cli, https://angular.io/guide/setup-local
4. Open a terminal window and navigate to Frontend folder.Then nagivate to nft-transaction-system and run the following command to install dependencies: npm install OR npm i
5. All modules listed as dependencies in package.json will be installed if any dependencies are not installed use this format: npm install [package-name]@[version-number]
    Dependencies:
    "@angular/animations": "^14.2.0",
    "@angular/cdk": "^14.2.7",
    "@angular/common": "^14.2.0",
    "@angular/compiler": "^14.2.0",
    "@angular/core": "^14.2.0",
    "@angular/forms": "^14.2.0",
    "@angular/material": "^14.2.7",
    "@angular/platform-browser": "^14.2.0",
    "@angular/platform-browser-dynamic": "^14.2.0",
    "@angular/router": "^14.2.0",
    "jquery": "^3.6.1",
    "moment": "^2.29.4",
    "popper.js": "^1.16.1",
    "rxjs": "~7.5.0",
    "tslib": "^2.3.0",
    "zone.js": "~0.11.4"

    Dev Dependencies: 
    "@angular-devkit/build-angular": "^14.2.6",
    "@angular/cli": "~14.2.6",
    "@angular/compiler-cli": "^14.2.0",
    "@types/jasmine": "~4.0.0",
    "@types/jquery": "^3.5.14",
    "jasmine-core": "~4.3.0",
    "karma": "~6.4.0",
    "karma-chrome-launcher": "~3.1.0",
    "karma-coverage": "~2.2.0",
    "karma-jasmine": "~5.1.0",
    "karma-jasmine-html-reporter": "~2.0.0",
    "typescript": "~4.7.2"
6. run the following command to build, deploy & serve: ng serve OR npm run ng serve
7. Angular Live Development Server will be listening on localhost:4200, open your browser on http://localhost:4200/


## Database Installation:

1. Download MYSQL
2. Open VS Code
3. In the Extension tab -> search and install MYSQL management tool
4. Open MYSQL location in the computer using file explorer. Usually in C Drive -> Program File.
5. After finding the location. Open command promt from that particular location.
6. Connect to MYSQL and perform the follwing commands:
   i)mysql -u root -p
   ii)CREATE USER 'sqluser'@'%' IDENTIFIED WITH mysql_native_password BY 'password'; 
   iii)GRANT ALL PRIVILEGES ON *.* TO 'sqluser'@'%'; 
   iv)FLUSH PRIVILEGES;
7. After performing above commands. Open VS Code. You will see SQL Folder in the EXPLORER window.
8. Click on '+' symbol beside MYSQL. Enter the following details:
   i)host - localhost
   ii)user - sqluser
   iii)passowrd - password
9. By doing this we dont need to change id and passowrd details in the code.
10. Now open Create.sql from Databse folder in the source(main folder) and Execute Create.sql. All the tables will be created.
11. Now Execute Data.sql inorder to start trading.
