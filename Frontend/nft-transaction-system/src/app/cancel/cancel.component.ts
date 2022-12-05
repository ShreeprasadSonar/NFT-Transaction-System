import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { Router } from '@angular/router';
import { HttpClient, HttpClientModule } from '@angular/common/http';
@Component({
  selector: 'app-cancel',
  templateUrl: './cancel.component.html',
  styleUrls: ['./cancel.component.scss']
})
export class CancelComponent implements OnInit {
  cancelpayment_fait: any;
  cancelpayment_nfts: any;

  public canceldata:any={
    tid:'',
  };

  constructor(private http:HttpClient,private dataService: DataService,
    private router: Router) { }

  ngOnInit(): void {

    this.dataService.getCancellablePayments().subscribe((data:any) => {
      this.cancelpayment_fait=data.fiat_trans;
      this.cancelpayment_nfts=data.nft_trans;
      console.log(data);
    });
  }


  cancelbutton(tid:string){
    this.dataService.cancelPayment(tid).subscribe((data:any) => {
  console.log(data);
  setTimeout(()=>window.location.href="http://localhost:4200/cancel",1000);

  });
  }
}
