import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { Router, ActivatedRoute  } from '@angular/router';
import { filter } from 'rxjs';



@Component({
  selector: 'app-transactions',
  templateUrl: './transactions.component.html',
  styleUrls: ['./transactions.component.scss']
})
export class TransactionsComponent implements OnInit {

  trade_transhistory_fiat:any;
  trade_transhistory_nfttrans:any;

  constructor(private dataService: DataService,
    private router: Router, private route: ActivatedRoute ) { 
      // console.log(this.router.getCurrentNavigation().extras.state.example);
    }

  ngOnInit(): void {

    this.route.queryParams
      .subscribe(params => {
        console.log(params); // { orderby: "price" }
        // this.orderby = params.orderby;
        // console.log(this.orderby); // price
      }
    );

    this.dataService.getTTransHistory().subscribe((data:any) =>{
      this.trade_transhistory_fiat=data.fiat_trans;
      this.trade_transhistory_nfttrans=data.nft_trans;
      console.log(data);
    })
  }

}
