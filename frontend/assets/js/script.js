function showForm() {
    const role = document.getElementById("role-select").value;

    // Hide both forms initially
    document.getElementById("teacher-form").style.display = "none";
    document.getElementById("student-form").style.display = "none";

    // Show the form based on the selected role
    if (role === "teacher") {
        document.getElementById("teacher-form").style.display = "block";
    } else if (role === "student") {
        document.getElementById("student-form").style.display = "block";
    }
}
