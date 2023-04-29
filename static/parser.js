document
	.getElementById('prediction-form')
	.addEventListener('submit', async function (event) {
		event.preventDefault();

		let formData = new FormData(event.target);
		let data = {};

		for (let [key, value] of formData.entries()) {
			data[key] = parseFloat(value);
		}

		let response = await fetch('/predict', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(data),
		});

		if (response.ok) {
			let result = await response.json();
			let message;
			if (result.prediction === 1) {
				message = 'Prone to heart attack: True';
			} else if (result.prediction === 0) {
				message = 'Prone to heart attack: False';
			} else {
				message = 'Error en la predicción';
			}
			document.getElementById('prediction-result').textContent = message;
		} else {
			document.getElementById('prediction-result').textContent =
				'Error: ' + response.status + ' ' + response.statusText;
		}
	});
