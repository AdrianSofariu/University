function fetchByGenre() {
  const genre = document.getElementById("genre").value;
  fetch("api/get_files.php?genre=" + encodeURIComponent(genre))
    .then((res) => res.json())
    .then((response) => {
      // Check if the response is successful
      if (response.success) {
        const list = document.getElementById("fileList");
        list.innerHTML = ""; // Clear the list before adding new items

        // Add the fetched items to the list
        response.data.forEach((item) => {
          const li = document.createElement("li");

          // Create a container for the title and format
          const fileInfo = document.createElement("div");
          fileInfo.classList.add("file-info");
          fileInfo.textContent = `${item.title} (${item.format})`;

          // Create a container for the actions (Details, Edit and Delete)
          const fileActions = document.createElement("div");
          fileActions.classList.add("file-actions");
          fileActions.innerHTML = `
            <a href="pages/file_details.php?id=${item.id}">Details</a> |
            <a href="pages/update_form.php?id=${item.id}">Edit</a> |
            <a href="pages/delete_form.php?id=${item.id}">Delete</a>
          `;

          // Append the content to the list item
          li.appendChild(fileInfo);
          li.appendChild(fileActions);
          list.appendChild(li);
        });

        // Update the previous filter display
        document.getElementById("prevFilter").textContent =
          document.getElementById("currentFilter").textContent;

        // Update the last filter display
        document.getElementById("currentFilter").textContent = genre
          ? `${genre}`
          : "All Genres";
      } else {
        console.error(
          "Error fetching files:",
          response.error || "Unknown error"
        );
      }
    })
    .catch((err) => console.error("Error fetching data:", err));
}

function fetchGenres() {
  fetch("api/get_genres.php")
    .then((res) => res.json())
    .then((response) => {
      if (response.success) {
        // If the response is successful, handle the genres data
        const genreSelect = document.getElementById("genre");
        response.data.forEach((genreObj) => {
          const option = document.createElement("option");
          option.value = genreObj.genre; // genreObj.genre is the genre name
          option.textContent = genreObj.genre; // Display genre name
          genreSelect.appendChild(option);
        });
      } else {
        // If the response is unsuccessful, log the errors
        console.error(
          "Error fetching genres:",
          response.errors || "Unknown error"
        );
      }
    })
    .catch((err) => console.error("Error fetching genres:", err));
}

// Fetch all records when the page loads if no genre is selected
document.addEventListener("DOMContentLoaded", function () {
  fetchGenres(); // Calls the function to populate genres
  fetchByGenre(); // Calls the function to load the data
});
