1. Install VS Code
2. Download Node.js https://nodejs.org/en/download/
3. To install the Angular CLI, open a terminal window and run the following command: npm install -g @angular/cli, https://angular.io/guide/setup-local
4. Open a terminal window in project folder and run the following command to install dependencies: npm install OR npm i
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