document.addEventListener('DOMContentLoaded', () => {
    alert("yo");

    if(document.querySelector('#Pizza').length > 1){
        alert("already have pizza types");
    };
    document.getElementsByTagName('button').onclick = function() {

        document.body.style.backgroundColor=red;

    }
    /*document.querySelector('#items').onchange = function() {
        document.querySelector(`#${this.value}`).style.display = block;
    };*/
});