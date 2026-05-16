document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');

    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault(); 

        const selectedRole = document.getElementById('role').value;
        const identifier = document.getElementById('identifier').value;
        const password = document.getElementById('password').value;

        // 1. Map roles to their specific backend login URLs
        let loginUrl = '';
        if (selectedRole === 'Doctor') {
            loginUrl = 'http://127.0.0.1:5000/api/doctors/login';
        } else if (selectedRole === 'Admin') {
            loginUrl = 'http://127.0.0.1:5000/api/admin/login';
        } else if (selectedRole === 'Patient') {
            loginUrl = 'http://127.0.0.1:5000/api/patient/login';
        } else if (selectedRole === 'Receptionists') {
            loginUrl = 'http://127.0.0.1:5000/api/receptionists/login';
        }

        try {
            // 2. Send request to the Backend
            const response = await fetch(loginUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    username: identifier, // This matches data.get("username") in Python
                    password: password
                })
            });

            const data = await response.json();

            if (response.ok) {
                // 3. Success! Save user info and redirect
                alert(`Login Successful! Welcome, ${selectedRole}.`);
                
                // Store user details in browser memory if needed for the dashboard
                localStorage.setItem('userData', JSON.stringify(data));
                localStorage.setItem('role', selectedRole);

                if (selectedRole === 'Admin') {
                    localStorage.setItem('adminData', JSON.stringify(data));
                }
                if (selectedRole === 'Doctor') {localStorage.setItem('user', JSON.stringify(data.user));
                }
                if (selectedRole === 'Receptionists') {
    localStorage.setItem('receptionistData', JSON.stringify(data));
}
                

                // Redirect to the specific role page
                if (selectedRole === 'Doctor')  window.location.href = 'doctors.html';
                else if (selectedRole === 'Admin') window.location.href = 'admin.html';
                else if (selectedRole === 'Patient') window.location.href = 'patient.html';
                else if (selectedRole === 'Receptionists') window.location.href = 'receptionists.html';

            } else {
                // 4. Show error from backend (e.g., "Invalid username or password")
                alert('Login Failed: ' + (data.message || 'Unknown error'));
            }

        } catch (error) {
            console.error('Error:', error);
            alert('Failed to connect to the server. Make sure your Python backend is running!');
        }
    });

    // --- Password Toggle Logic ---
    const togglePass = document.getElementById('togglePass');
    const passInput = document.getElementById('password');
    
    if (togglePass && passInput) {
        togglePass.addEventListener('click', () => {
            if (passInput.type === 'password') {
                passInput.type = 'text';
                togglePass.textContent = '🙈';
            } else {
                passInput.type = 'password';
                togglePass.textContent = '👁️';
            }
        });
    }
});