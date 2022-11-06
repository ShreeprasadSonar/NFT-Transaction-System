import { Router } from '@angular/router';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormControl,FormGroup,Validators,FormBuilder } from '@angular/forms';
import * as moment from "moment";

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  isloggedIn = false

  constructor(private http: HttpClient,
              private router: Router) { 
                if(localStorage.getItem('isloggedIn') == 'true'){
                  this.isloggedIn = true
                }
              }

  // login(email:string, pass:string){
  //   // ref https://blog.angular-university.io/angular-jwt-authentication/

  //   if(email == 'admin@admin.com' && pass == 'admin'){
  //     this.isloggedIn = true
  //     localStorage.setItem('isloggedIn', 'true');
  //     localStorage.setItem('email', email);
  //     return 'loggedIn'
  //   }  else {
  //     return 'notloggedIN'
  //   }
  // }

  login(email:string, password:string ) {
    return this.http.post('http://127.0.0.1:5000/login', {email, password})
  }

  signup(email:string, password:string, firstName:string, lastName:string, phoneNumber:string, cellphoneNumber:string,
    streetAddress:string, city:string, state: string, zipCode:string) {
    return this.http.post('http://127.0.0.1:5000/register', {email, password, firstName, lastName, phoneNumber, cellphoneNumber,
    streetAddress, city, state, zipCode})
  }

  isAuthenticated(){
    return this.isloggedIn;
  }

  logout(){
    localStorage.setItem('isloggedIn', 'false');
    localStorage.removeItem('email');
    localStorage.removeItem('token');
    alert("You have been succesfully logged out");
    this.router.navigateByUrl("/homepage");
  }

  // private setSession(authResult) {
  //   const expiresAt = moment().add(authResult.expiresIn,'second');

  //   localStorage.setItem('id_token', authResult.idToken);
  //   localStorage.setItem("expires_at", JSON.stringify(expiresAt.valueOf()) );
  // }  

}
