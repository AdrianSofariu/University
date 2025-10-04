<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Error</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f0f2f5;
      color: #333;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      margin: 0;
    }
    .container {
      background-color: #fff;
      padding: 40px;
      border-radius: 10px;
      box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
      text-align: center;
      max-width: 400px;
      width: 90%;
    }
    h1 {
      color: #dc3545; /* Red for error */
      margin-bottom: 20px;
    }
    p {
      margin-bottom: 15px;
      line-height: 1.6;
    }
    .nav-links a {
      display: inline-block;
      background-color: #007bff;
      color: white;
      padding: 10px 20px;
      margin: 0 10px;
      border-radius: 5px;
      text-decoration: none;
      transition: background-color 0.3s ease;
    }
    .nav-links a:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
<div class="container">
  <h1>Oops!</h1>
  <p>Something went wrong. We are working to fix the problem.</p>
  <p>Please try again or navigate to a different page.</p>
  <div class="nav-links">
    <a href="dashboard">Go to Dashboard</a>
    <a href="login.jsp">Go to Login Page</a>
  </div>
</div>
</body>
</html>