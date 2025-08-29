document.addEventListener('DOMContentLoaded', () => {
    
    const emailForm = document.getElementById('email-form');
    const submitButton = document.getElementById('submit-button');
    const resultsContainer = document.getElementById('results-container');
    const categoryBadge = document.getElementById('category-badge');
    const responseParagraph = document.getElementById('suggested-response');

    emailForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const emailText = document.getElementById('email-text').value;

        submitButton.disabled = true;
        submitButton.textContent = 'Analisando...';
        resultsContainer.style.display = 'none';

        try {
            const apiResponse = await fetch('/classify', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: emailText }),
            });

            const data = await apiResponse.json();

            if (!apiResponse.ok) {
                throw new Error(data.error || 'Ocorreu um erro desconhecido.');
            }

            categoryBadge.textContent = data.category;
            responseParagraph.textContent = data.suggested_response;
            
            categoryBadge.className = '';
            const categoryClass = data.category === 'Produtivo' ? 'productive' : 'unproductive';
            categoryBadge.classList.add(categoryClass);

            resultsContainer.style.display = 'block';

        } catch (error) {
            resultsContainer.style.display = 'block';
            categoryBadge.textContent = 'Erro!';
            categoryBadge.className = 'error';
            responseParagraph.textContent = error.message;

        } finally {
            submitButton.disabled = false;
            submitButton.textContent = 'Analisar E-mail';
        }
    });
});