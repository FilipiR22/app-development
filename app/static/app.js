document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('enviar-requisicao').addEventListener('click', () =>{
        var xhr = new XMLHttpRequest();
        var url = '/processar-requisicao';
        xhr.open('POST', url, true);
        xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
        xhr.onload = function () {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                document.getElementById('resultado').innerText = 'Resposta do servidor: ' + response;
                console.log(response)
            } else {
                console.error('Erro na requisição AJAX');
            }
        };

        var data = JSON.stringify({ key: 'value' });
        xhr.send(data);
    });
});
