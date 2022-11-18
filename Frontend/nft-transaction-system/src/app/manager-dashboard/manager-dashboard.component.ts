import { Component, OnInit } from '@angular/core';
import UsersJson from './allusernft.json';
import {ViewEncapsulation} from '@angular/core';
import {MatCalendarCellClassFunction} from '@angular/material/datepicker';
import { FormBuilder, FormGroup } from '@angular/forms';


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
  constructor() { 

    
  }
 
  ngOnInit(): void {


  }


  
}


