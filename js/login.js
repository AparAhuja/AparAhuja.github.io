// Validate the form submission
function validateForm() {
  // Get the username and password
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;

  // Check if the username and password are correct
  if (username === "apar" && password === "apar") {

    // Redirect to the CGPA calculator page
    window.location.href = "cgpa.html";

    // Prevent the form from being submitted
    return false;
  } else {
    // Show an error message
    alert("Incorrect username or password");

    // Prevent the form from being submitted
    return false;
  }
}
