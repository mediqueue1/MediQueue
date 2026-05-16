document.addEventListener('DOMContentLoaded', () => {

    // 1. Get the data saved in login.js
    const adminDataString = localStorage.getItem('adminData');
    const userRole = localStorage.getItem('role');

    // 2. Security: If not logged in as Admin, send back to login page
    if (!adminDataString || userRole !== 'Admin') {
        window.location.href = 'login.html';
        return;
    }

    const adminData = JSON.parse(adminDataString);

    // 3. Display the name (fixes the "Guest" issue)
    const adminNameDisplay = document.getElementById('adminName');
    if (adminNameDisplay) {
        adminNameDisplay.innerText = adminData.name || "Administrator";
    }
    // Logout functionality
    const logoutBtn = document.getElementById('logoutBtn');
    logoutBtn.addEventListener('click', (e) => {
        e.preventDefault();
        if(confirm("Are you sure you want to logout?")) {
            window.location.href = "login.html"; // Redirects back to login
        }
    });

    // Simple interaction for table rows
    const rows = document.querySelectorAll('tbody tr');
    rows.forEach(row => {
        row.addEventListener('mouseenter', () => {
            row.style.backgroundColor = "#f4f7fe";
        });
        row.addEventListener('mouseleave', () => {
            row.style.backgroundColor = "transparent";
        });
    });

    console.log("Admin Dashboard Loaded Successfully");
});

// get no. of patients and doctors
async function loadCounts() {
  const res = await fetch("http://127.0.0.1:5000/api/admin/counts");
  const data = await res.json();

  document.getElementById("doctorCount").innerText = data.total_doctors;
  document.getElementById("patientCount").innerText = data.total_patients;
  document.getElementById("todayAppointments").innerText = data.today_appointments;
}

loadCounts();

// Load admin name
// async function loadAdminName() {
//   try {
//     const res = await fetch("http://127.0.0.1:5000/api/admin/dashboard", {
//       method: "GET",
//       credentials: "include"  // 🔥 MUST
//     });

//     const data = await res.json();

//     if (!res.ok) {
//       document.getElementById("adminName").innerText = "Guest";
//       return;
//     }

//     document.getElementById("adminName").innerText = data.name;

//   } catch (err) {
//     console.log(err);
//     document.getElementById("adminName").innerText = "Error";
//   }
// }

// loadAdminName();