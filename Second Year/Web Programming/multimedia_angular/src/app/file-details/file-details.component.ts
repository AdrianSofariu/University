import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../api/api.service';

@Component({
  selector: 'app-file-details',
  standalone: false,
  templateUrl: './file-details.component.html',
  styleUrl: './file-details.component.css',
})
export class FileDetailsComponent implements OnInit {
  fileId!: string;
  fileData: any;
  errorMessage = '';

  constructor(private route: ActivatedRoute, private api: ApiService) {}

  ngOnInit(): void {
    this.fileId = this.route.snapshot.paramMap.get('id') || '';
    if (!this.fileId) {
      this.errorMessage = 'Missing file ID';
      return;
    }

    this.api.getFileById(this.fileId).subscribe({
      next: (response) => {
        if (response.success) {
          this.fileData = response.file;
        } else {
          this.errorMessage = response.error || 'Unknown error';
        }
      },
      error: (err) => {
        this.errorMessage = err.message || 'Error fetching file details';
      },
    });
  }
}
