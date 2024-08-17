$(document).ready(function() {
    const loginForm = $('#loginForm');
    const message = $('#message');

    if (loginForm.length) {
        loginForm.on('submit', function(event) {
            event.preventDefault();

            const username = $('#username').val();
            const password = $('#password').val();

            $.ajax({
                url: 'http://127.0.0.1:5000/login',
                method: 'POST',
                contentType: 'application/json',
                dataType: 'json',
                beforeSend: function(request) {
                    console.error(request);
                    request.setRequestHeader("Accept", 'application/ld+json');
                },
                data: JSON.stringify({ username, password }),
                success: function(data) {
                    if (data.success) {
                        localStorage.setItem('access_token', data.access_token);
                        localStorage.setItem('refresh_token', data.refresh_token);
                        window.location.href = '/home'; 
                    } else {
                        message.text(data.message);
                    }
                },
                error: function(error) {
                    console.error('Error:', error);
                    message.text('An error occurred.');
                }
            });
        });
    }

    const logoutButton = $('#logoutButton');
    if (logoutButton.length) {
        logoutButton.on('click', function() {
            $.ajax({
                url: 'http://127.0.0.1:5000/logout',
                method: 'POST',
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem('access_token')
                },
                success: function(data) {
                    if (data.message === 'Logged out successfully') {
                        localStorage.removeItem('access_token');
                        localStorage.removeItem('refresh_token');
                        window.location.href = '/login';
                    }
                },
                error: function(error) {
                    console.error('Error:', error);
                }
            });
        });
    }

    if (window.location.pathname === '/home') {
        const accessToken = localStorage.getItem('access_token');
        if (!accessToken) {
            window.location.href = '/login';
        } else {
            $.ajax({
                url: 'http://127.0.0.1:5000/home',
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${accessToken}`,
                },
                success: function(data) {
                    console.log(data);
                },
                error: function(response) {
                    if (response.status === 401) {
                        window.location.href = '/login';
                    } else {
                        console.error('Error:', response);
                        window.location.href = '/login';
                    }
                }
            });
        }
    }
});
