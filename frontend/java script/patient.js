document.addEventListener('DOMContentLoaded', () => {

    const userDataString = localStorage.getItem('userData');
    const userRole = localStorage.getItem('role');

    if (!userDataString || userRole !== 'Patient') {
        window.location.href = 'login.html';
        return;
    }

    const data = JSON.parse(userDataString);
    const patient = data.user || data || {};
    const welcomeHeader = document.getElementById('welcomeName');

if (welcomeHeader) {
    const name =
        patient.first_name ||
        patient.name ||
        "Patient";

    welcomeHeader.textContent = `Welcome back, ${name}`;
}

    // ============================
    // TODAY DATE
    // ============================
    const dateElement = document.getElementById("currentDateDisplay");

    if (dateElement) {
        const today = new Date();
        dateElement.textContent = today.toLocaleDateString('en-IN', {
            weekday: 'long',
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
    }

    let selectedDoctorId = null;

    // ============================
    // INITIAL QUEUE CALLS
    // ============================
    setTimeout(() => {
        updateQueueStatus(patient.patient_id);
        updateAllQueueStatus(patient.patient_id);
    }, 300);

    setInterval(() => {
        updateQueueStatus(patient.patient_id);
        updateAllQueueStatus(patient.patient_id);
    }, 5000);

    // ============================
    // MULTIPLE QUEUE STATUS
    // ============================
    async function updateAllQueueStatus(patientId) {
        try {
            const response = await fetch(`http://127.0.0.1:5000/api/queue_status_all/${patientId}`);
            const resData = await response.json();

            const container = document.getElementById("queueList");
            const queueBox = document.getElementById("queue");
            const waitingTextElement = document.getElementById("waitingText");

            if (!container) return;

            container.innerHTML = "";
            let combinedText = "";

            if (resData.success && resData.appointments.length > 0) {

                resData.appointments.forEach(item => {

                    if (item.status === "completed") return;

                    const ahead = item.ahead ?? item.tokens_ahead ?? 0;

                    let message = "";

                    if (ahead === 0) message = "You are next!";
                    else if (ahead === 1) message = "1 patient ahead of you";
                    else message = ahead + " patients ahead of you";

                    if (item.waiting_time != null) {
                        const safeTime = Math.max(0, Math.round(item.waiting_time));
                        message += ` (Approx ${safeTime} min)`;

                        if (waitingTextElement) {
                            waitingTextElement.innerHTML =
                                `⏳ Estimated waiting time: <b>${safeTime} min</b>`;
                        }
                    }

                    container.innerHTML += `
                        <div class="queue-card">
                            <h3>Token: A-${item.token_number}</h3>
                            <p>${message}</p>
                        </div>
                    `;

                    combinedText += `A-${item.token_number}: ${message}\n`;
                });

                if (queueBox) queueBox.textContent = combinedText;

            } else {
                container.innerHTML = "<p>No appointments today</p>";
                if (queueBox) queueBox.textContent = "No appointments today";
            }

        } catch (error) {
            console.error("Queue fetch error:", error);
        }
    }

    // ============================
    // SINGLE QUEUE STATUS
    // ============================
    async function updateQueueStatus(patientId) {
        try {
            const response = await fetch(`http://127.0.0.1:5000/api/queue_status/${patientId}`);
            const resData = await response.json();

            if (resData.success) {

                const tokenEl = document.getElementById('token');
                const queueEl = document.getElementById('queue');
                const waitingTextElement = document.getElementById("waitingText");
                const welcomeHeader = document.getElementById('welcomeName');

                // const name =
                //     patient.first_name ||
                //     resData.first_name ||
                //     data.first_name ||
                //     "Patient";

                // if (welcomeHeader) {
                //     welcomeHeader.textContent = `Welcome back, ${name}`;
                // }

                if (tokenEl) {
                    tokenEl.textContent = "A-" + resData.user_token;
                }

                let message = "";

                if (resData.tokens_ahead === 0) message = "You are next!";
                else if (resData.tokens_ahead === 1) message = "1 patient ahead of you";
                else message = resData.tokens_ahead + " patients ahead of you";

                if (resData.waiting_time != null) {
                    const safeTime = Math.max(0, Math.round(resData.waiting_time));
                    message += ` (Approx wait: ${safeTime} min)`;

                    if (waitingTextElement) {
                        waitingTextElement.innerHTML =
                            `⏳ Estimated waiting time: <b>${safeTime} min</b>`;
                    }
                }

                if (queueEl) queueEl.textContent = message;
            }

        } catch (error) {
            console.error("Queue fetch error:", error);
        }
    }

    // ============================
    // SPECIALIZATION → DOCTOR DROPDOWN (FINAL WORKING)
    // ============================
    setTimeout(async () => {

        const specializationSelect = document.getElementById('departmentSelect');
        const doctorSelect = document.getElementById('doctorSelect');

        if (!specializationSelect || !doctorSelect) {
            console.error("Dropdown elements not found!");
            return;
        }

        try {
            const res = await fetch('http://127.0.0.1:5000/api/doctors');
            const doctors = await res.json();

            console.log("Doctors Data:", doctors);

            // CLEAR
            specializationSelect.innerHTML = "";

            const defaultOption = document.createElement("option");
            defaultOption.textContent = "Select Specialization";
            defaultOption.value = "";
            specializationSelect.appendChild(defaultOption);

            const seen = new Set();

            doctors.forEach(doc => {
                if (!doc.specialization) return;

                if (!seen.has(doc.specialization)) {
                    seen.add(doc.specialization);

                    const opt = document.createElement("option");
                    opt.value = doc.specialization;
                    opt.textContent = doc.specialization;

                    specializationSelect.appendChild(opt);
                }
            });

            doctorSelect.disabled = true;

            specializationSelect.addEventListener("change", () => {

                const selected = specializationSelect.value;

                doctorSelect.innerHTML = `<option value="">Select Doctor</option>`;

                if (!selected) {
                    doctorSelect.disabled = true;
                    return;
                }

                doctors
                    .filter(doc => doc.specialization === selected)
                    .forEach(doc => {

                        const opt = document.createElement("option");
                        opt.value = doc.doctor_id;
                        opt.textContent = `Dr. ${doc.first_name} ${doc.last_name}`;

                        doctorSelect.appendChild(opt);
                    });

                doctorSelect.disabled = false;
            });

            doctorSelect.addEventListener('change', () => {
                selectedDoctorId = doctorSelect.value;
            });

        } catch (err) {
            console.error("Dropdown error:", err);
        }

    }, 500);

    // ============================
    // SLOT SELECTION
    // ============================
    document.querySelectorAll('.slot-btn').forEach(slot => {
        slot.addEventListener('click', () => {
            document.querySelectorAll('.slot-btn').forEach(s => s.classList.remove('active'));
            slot.classList.add('active');
        });
    });

    // ============================
    // BOOKING
    // ============================
    const bookingForm = document.getElementById('bookingForm');

    if (bookingForm) {
        bookingForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            const activeTimeText = document.querySelector('.slot-btn.active')?.innerText;
            const today = new Date().toLocaleDateString('en-CA');

            const fullName = document.getElementById('bookingName').value;
            const contact = document.getElementById('bookingPhone').value;
            const gender = document.getElementById('gender').value;
            const dob = document.getElementById('dob').value;

            const doctorSelect = document.getElementById('doctorSelect');
            const selectedDoctorOption = doctorSelect.options[doctorSelect.selectedIndex];

            const doctorName = selectedDoctorOption
                ? selectedDoctorOption.text.replace("Dr. ", "")
                : "";

            if (!fullName.trim()) {
                alert("Full Name is required!");
                return;
            }

            if (!contact.trim()) {
                alert("Contact number is required!");
                return;
            }

            const appointmentData = {
                patient_id: patient.patient_id,
                doctor_id: selectedDoctorId,
                doctor_name: doctorName,
                full_name: fullName,
                contact: contact,
                gender: gender,
                dob: dob,
                appointment_date: today,
                appointment_time: convertTo24Hour(activeTimeText)
            };

            try {
                const response = await fetch('http://127.0.0.1:5000/api/book_appointment', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(appointmentData)
                });

                const result = await response.json();

                if (result.success) {
                    alert(`Confirmed!\nDoctor: ${doctorName}\nTime: ${activeTimeText}`);

                    updateQueueStatus(patient.patient_id);
                    updateAllQueueStatus(patient.patient_id);
                }

            } catch (error) {
                alert("Check if Flask is running.");
            }
        });
    }

    // ============================
    // LOGOUT
    // ============================
    const logoutBtn = document.getElementById('logoutBtn');

    if (logoutBtn) {
        logoutBtn.addEventListener('click', (e) => {
            e.preventDefault();
            localStorage.removeItem('userData');
            localStorage.removeItem('role');
            window.location.href = 'login.html';
        });
    }
});

// ============================
function convertTo24Hour(timeStr) {
    if (!timeStr) return "00:00:00";
    let [time, modifier] = timeStr.split(' ');
    let [hours, minutes] = time.split(':');
    let h = parseInt(hours, 10);
    if (modifier === 'PM' && h !== 12) h += 12;
    if (modifier === 'AM' && h === 12) h = 0;
    return `${h.toString().padStart(2, '0')}:${minutes}:00`;
}

function printToken() {
    window.print();
}