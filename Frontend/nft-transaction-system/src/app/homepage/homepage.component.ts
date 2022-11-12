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
  }

  goto(link:string){
    this.router.navigateByUrl('/trade')
  }
}
