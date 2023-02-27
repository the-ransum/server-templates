// Dependencies
const express = require('express');

// Globals
const app = express();
const PORT = process.env.PORT || 3000;

// Creating a simple route => http://localhost:3000/
app.get('/', (req, res) => {
	res.send('Hello World!');
});

// Start the server listening on port 3000
app.listen(PORT, () => {
	console.log(`Server listening on port ${PORT}`);
});
