import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ApiService } from '../api/api.service';

@Component({
  selector: 'app-edit-file',
  standalone: false,
  templateUrl: './edit-file.component.html',
  styleUrls: ['./edit-file.component.css'],
})
export class EditFileComponent implements OnInit {
  fileId: string | null = null;
  title: string = '';
  format: string = '';
  genre: string = '';
  path: string = '';

  constructor(
    private route: ActivatedRoute,
    private apiService: ApiService, // Inject ApiService
    private router: Router
  ) {}

  ngOnInit(): void {
    // Get the 'id' from the URL
    this.route.paramMap.subscribe((params) => {
      this.fileId = params.get('id');
      if (this.fileId) {
        this.loadFileData();
      }
    });
  }

  // Method to fetch file data
  loadFileData() {
    this.apiService.getFileById(this.fileId!).subscribe(
      (response) => {
        if (response.success) {
          this.title = response.file.title;
          this.format = response.file.format;
          this.genre = response.file.genre;
          this.path = response.file.path;
        } else {
          alert('Error: ' + response.error);
        }
      },
      (error) => {
        alert('Error fetching file data');
      }
    );
  }

  // Method to update the file
  updateFile() {
    const formData = {
      id: this.fileId,
      title: this.title,
      format: this.format,
      genre: this.genre,
      path: this.path,
    };

    this.apiService.updateFile(formData).subscribe(
      (response) => {
        if (response.success) {
          alert(response.message); // Success message
          this.router.navigate(['/']); // Redirect after success
        } else {
          alert('Error: ' + response.errors.join('\n')); // Show error messages
        }
      },
      (error) => {
        alert('Error updating file');
      }
    );
  }
}
