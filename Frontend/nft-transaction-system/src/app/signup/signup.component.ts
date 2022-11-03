import { Component, OnInit } from '@angular/core';
import { FormControl,FormGroup,Validators,FormBuilder } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from './../auth.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent implements OnInit {
  cstatus = 'None'
  registerForm:any = FormGroup;
  submitted = false;
  wrongPassword = false;
  constructor(private formBuilder: FormBuilder,
              private authService: AuthService,
              private router: Router) { }
  
  get f() { return this.registerForm.controls; }

  ngOnInit(): void {
    if(localStorage.getItem('isloggedIn') == 'true'){
      this.router.navigateByUrl('/')
    }
    this.registerForm = this.formBuilder.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required]],
      firstName: ['', [Validators.required]],
      lastName: ['', [Validators.required]],
      phoneNumber: ['', [Validators.required, Validators.pattern("[0-9 ]{10}")]],
      cellphoneNumber: ['', [Validators.required, Validators.pattern("[0-9 ]{10}")]],
      streetAddress: ['', [Validators.required]],
      city: ['', [Validators.required]],
      state: ['', [Validators.required]],
      zipCode: ['', [Validators.required, Validators.pattern("[0-9 ]{5}")]],
      });
  }

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
      if(this.cstatus != 'loggedIn'){
        this.wrongPassword = true;
        return;
      }
      this.ngOnInit()
      alert("Great!!");
    }
   
  }

}
