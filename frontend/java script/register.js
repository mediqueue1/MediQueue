document.addEventListener('DOMContentLoaded', () => {
    const registrationForm = document.getElementById('registrationForm');
    const roleSelect = document.getElementById('role');
    const doctorFields = document.getElementById('doctorFields');
    const patientFields = document.getElementById('patientFields');

    // 1. Dynamic Form Logic: Show/Hide fields based on role selection
    roleSelect.addEventListener('change', (e) => {
        const selectedRole = e.target.value;
        
        // Hide both first
        doctorFields.style.display = 'none';
        patientFields.style.display = 'none';

        // Show the relevant one
        if (selectedRole === 'Doctor') {
            doctorFields.style.display = 'block';
        } else if (selectedRole === 'Patient') {
            patientFields.style.display = 'block';
        }
    });

    // 2. Submit Logic
    registrationForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const role = document.getElementById('role').value;
        
        if (!role) {
            alert("Please select a Staff Role");
            return;
        }

        // 🔐 Password validation
            const password = document.getElementById('password').value;
            const passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$/;

            if (!passwordPattern.test(password)) {
            alert("Password must contain uppercase, lowercase, number, special character and be at least 8 characters long");
            return;
        }

        // Build the base user data object
        const userData = {
            firstName: document.getElementById('firstName').value,
            middleName: document.getElementById('middleName').value,
            lastName: document.getElementById('lastName').value,
            email: document.getElementById('email').value,
            username: document.getElementById('username').value,
            phone: document.getElementById('phone').value,
            role: role,
            password: document.getElementById('password').value
        };

        // Add specific fields if applicable
        
        if (role === 'Patient') {
            userData.gender = document.getElementById('gender').value;
            userData.dateOfBirth = document.getElementById('dob').value;
            userData.address = document.getElementById('address').value;
        }
        else if (role === 'Doctor') {
            userData.specialization = document.getElementById('specialization').value;
        }

        // 3. Determine the correct backend URL based on role
        let backendUrl = '';
        if (role === 'Doctor') {
            backendUrl = 'https://mediqueue-api-qsnu.onrender.com/api/doctors/register'; 
        } else if (role === 'Patient') {
            backendUrl = 'https://mediqueue-api-qsnu.onrender.com/api/patient/register'; 
        } else if (role === 'Admin') {
            backendUrl = 'https://mediqueue-api-qsnu.onrender.com/admin/register';
        } else if (role === 'Receptionist') {
            backendUrl = 'https://mediqueue-api-qsnu.onrender.com/receptionists/register';
        }

        // 4. Send to Backend
        try {
            // We pass the dynamic 'backendUrl' variable into the fetch command
            const response = await fetch(backendUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(userData)
            });

            const data = await response.json();

            if (response.ok) {
                alert('Account created successfully! Please login.');
                window.location.href = 'login.html'; // Redirect to login
            } else {
                alert('Registration failed: ' + (data.message || 'Unknown error'));
            }

        } catch (error) {
            console.error('Error:', error);
            alert('Already Registered.Please use another Username to register');
            console.log("Data that tried to send:", userData);
            console.log("URL it tried to send to:", backendUrl);
        }
    });
});