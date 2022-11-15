import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { DataService } from '../data.service';
import { NgModule } from '@angular/core';
import UsersJson from './usernft.json';
import { Router } from '@angular/router';

interface USERS{
  Name:String;
  NFT_Address:String;
  NFT_Value:Number;
  Image_URL:String
}



@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
  //Users:USERS[]=UsersJson;

  trade_nfts:any;
  add_money:any;

  public searchFilter: any = '';
  searchText = '';

  constructor(private dataService: DataService,
              private router: Router ) { }
  
  ngOnInit(): void {
    this.dataService.addEth().subscribe((data:any) => {
      console.log(data);
    });

    this.dataService.getTraderNfts().subscribe((data:any) => {
      console.log(this.trade_nfts);
    });

    this.dataService.transaction().subscribe((data:any) =>{

      this.add_money=data.message;
      console.log(this.add_money)
    })

  }

}
