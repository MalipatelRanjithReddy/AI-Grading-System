// Handle Login
document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("loginForm");
  if (loginForm) {
    loginForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const role = document.getElementById("role").value;

      // Redirect based on role
      if (role === "teacher") {
        window.location.href = "teacher_dashboard.html";
      } else {
        window.location.href = "student_dashboard.html";
      }
    });
  }

  // Handle Student Upload
  const uploadForm = document.getElementById("uploadForm");
  if (uploadForm) {
    uploadForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const file = document.getElementById("assignmentFile").files[0];
      if (file) {
        alert("Assignment uploaded successfully!");
        // TODO: Send file to backend using fetch API
      }
    });
  }
});

// Logout Function
function logout() {
  window.location.href = "index.html";
}
