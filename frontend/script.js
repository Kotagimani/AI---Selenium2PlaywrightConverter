document.getElementById('convertBtn').addEventListener('click', convertCode);

async function convertCode() {
    const javaCode = document.getElementById('javaInput').value;
    const outputDiv = document.getElementById('tsOutput');

    outputDiv.innerText = "// Converting...";

    try {
        const response = await fetch('/api/convert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ source_code: javaCode })
        });

        const data = await response.json();

        if (data.status === 'success') {
            outputDiv.innerText = data.conversion_result.converted_code;
        } else {
            outputDiv.innerText = "// Error: " + data.message;
        }
    } catch (e) {
        outputDiv.innerText = "// Network Error: " + e.message;
    }
}

// Basic Syntax Highlighting Helper (very simple)
function highlight(text) {
    // In a real app, use Prism.js or Monaco
    return text; // Placeholder
}
