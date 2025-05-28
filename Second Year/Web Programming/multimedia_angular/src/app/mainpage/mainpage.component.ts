import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api/api.service'; // Import the ApiService

@Component({
  selector: 'app-mainpage',
  standalone: false,
  templateUrl: './mainpage.component.html',
  styleUrl: './mainpage.component.css',
})
export class MainpageComponent implements OnInit {
  genres: string[] = [];
  files: any[] = [];
  currentFilter: string = 'All Genres';
  prevFilter: string = '--';

  constructor(private apiService: ApiService) {} // Inject ApiService

  ngOnInit() {
    this.loadGenres();
    this.loadFiles();
  }

  loadGenres() {
    this.apiService.getGenres().subscribe(
      (response) => {
        if (response.success) {
          this.genres = response.data.map((genreObj: any) => genreObj.genre);
        } else {
          console.error('Error fetching genres:', response.error);
        }
      },
      (error) => console.error('Error fetching genres:', error)
    );
  }

  loadFiles(genre: string = '') {
    this.apiService.getFilesByGenre(genre).subscribe(
      (response) => {
        if (response.success) {
          this.files = response.data;
          this.prevFilter = this.currentFilter;
          this.currentFilter = genre ? genre : 'All Genres';
        } else {
          console.error('Error fetching files:', response.error);
        }
      },
      (error) => console.error('Error fetching files:', error)
    );
  }

  onGenreChange(event: Event) {
    const target = event.target as HTMLSelectElement; // Type casting the event target
    const genre = target.value;
    this.loadFiles(genre);
  }
}
