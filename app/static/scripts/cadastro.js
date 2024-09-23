function verificar_latitude_e_longitude(form_elements){
    let formData = {};
    let isValid = true;
    let latitude_longitude;

    for (let i = 0; i < form_elements.length; i++) {
        let element = form_elements[i];
        if (element.type !== "submit") {
            formData[element.name] = element.value;
            
            // Verifica se o campo é latitude ou longitude e se é um número de ponto flutuante
            if (element.name === "latitude" || element.name == "longitude") {
                latitude_longitude = parseFloat(element.value);
                if (isNaN(latitude_longitude)) {
                    isValid = false;
                    alert("A " + element.name + " deve ser um número de ponto flutuante.");
                }
            }
        }
    }

    return [isValid, formData];
}

async function enviarDados(route, formData) {
    try {
        // Envia os dados como JSON
        const response = await fetch(route, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        const data = await response.json();

        if (response.ok) {
            console.log('Success:', data);
            alert(data.message);
            return true;
        } else {
            console.error('Error:', data.message);
            alert(data.message);
            return false;
        }
    } catch (error) {
        console.error('Request failed:', error);
        alert('An error occurred');
        return false;
    }
}
