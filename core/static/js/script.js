// Validation for Register Form
document.getElementById('register-form')?.addEventListener('submit', function(event) {
    // Clear previous error messages
    document.querySelectorAll('.error-message').forEach(function(error) {
        error.textContent = '';
        error.style.visibility = 'hidden'; // Hide all error messages initially
    });

    let isValid = true;

    // Validate Username
    const username = document.getElementById('username').value.trim();
    if (!username || username.length < 3) {
        document.getElementById('username-error').textContent = 'Username must be at least 3 characters.';
        document.getElementById('username-error').style.visibility = 'visible';
        isValid = false;
    } else if (!/^[a-zA-Z]+$/.test(username)) {
        document.getElementById('username-error').textContent = 'Username must contain only letters.';
        document.getElementById('username-error').style.visibility = 'visible';
        isValid = false;
    }

    // Validate Email
    const email = document.getElementById('email')?.value.trim();
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email || !emailPattern.test(email)) {
        document.getElementById('email-error').textContent = 'Please enter a valid email address.';
        document.getElementById('email-error').style.visibility = 'visible';
        isValid = false;
    }

    // Validate Password
    const password1 = document.getElementById('password1')?.value.trim();
    const password2 = document.getElementById('password2')?.value.trim();
    if (!password1 || password1.length < 8) {
        document.getElementById('password1-error').textContent = 'Password must be at least 8 characters.';
        document.getElementById('password1-error').style.visibility = 'visible';
        isValid = false;
    }

    // Validate Password Confirmation
    if (password1 && password2 && password1 !== password2) {
        document.getElementById('password2-error').textContent = 'Passwords do not match.';
        document.getElementById('password2-error').style.visibility = 'visible';
        isValid = false;
    }

    // Prevent form submission if validation fails
    if (!isValid) {
        event.preventDefault();
    }
});

// Validation for Login Form
document.getElementById('login-form')?.addEventListener('submit', function(event) {
    // Clear previous error messages
    document.querySelectorAll('.error-message').forEach(function(error) {
        error.textContent = '';
        error.style.visibility = 'hidden'; // Hide all error messages initially
    });

    let isValid = true;

    // Validate Username
    const username = document.getElementById('username').value.trim();
    if (!username) {
        document.getElementById('username-error').textContent = 'Username is required.';
        document.getElementById('username-error').style.visibility = 'visible';
        isValid = false;
    } else if (!/^[a-zA-Z]+$/.test(username)) {
        document.getElementById('username-error').textContent = 'Username must contain only letters.';
        document.getElementById('username-error').style.visibility = 'visible';
        isValid = false;
    }

    // Validate Password
    const password = document.getElementById('password').value.trim();
    if (!password) {
        document.getElementById('password-error').textContent = 'Password is required.';
        document.getElementById('password-error').style.visibility = 'visible';
        isValid = false;
    }

    // Prevent form submission if validation fails
    if (!isValid) {
        event.preventDefault();
    }
});