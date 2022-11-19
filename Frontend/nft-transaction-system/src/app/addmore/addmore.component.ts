import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { DataService } from '../data.service';
import { Router } from '@angular/router';
@Component({
  selector: 'app-addmore',
  templateUrl: './addmore.component.html',
  styleUrls: ['./addmore.component.scss']
})
export class AddmoreComponent implements OnInit {
  
    usdeth:string='';
    amtcnt:number=0;
    acntno:number=0;
    rtno:number=0;

  public addmoreform:any={
    usdeth:''
  };


  constructor(private http:HttpClient,private dataService: DataService,
    private router: Router ) { 
    
  }

  ngOnInit(): void {


    

  }
//example 
  submit(){
    this.dataService.transaction(this.addmoreform.amtcnt,this.addmoreform.usdeth).subscribe((data:any) => {
      console.log(data);
    });
    console.log(this.addmoreform);
    console.log(this.addmoreform.usdeth);
}
}
