import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { DataService } from '../data.service';
import { NgModule } from '@angular/core';
import UsersJson from './usernft.json';

interface USERS{
  Name:String;
  NFT_Address:String;
  NFT_Value:Number;

}



@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
  Users:USERS[]=UsersJson;

  constructor(private data:DataService) { }

  ngOnInit(): void {
    this.data.addEth().subscribe((data:any) => {
      console.log(data);
    });
  }

}
