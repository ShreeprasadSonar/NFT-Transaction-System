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
  message:string = "";

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
      if (this.registerForm.value.email && this.registerForm.value.password && this.registerForm.value.type) {
        this.authService.login(this.registerForm.value.email, this.registerForm.value.password, this.registerForm.value.type)
            .subscribe(
                res => {
                    this.response = res
                    console.log(this.response)
                    if(this.response.status != 'fail'){
                      localStorage.setItem('isloggedIn', 'true');
                      localStorage.setItem('token', this.response.token);
                      localStorage.setItem('type', this.response.type);
                      localStorage.setItem('email', this.response.email);
                      localStorage.setItem('name', this.response.name);
                      localStorage.setItem('id', this.response.id);
                      if(this.registerForm.value.type == 'Manager'){
                        this.router.navigateByUrl('/manager-dashboard');
                      } else{
                        this.router.navigateByUrl('/dashboard');
                      }
                      alert("Great!!");
                      
                    } else {
                      this.message = this.response.message
                      this.wrongPassword = true;
                      console.log("User is not logged in");
                    }
                },
                error =>{
                  this.message = "Error while logging in"
                  this.wrongPassword = true;
                  console.log("User is not logged in");
                }
            );
      }
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
