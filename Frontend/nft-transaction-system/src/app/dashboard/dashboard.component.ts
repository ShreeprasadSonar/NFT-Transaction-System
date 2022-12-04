import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { DataService } from '../data.service';
import { NgModule } from '@angular/core';
import UsersJson from './usernft.json';
import { Router } from '@angular/router';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
  //Users:USERS[]=UsersJson;

  trade_nfts:any;
  add_money:any;
  ethfiatvalue:any;
  public searchFilter: any = '';
  searchText = '';
  userDetails:any;
  ethValueInFiat: any;

  constructor(private dataService: DataService,
              private router: Router ) {
                
               }
  
  ngOnInit(): void {
    this.dataService.getTraderNfts().subscribe((data:any) => {
      this.trade_nfts=data.message;
      this.ethfiatvalue=data;
      this.ethValueInFiat = (this.ethfiatvalue.ethCnt * this.ethfiatvalue.ethValue).toFixed(2)
      const mem = document.getElementsByClassName('memType').item(0) as HTMLElement;
      if(this.ethfiatvalue.memType == 'GOLD'){
        mem.style.color = "Gold"
      }
      else if(this.ethfiatvalue.memType == 'SILVER'){
        mem.style.color = "Silver"
      }
    });

    this.dataService.getTraderInfo().subscribe((data:any) => {
      this.userDetails=data.data;
    }); 
  }
  date(){
    let date=new Date();
    console.log(date);
    this.router.navigate(['./cancel']);
  };

}
