// frontend/src/api.js
export async function searchQuery(query) {
    try {
        const response = await fetch('http://localhost:5000/api/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query }),
        });
        return await response.json();
    } catch (error) {
        console.error("Error:", error);
        return { error: true, message: error.toString() };
    }
}
