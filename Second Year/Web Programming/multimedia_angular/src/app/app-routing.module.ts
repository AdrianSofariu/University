import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MainpageComponent } from './mainpage/mainpage.component';
import { FileDetailsComponent } from './file-details/file-details.component';
import { EditFileComponent } from './edit-file/edit-file.component';
import { AddFileComponent } from './add-file/add-file.component';
import { DeleteFileComponent } from './delete-file/delete-file.component';

const routes: Routes = [
  { path: '', component: MainpageComponent },
  { path: 'details/:id', component: FileDetailsComponent },
  { path: 'edit/:id', component: EditFileComponent },
  { path: 'delete/:id', component: DeleteFileComponent },
  { path: 'add', component: AddFileComponent },
  { path: '**', redirectTo: '' }, // catch-all
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
