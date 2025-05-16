document.getElementById('generate-btn').addEventListener('click', function() {
    const data = document.getElementById('data').value;
    if (data) {
        fetch('http://127.0.0.1:5000/generate_qr', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ data: data }),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.qr_code) {
                document.getElementById('qrcode').innerHTML = `<img src="data:image/png;base64,${data.qr_code}" alt="QR Code">`;
            } else {
                alert('Error generating QR code');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error generating QR code: ' + error.message);
        });
    } else {
        alert('Please enter data to generate QR code');
    }
});
