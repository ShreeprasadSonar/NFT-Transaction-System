import { Component, OnInit } from '@angular/core';
const scroller = document.querySelector("#scroller");

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
    $(document).ready(function(){
      $(".dropdown").on("hide.bs.dropdown", function(){
        $(".btn").html('Dropdown <span class="caret"></span>');
      });
      $(".dropdown").on("show.bs.dropdown", function(){
        $(".btn").html('Dropdown <span class="caret caret-up"></span>');
      });
    });
  }

}
