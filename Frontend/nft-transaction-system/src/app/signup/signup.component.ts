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
  response:any;
  constructor(private formBuilder: FormBuilder,
              private authService: AuthService,
              private router: Router) { }
  
  get f() { return this.registerForm.controls; }

  ngOnInit(): void {
    if(localStorage.getItem('isloggedIn') == 'true'){
      this.router.navigateByUrl('/')
    }
    this.registerForm = this.formBuilder.group({
      email: ['', [Validators.required, Validators.email, Validators.maxLength(50)]],
      password: ['', [Validators.required, Validators.maxLength(50)]],
      firstName: ['', [Validators.required, Validators.maxLength(25)]],
      lastName: ['', [Validators.required, Validators.maxLength(25)]],
      phoneNumber: ['', [Validators.required, Validators.pattern("[0-9 ]{10}")]],
      cellphoneNumber: ['', [Validators.required, Validators.pattern("[0-9 ]{10}")]],
      streetAddress: ['', [Validators.required, Validators.maxLength(50)]],
      city: ['', [Validators.required, Validators.maxLength(10)]],
      state: ['', [Validators.required, Validators.maxLength(10)]],
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
      this.authService.signup(this.registerForm.value.email,
                              this.registerForm.value.password,
                              this.registerForm.value.firstName,
                              this.registerForm.value.lastName,
                              this.registerForm.value.phoneNumber,
                              this.registerForm.value.cellphoneNumber,
                              this.registerForm.value.streetAddress,
                              this.registerForm.value.city,
                              this.registerForm.value.state,
                              this.registerForm.value.zipCode,
                              )
            .subscribe(
                res => {
                    this.response = res;
                    console.log(this.response);
                    alert("Signup Succesful");
                    this.router.navigateByUrl('/');
                }
            );
    }
   
  }

}
