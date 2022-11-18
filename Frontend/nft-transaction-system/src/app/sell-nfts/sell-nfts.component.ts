import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-sell-nfts',
  templateUrl: './sell-nfts.component.html',
  styleUrls: ['./sell-nfts.component.scss']
})
export class SellNftsComponent implements OnInit {

  nfts:any;
  public searchFilter: any = '';
  searchText = '';

  constructor(private dataService: DataService,
              private router: Router ) { }
  
  ngOnInit(): void {
      this.dataService.getTraderNfts().subscribe((data:any) => {
        this.nfts = data.message;
        console.log(this.nfts);
      });
  }
}
