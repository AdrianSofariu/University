import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from '../api/api.service';

@Component({
  selector: 'app-add-file',
  standalone: false,
  templateUrl: './add-file.component.html',
  styleUrls: ['./add-file.component.css'],
})
export class AddFileComponent {
  title = '';
  format = '';
  genre = '';
  path = '';
  errorMessage = '';
  successMessage = '';

  constructor(private api: ApiService, private router: Router) {}

  onSubmit(): void {
    this.errorMessage = '';
    this.successMessage = '';

    if (!this.title || !this.format || !this.genre || !this.path) {
      this.errorMessage = 'All fields are required.';
      return;
    }

    this.api
      .addFile({
        title: this.title,
        format: this.format,
        genre: this.genre,
        path: this.path,
      })
      .subscribe({
        next: (res) => {
          if (res.success) {
            this.successMessage = res.message;
            alert(this.successMessage);
            setTimeout(() => this.router.navigate(['/']), 1500);
          } else {
            this.errorMessage =
              res.errors?.join('\n') || res.error || 'Failed to add file.';
          }
        },
        error: (err) => {
          this.errorMessage = err.message || 'Server error.';
          alert(this.errorMessage);
        },
      });
  }
}
