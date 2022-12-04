import { DataService } from './../data.service';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.scss']
})
export class HomepageComponent implements OnInit {

  constructor(private data:DataService,
              private router: Router) { }

  ngOnInit(): void {
    // console.log(this.data.getData().toString())
    if(localStorage.getItem('type') == 'Manager'){
      this.router.navigateByUrl('/manager-dashboard')
    }
  }

  gotoTrade(){
    this.router.navigateByUrl('/trade')
  }

  gotoSignup(){
    if(localStorage.getItem('isloggedIn') != 'true'){
      this.router.navigateByUrl('/signup')
    } else {
      this.router.navigateByUrl('/trade')
    }
  }
}
