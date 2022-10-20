import { AuthService } from './../auth.service';
import { Component, OnInit } from '@angular/core';
const scroller = document.querySelector("#scroller");

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {
  isloggedIn:Boolean = false

  constructor(private authService:AuthService) {
    if(localStorage.getItem('isloggedIn') == 'true'){
      this.isloggedIn = true
    } else{
      this.isloggedIn = false
    }
  }

  readisloggedIn(){
    if(localStorage.getItem('isloggedIn') == 'true'){
      return true;
    } else{
      return false;
    }
  }

  ngOnInit(): void {
    if(localStorage.getItem('isloggedIn') == 'true'){
      this.isloggedIn = true;
    } else{
      this.isloggedIn = false;
    }
    $(document).ready(function(){
      $(".dropdown").on("hide.bs.dropdown", function(){
        $(".btn").html('Dropdown <span class="caret"></span>');
      });
      $(".dropdown").on("show.bs.dropdown", function(){
        $(".btn").html('Dropdown <span class="caret caret-up"></span>');
      });
    });
  }

  logout(){
    this.authService.logout()
    this.ngOnInit()
  }

}
