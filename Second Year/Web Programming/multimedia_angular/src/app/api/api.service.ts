import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'; // Import HttpClient
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root', // This ensures that the service is available throughout the app
})
export class ApiService {
  private apiUrl = 'http://localhost/multimedia_app/api'; // Replace with your API URL

  constructor(private http: HttpClient) {} // Inject HttpClient in the constructor

  // Function to fetch genres
  getGenres(): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/get_genres.php`);
  }

  // Function to fetch files by genre
  getFilesByGenre(genre: string): Observable<any> {
    const genreParam = genre ? `?genre=${encodeURIComponent(genre)}` : '';
    return this.http.get<any>(`${this.apiUrl}/get_files.php${genreParam}`);
  }

  // Function to get a file by ID
  getFileById(id: string): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/get_file.php?id=${id}`);
  }

  // Function to add a new file
  addFile(fileData: {
    title: string;
    format: string;
    genre: string;
    path: string;
  }): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/add_file.php`, fileData);
  }

  // Function to delete a file by ID
  deleteFile(id: number): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}/delete_file.php?id=${id}`);
  }

  // Function to update a file
  updateFile(data: any): Observable<any> {
    return this.http.patch<any>(`${this.apiUrl}/update_file.php`, data);
  }
}
