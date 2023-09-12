import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  templist: any=[];
  showcomment: boolean = false;
    constructor(private http:HttpClient,private  router: Router) { }
    ngOnInit(): void {
      let url = "http://localhost:5000/api/get_data"
          this.http.get<any>(url).subscribe((data) => {
              this.templist = data;  
            });
    }
  method(){
    this.showcomment=!this.showcomment;
  }
  visualize(){
    this.router.navigateByUrl("visualize");
  }
  }


