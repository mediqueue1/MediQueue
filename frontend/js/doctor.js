document.addEventListener('DOMContentLoaded', () => {
    // Global variable to track the active patient
    let currentPatient = null;

    // --- BUTTONS ---
    const completeBtn = document.getElementById('completeBtn');
    const nextBtn = document.getElementById('nextPatientBtn');

    // --- QUEUE MANAGEMENT FUNCTIONS ---
    async function callNextPatient() {
        const userData = JSON.parse(localStorage.getItem("userData"));
        const doctorId = userData?.user?.doctor_id;

        console.log("FULL USER DATA:", userData);
        console.log("DOCTOR ID:", doctorId);

        if (!doctorId) {
            alert("Doctor session not found.");
            return;
        }

        try {
            const res = await fetch(`https://mediqueue-api-qsnu.onrender.com/api/queue/next/${doctorId}`);
            const data = await res.json();

            if (!data.patient) {
                alert("No patients waiting in queue.");

                document.getElementById("patientName").innerText = "No Patient";
                document.getElementById("patientMeta").innerText = "Waiting for next patient...";
                return;
            }

            currentPatient = data.patient;

            // Update UI
            document.getElementById("patientName").innerText =
            currentPatient.full_name;

            document.getElementById("patientMeta").innerText =
                `Token #${currentPatient.token_number}`;

            // RESET COMPLETE BUTTON (IMPORTANT FIX)
            if (completeBtn) {
                completeBtn.innerHTML = "Complete";
                completeBtn.disabled = false;
                completeBtn.style.background = "";
            }

        } catch (err) {
            console.error("Error fetching next patient:", err);
        }
    }

    async function completePatient() {
        if (!currentPatient) {
            alert("No active patient to complete.");
            return;
        }

        if (confirm("Confirm: Consultation is finished?")) {
            try {
                await fetch(`https://mediqueue-api-qsnu.onrender.com/api/queue/complete/${currentPatient.appointment_id}`, {
                    method: "PUT"
                });

                alert("Consultation completed!");

                // Reset UI
                document.getElementById("patientName").innerText = "No Patient";
                document.getElementById("patientMeta").innerText = "Waiting for next patient...";

                // Visual feedback for the button
                if (completeBtn) {
                    completeBtn.innerHTML = "✓ Completed";
                    completeBtn.style.background = "#05cd99";
                    completeBtn.disabled = true;
                }

                currentPatient = null;

            } catch (err) {
                console.error("Error completing patient:", err);
            }
        }
    }

    // Attach new event listeners
    if (nextBtn) nextBtn.addEventListener('click', callNextPatient);
    if (completeBtn) completeBtn.addEventListener('click', completePatient);

    // --- SIDEBAR ACTIVE ---
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            navLinks.forEach(l => l.classList.remove('active'));
            this.classList.add('active');
        });
    });

    // --- NAVIGATION ---
    const DoctorsBtn = document.getElementById('DoctorsBtn');
    if (DoctorsBtn) {
        DoctorsBtn.addEventListener('click', (e) => { e.preventDefault(); window.location.href = 'doctors.html'; });
    }

    const QueuedBtn = document.getElementById('QueuedBtn');
    if (QueuedBtn) {
        QueuedBtn.addEventListener('click', (e) => { e.preventDefault(); window.location.href = 'queued.html'; });
    }

    const ScheduledBtn = document.getElementById('ScheduledBtn');
    if (ScheduledBtn) {
        ScheduledBtn.addEventListener('click', (e) => { e.preventDefault(); window.location.href = 'scheduled.html'; });
    }

    const DoctordBtn = document.getElementById('DoctordBtn');
    if (DoctordBtn) {
        DoctordBtn.addEventListener('click', (e) => { e.preventDefault(); window.location.href = 'Doctord.html'; });
    }

    // --- LOGOUT ---
    const logoutBtn = document.getElementById('logoutBtn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', (e) => {
            e.preventDefault();
            if(confirm("Are you sure you want to logout?")) {
                localStorage.removeItem('userData');
                localStorage.removeItem('role');
                window.location.href = "login.html";
            }
        });
    }

    // --- DYNAMIC DOCTOR NAME ---
    const userData = JSON.parse(localStorage.getItem("userData"));

    if (userData && userData.user) {
        const doctor = userData.user;
        const name = doctor.first_name 
            ? `${doctor.first_name} ${doctor.middle_name ? doctor.middle_name + " " : ""}${doctor.last_name}`
            : doctor.name || "Doctor";

        const welcomeText = document.getElementById("welcomeText");
        if (welcomeText) {
            welcomeText.innerHTML = `Welcome back, Dr. ${name}.`;
        }
    } else {
        window.location.href = "login.html";
    }
});