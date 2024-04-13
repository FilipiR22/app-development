let resultado_div = document.querySelector('#resultado');
const nome_remover = document.querySelector('#nome-remover');
const email_remover = document.querySelector('#email-remover');


async function acionarFuncaoNoBackendRemover() {
    try {
        //Remover
        const dados = {
            nome: nome_remover,
            email: email_remover
        };

        let response = await fetch('/remover', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dados)
        });

        const data = await response.json();
        console.log('Resultado do servidor:', data.resultado);
        resultado_div.textContent = data.resultado
    } catch (error) {
        console.error('Erro:', error);
        throw error;
    }
}
