document.addEventListener('DOMContentLoaded', () => {
    alert("yo");

    if(document.querySelector('#Pizza').length > 1){
        alert("already have pizza types");
    };
    document.querySelector('#items').onchange = function() {
        document.querySelector(`#${this.value}`).style.display = block;
    };
});