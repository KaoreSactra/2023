//calcular idade automáticamente
const idade = document.getElementById('idade');

const atualizarIdade = setInterval(function date() {
    
    let data = new Date();
    let ano = data.getFullYear();
    idade.textContent = String(ano - 2004)+" anos";

})