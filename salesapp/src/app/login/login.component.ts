import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { User } from '../classModels/User';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  user :User = new User();


  constructor(private  router: Router) { }
  ngOnInit(): void {
  }

  Onsubmit(){
    if(this.user.userName==="mahii" && this.user.userPassword==="12345"){
      alert("Login Successfull")
      this.router.navigateByUrl("file-upload")
    }
    else{
      alert("Wrong Credintials");
    }
  }
}
