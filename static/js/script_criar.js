const nome_criar = document.querySelector('#nome-criar');
const email_criar = document.querySelector('#email-criar');
let resultado_div_html = document.querySelector('.resultado');

async function acionarFuncaoNoBackendCriar() {
    try {
        //Criar
        const dados = {
            nome: nome_criar.value,
            email: email_criar.value
        };

        let response = await fetch('/criar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dados)
        });

        const data = await response.json();
        console.log('Resultado do servidor:', data.resultado);
        resultado_div_html.textContent = data.resultado;
    } catch (error) {
        console.error('Erro:', error);
        throw error;
    }
}

// Exemplo de uso

