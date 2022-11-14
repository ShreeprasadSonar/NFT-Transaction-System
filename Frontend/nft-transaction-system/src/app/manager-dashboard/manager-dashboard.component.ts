import { Component, OnInit } from '@angular/core';
import UsersJson from './allusernft.json';
import {ViewEncapsulation} from '@angular/core';
import {MatCalendarCellClassFunction} from '@angular/material/datepicker';


interface USERS{
  NFT_Name:String;
  Trans_ID:String;
  NFT_Value:Number;
  Status:String;
  Trans_date_time: String;
}
 
 
 
@Component({
  selector: 'app-manager-dashboard',
  templateUrl: './manager-dashboard.component.html',
  styleUrls: ['./manager-dashboard.component.scss'],
  encapsulation: ViewEncapsulation.None,
})
export class ManagerDashboardComponent implements OnInit {

  toDisplay = false;
  
  toggleData() {
    this.toDisplay = !this.toDisplay;
  }


  Users:USERS[]=UsersJson;
  constructor() { }
 
  ngOnInit(): void {
  }


  
}

export class DatepickerDateClassExample {
  dateClass: MatCalendarCellClassFunction<Date> = (cellDate, view) => {
    // Only highligh dates inside the month view.
    if (view === 'month') {
      const date = cellDate.getDate();

      // Highlight the 1st and 20th day of each month.
      return date === 1 || date === 20 ? 'example-custom-date-class' : '';
    }

    return '';
  };
}
