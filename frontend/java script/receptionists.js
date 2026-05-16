document.addEventListener('DOMContentLoaded', () => {
    
    // Complete Visit Interaction
    const completeVisitBtn = document.getElementById('completeVisitBtn');
    if(completeVisitBtn) {
        completeVisitBtn.addEventListener('click', () => {
            const confirmed = confirm("Mark Token #242 (Jonathan Sterling) as completed?");
            if (confirmed) {
                completeVisitBtn.innerHTML = "Completed ✓";
                completeVisitBtn.style.backgroundColor = "#22c55e"; // Success green
                completeVisitBtn.disabled = true;
            }
        });
    }

    // Push Notification Alert
    const sendAlertBtn = document.getElementById('sendAlertBtn');
    if(sendAlertBtn) {
        sendAlertBtn.addEventListener('click', () => {
            const selectBox = document.querySelector('.msg-select');
            const message = selectBox.value;
            alert(`Push Notification Sent!\n\nMessage: "${message}"\nSent to: All waiting patients.`);
        });
    }

    // Logout Functionality
    const logoutBtn = document.getElementById('logoutBtn');
    if(logoutBtn) {
        logoutBtn.addEventListener('click', (e) => {
            e.preventDefault();
            if(confirm("Are you sure you want to log out?")) {
                window.location.href = "login.html";
            }
        });
    }
});

document.addEventListener("DOMContentLoaded", () => {

    const data = JSON.parse(localStorage.getItem("receptionistData"));

    if (!data) {
        document.getElementById("receptionistName").innerText = "Guest";
        return;
    }

    // 🔥 IMPORTANT: depends on backend response
    const r = data.receptionist || data.user || data;

    const fullName = [
        r.first_name,
        r.middle_name,
        r.last_name
    ].filter(Boolean).join(" ");

    document.getElementById("receptionistName").innerText = fullName || "Guest";

});

async function loadNowServing() {
    try {
        const res = await fetch("https://mediqueue-api-qsnu.onrender.com/api/now_serving");
        const result = await res.json();

        if (result.success && result.data.length > 0) {
            const current = result.data[0]; // first active patient

            document.getElementById("doctorName").innerText =
                "Dr. " + current.first_name + " " + current.last_name;

            document.getElementById("doctorSpecialization").innerText =
                current.specialization;

            document.getElementById("tokenNumber").innerText =
                "Token #" + current.token_number;

            document.getElementById("patientName").innerText =
                current.full_name;

            document.getElementById("patientInfo").innerText =
                "In Consultation";
        } else {
            document.getElementById("tokenNumber").innerText = "No Active Patient";
        }

    } catch (err) {
        console.error("Now Serving Error:", err);
    }
}

// Call once + auto refresh
loadNowServing();
setInterval(loadNowServing, 5000);