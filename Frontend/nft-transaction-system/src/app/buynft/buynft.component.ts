import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { Router, ActivatedRoute  } from '@angular/router';
import { HttpClient, HttpClientModule } from '@angular/common/http';
@Component({
  selector: 'app-buynft',
  templateUrl: './buynft.component.html',
  styleUrls: ['./buynft.component.scss']
})
export class BuynftComponent implements OnInit {
  x: any;
  usdeth:string='';
  address:string='';
  alert=false;


  public buynftform:any={
    usdeth:'',
  };
  msg: any;

  constructor(private http:HttpClient,private dataService: DataService,
    private router: Router, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.route.queryParams
    .subscribe(params => {
    console.log(params['address']);
    this.x=params['address'] ; 
    console.log("x is",this.x) ;

    }
  );

  }

  submit(){

    this.dataService.buynft(this.buynftform.address,this.buynftform.usdeth).subscribe((data:any) => {
      this.msg=data;
      console.log(this.msg);
      this.alert=true;
      setTimeout(()=>window.location.href="http://localhost:4200/dashboard",3000);
    });
    
    
    
}
}
