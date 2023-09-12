import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { FileUploadComponent } from './file-upload/file-upload.component';
import { LoginComponent } from './login/login.component';
import { VisualizeComponent } from './visualize/visualize.component';

const routes: Routes = [

  {path: '', component: LoginComponent},
  {path: 'file-upload', component: FileUploadComponent},
  {path: 'dashboard', component: DashboardComponent},
  {path: 'visualize', component: VisualizeComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
