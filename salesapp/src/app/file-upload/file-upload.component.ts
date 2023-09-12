import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { HttpClient, HttpClientJsonpModule } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-file-upload',
  templateUrl: './file-upload.component.html',
  styleUrls: ['./file-upload.component.css']
})
export class FileUploadComponent implements OnInit {

  @ViewChild('fileSelect') myInputVariable?: ElementRef;

  filename: any;
  format: any;
  formfile: any;
  file:any;
  showLoader: boolean = false;

  constructor(
    private http: HttpClient,
    private router:Router
  ) { }

  ngOnInit(): void {
  }
  onFileSelect(event: any) {
    try {
       this.file = event.target.files[0];
      if (this.file) {
        this.filename = this.file.name;
        this.format = this.file.name.split('.');
        if (this.format[1] != 'csv') {
          this.deleteFile();
        } else {
          this.formfile = new FormData();
          this.formfile.append('file', this.file);
        }
      }
    } catch (error) {
      this.deleteFile();
      console.log('no file was selected...');
    }
  }

  fileUpload() {
    if (this.file) {
      this.showLoader = true;
      let url = "http://localhost:5000/api/file_upload"
      this.http.post(url, this.formfile).subscribe((res:any) => {
        alert(res.statusMessage)
        this.showLoader = false;
      },
        (error) => {
          this.showLoader = false;
        });
    }else{
      alert("Please upload file")
    }
  }
  getdata(){
    this.router.navigateByUrl('dashboard')
  }
  deleteFile(){
    this.file = null;
    this.format = null;
    this.filename = null;
    this.formfile.delete('file');
  }
}



