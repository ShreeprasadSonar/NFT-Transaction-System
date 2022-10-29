import { Router } from '@angular/router';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

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

  login(email:string, pass:string){
    // ref https://blog.angular-university.io/angular-jwt-authentication/

    if(email == 'admin@admin.com' && pass == 'admin'){
      this.isloggedIn = true
      localStorage.setItem('isloggedIn', 'true');
      localStorage.setItem('email', email);
      return 'loggedIn'
    }  else {
      return 'notloggedIN'
    }
  }

  isAuthenticated(){
    return this.isloggedIn;
  }

  logout(){
    localStorage.setItem('isloggedIn', 'false');
    localStorage.removeItem('email');
    alert("You have been succesfully logged out");
    this.router.navigateByUrl("/homepage");
  }

  // private setSession(authResult) {
  //   const expiresAt = moment().add(authResult.expiresIn,'second');

  //   localStorage.setItem('id_token', authResult.idToken);
  //   localStorage.setItem("expires_at", JSON.stringify(expiresAt.valueOf()) );
  // }  

}
