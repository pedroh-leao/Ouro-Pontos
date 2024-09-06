const calcularRotaBtn = document.getElementById('calcularRotaBtn');
calcularRotaBtn.addEventListener('click', rotaPorPontosSelecionados);

const calcularPelaCoordenada = document.getElementById('calcularPelaCoordenada');
calcularPelaCoordenada.addEventListener('click', rotaPorLocalizacao);

alternarCapturarBtn();

function alternarCapturarBtn() {
    const radioButton = document.querySelector('input[type="radio"]:checked');
    calcularRotaBtn.disabled = !radioButton;
}

document.querySelectorAll('input[type="radio"]').forEach(radio => {
    radio.addEventListener('change', alternarCapturarBtn);
});


// Obter os pontos turisticos selecionados pelo usuário e abrir a página de calcular
function capturarID() {
    let ids_selecionados = [];
    const checkboxes = document.querySelectorAll('.select-point');
    const radioButton = document.querySelector('input[type="radio"]:checked');

    // Colocando em um vetor os checkbox selecionados
    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            let id = checkbox.value;
            ids_selecionados.push(id);
        }
    });

    // Adicionando o ponto de partida na lista de pontos selecionados, caso ele já não esteja
    if (radioButton) {
        let radioId = radioButton.value;
        // Verifica se o id já existe no vetor
        let index = ids_selecionados.indexOf(radioId);
        if (index != -1) {
            ids_selecionados.splice(index, 1);
        }
        //insere o id no inicio
        ids_selecionados.unshift(radioId);
    }

    return { ids: ids_selecionados };
}

async function buscar_info_ids(ids) {
    try {
        let response = await fetch('/pontos_turisticos/listar_por_ids', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(ids)
        });

        let data = await response.json();               
        return data;
    } catch (error) {
        console.error('Error:', error);
        alert(error);
    }
}

function ordenar_ids(ids_selecionados, ids_infos) {
    ids_selecionados = ids_selecionados.ids

    //Colocando os pontos turisticos na ordem, colocando a origem no início
    let pontos_turisticos = [];
    for (let i = 0; i < ids_selecionados.length; i++) {
        let index = parseInt(ids_selecionados[i]);                
        let temp = ids_infos[index]; 
        temp.longitude = parseFloat(temp.longitude)
        temp.latitude = parseFloat(temp.latitude)

        pontos_turisticos.push(temp);
    }

    return pontos_turisticos
}

function calcularRota(pontos_turisticos){
    localStorage.pontos_selecionados = JSON.stringify(pontos_turisticos);
    window.location.href = '/pontos_turisticos/listarMenorCaminho';
}

async function rotaPorPontosSelecionados() {
    let ids_selecionados = capturarID();

    if(ids_selecionados.ids.length < 2){
        alert("Selecione pelo menos dois pontos");
        return;
    }

    // Espera a resposta da requisição antes de continuar
    let ids_infos = await buscar_info_ids(ids_selecionados);

    // Chama a função de ordenação após a resposta
    pontos_turisticos = ordenar_ids(ids_selecionados, ids_infos);

    calcularRota(pontos_turisticos);
}

// Obter localização do usuário
var posicao;
const successCallback = (position) => {
    posicao = position
};
const errorCallback = (error) => {
    posicao = null
    document.getElementById('calcularPelaCoordenada').style.display = 'none';
};
navigator.geolocation.getCurrentPosition(successCallback, errorCallback);

async function rotaPorLocalizacao(){
    if(posicao == null){
        alert("Permita o site a acessar a sua localização.");
        return;
    }
    
    let ids_selecionados = capturarID();
    if(ids_selecionados.ids.length < 2){
        alert("Selecione pelo menos dois pontos");
        return;
    }

    let ids_infos = await buscar_info_ids(ids_selecionados);
    let pontos_turisticos = ordenar_ids(ids_selecionados, ids_infos);

    //Adicionando a localização do usuário 
    let minha_localizacao = {
        latitude: posicao.coords.latitude,
        longitude: posicao.coords.longitude,
    }

    pontos_turisticos.unshift(minha_localizacao);

    calcularRota(pontos_turisticos)
}