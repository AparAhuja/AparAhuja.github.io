// Keep track of the number of courses
var numCourses = 1;

// Add a new course row to the table
function addCourse() {
  numCourses++;
  var table = document.getElementById("courses");
  var row = table.insertRow(-1);
  var cell1 = row.insertCell(0);
  var cell2 = row.insertCell(1);
  var cell3 = row.insertCell(2);
  cell1.innerHTML = "Course " + numCourses;
  cell2.innerHTML = "<input type='text' class='credits' value='4'>";
  cell3.innerHTML = "<input type='text' class='grade'>";
}

// Calculate the CGPA
function calculateCGPA() {
  // Initialize the total number of credits and GPA
  var totalCredits = 0;
  var totalGPA = 0;
  
  // Get the values of the input fields
  var creditsElements = document.getElementsByClassName("credits");
  var gradeElements = document.getElementsByClassName("grade");
  for (var i = 0; i < numCourses; i++) {
    totalCredits += parseInt(creditsElements[i].value);
    totalGPA += parseInt(creditsElements[i].value) * parseFloat(gradeElements[i].value);
  }
  
  // Calculate the CGPA
  var cgpa = totalGPA / totalCredits;
  
  // Display the result
  document.getElementById("result").innerHTML = "Your CGPA is: " + cgpa.toFixed(2);
}
