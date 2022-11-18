import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { Router } from '@angular/router';




@Component({
  selector: 'app-transactions',
  templateUrl: './transactions.component.html',
  styleUrls: ['./transactions.component.scss']
})
export class TransactionsComponent implements OnInit {

  trade_transhistory_fiat:any;
  trade_transhistory_nfttrans:any;

  constructor(private dataService: DataService,
    private router: Router ) { }

  ngOnInit(): void {

    this.dataService.getTTransHistory().subscribe((data:any) =>{
      this.trade_transhistory_fiat=data.fiat_trans;
      this.trade_transhistory_nfttrans=data.nft_trans;
      console.log(data);
    })
  }

}
