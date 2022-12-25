<?php
  // Store the username and password in variables
  $username = "admin";
  $password = "apar";

  // Get the submitted username and password
  $submittedUsername = $_POST["username"];
  $submittedPassword = $_POST["password"];

  // Check if the submitted username and password match the stored values
  if ($submittedUsername === $username && $submittedPassword === $password) {
    // Set a session variable to indicate that the user is logged in
    session_start();
    $_SESSION["loggedIn"] = true;

    // Redirect to the CGPA calculator page
    header("Location: cgpa.html");
  } else {
    // Show an error message
    echo "Incorrect username or password";
  }
?>
