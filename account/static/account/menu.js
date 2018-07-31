document.addEventListener('DOMContentLoaded', () => {

    document.getElementById('mainDiv').innerHTML = '';

    document.getElementById('items').onchange = function(){

        value = this.value;

        document.getElementById('mainDiv').innerHTML = '';
        alert(value);

        if(value === "Dinner Platter"){
            value = "Dinner_Platter"
        }

        document.getElementById('mainDiv').append(document.getElementById(`${value}Div`));
        document.getElementById(`${value}Div`).style.display = "block";


    };
});