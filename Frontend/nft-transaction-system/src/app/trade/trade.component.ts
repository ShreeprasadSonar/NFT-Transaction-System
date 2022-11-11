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

  constructor(private dataService: DataService,
              private router: Router ) { }

  ngOnInit(): void {
      this.dataService.getNfts().subscribe((data:any) => {
        this.nfts = data;
        console.log(this.nfts);
      });
  }

}
