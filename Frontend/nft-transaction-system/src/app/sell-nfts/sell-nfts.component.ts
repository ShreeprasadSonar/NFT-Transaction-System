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
  check=false;
  selldata: any;

  constructor(private dataService: DataService,
              private router: Router ) { }
  
  ngOnInit(): void {
      this.dataService.getTraderNfts().subscribe((data:any) => {
        this.nfts = data.message;
        console.log(this.nfts);
      });
  }


  sellnft(add:string){
    this.dataService.sellnfts(add).subscribe((data:any)=>{
      this.selldata=data;
      this.check=true;
      setTimeout(()=>window.location.href="http://localhost:4200/dashboard",5000);
    })


  }


}
