document.addEventListener('DOMContentLoaded', () => {

    document.getElementById('mainDiv').innerHTML = '';

    document.getElementById('items').onchange = function(){

        alert(this.value);
        document.getElementById('mainDiv').append(document.getElementById(`${this.value}Div`));
        document.getElementById(`${this.value}Div`).style.display = "block";
    };

    document.getElementById('is_special').onchange = function(){
        alert(document.querySelector('input[name = "is_specialRD"]:checked').value);
    };
});