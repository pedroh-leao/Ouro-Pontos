function deletar_ponto(button) {
    var row = button.parentNode.parentNode;

    var id = row.cells[0].innerText;

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