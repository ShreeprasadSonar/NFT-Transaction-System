import { AuthService } from './../auth.service';
import { Component, OnInit } from '@angular/core';
import { FormControl,FormGroup,Validators,FormBuilder } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  cstatus = 'None'
  registerForm:any = FormGroup;
  submitted = false;
  wrongPassword = false;
  response:any;

  constructor(private formBuilder: FormBuilder,
              private authService: AuthService,
              private router: Router) { }
  get f() { return this.registerForm.controls; }

  onSubmit() {
    this.submitted = true;
    // stop here if form is invalid
    if (this.registerForm.invalid) {
        return;
    }
    //True if all the fields are filled
    if(this.submitted)
    {
      // this.authService.login(this.registerForm.value.email, this.registerForm.value.password).subscribe(() => {
      //                   console.log("User is logged in");
      //                   this.router.navigateByUrl('/');
      //               }
      //           );
      // this.cstatus = this.authService.login(this.registerForm.value.email, this.registerForm.value.password)
      if (this.registerForm.value.email && this.registerForm.value.password && this.registerForm.value.type) {
        this.authService.login(this.registerForm.value.email, this.registerForm.value.password, this.registerForm.value.type)
            .subscribe(
                res => {
                    this.response = res
                    console.log("User is logged in");
                    localStorage.setItem('isloggedIn', 'true');
                    localStorage.setItem('token', this.response.auth_token);
                    localStorage.setItem('email', this.registerForm.value.email);
                    this.router.navigateByUrl('/dashboard');
                }
            );
    }
      if(this.cstatus != 'loggedIn'){
        this.wrongPassword = true;
        return;
      }
      this.ngOnInit()
      alert("Great!!");
    }
   
  }

  ngOnInit(): void {

    if(localStorage.getItem('isloggedIn') == 'true'){
      this.router.navigateByUrl('/')
    }
    this.registerForm = this.formBuilder.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required]],
      type: ['', [Validators.required]]
      });
  }

}
