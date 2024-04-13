async function acionarFuncaoNoBackend(nomeFuncao, parametros) {
    try {
        const dados = {
            funcao: nomeFuncao,
            parametros: parametros
        };

        const response = await fetch('/executar-funcao', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dados)
        });

        const data = await response.json();
        console.log('Resultado do servidor:', data.resultado);
        return data.resultado;
    } catch (error) {
        console.error('Erro:', error);
        throw error;
    }
}

// Exemplo de uso
acionarFuncaoNoBackend('funcao1', { parametro1: valor1, parametro2: valor2 });
