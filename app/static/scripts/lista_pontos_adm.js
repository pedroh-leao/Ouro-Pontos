function obter_id(button){
    let row = button.parentNode.parentNode;
    let id = row.cells[0].innerText;
    return id;
}

function deletar_ponto(button) {
    let id = obter_id(button);

    fetch('/pontos_turisticos/deletar', {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "id": id })
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            alert('Ponto turístico removido com sucesso! ID: ' + data.id);
            //removendo linha da tabela
            row.parentNode.removeChild(row);
        })
        .catch((error) => {
            console.error('Error:', error);
            alert(error);
        });
}

function editar_ponto(button){
    let id = obter_id(button);
    window.location.href = "pontos_turisticos/tela_editar?id="+id;
}