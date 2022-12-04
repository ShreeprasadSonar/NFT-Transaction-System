import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-trade',
  templateUrl: './trade.component.html',
  styleUrls: ['./trade.component.scss']
})

export class TradeComponent implements OnInit {
  nfts:any;
  public searchFilter: any = '';
  searchText = '';
  ethValueInD:any;

  constructor(private dataService: DataService,
              private router: Router ) { }
  
  ngOnInit(): void {
    this.dataService.getNfts().subscribe((data:any) => {
      this.nfts = data.message;
    });
    this.dataService.getTraderNfts().subscribe((data:any) => {
      this.ethValueInD = data.ethValue;
    });
  }

  makeTransaction(add:string){
    this.router.navigate(
      ['/buynft'],
      { queryParams: { address: add } }
    );
  }

}
