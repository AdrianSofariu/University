import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ApiService } from '../api/api.service';

@Component({
  selector: 'app-delete-file',
  standalone: false,
  templateUrl: './delete-file.component.html',
  styleUrls: ['./delete-file.component.css'],
})
export class DeleteFileComponent implements OnInit {
  fileId!: number;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private apiService: ApiService
  ) {}

  ngOnInit(): void {
    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.fileId = +id;
    } else {
      alert('No file ID provided.');
      this.router.navigate(['/']);
    }
  }

  onDelete(): void {
    this.apiService.deleteFile(this.fileId).subscribe({
      next: (res) => {
        if (res.success) {
          alert(res.message);
          this.router.navigate(['/']);
        } else {
          alert(res.message);
        }
      },
      error: (err) => {
        alert('Error: ' + err.message);
      },
    });
  }
}
