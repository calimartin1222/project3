document.addEventListener('DOMContentLoaded', () => {
    if(document.getElementById('mainDiv')){
        document.getElementById('mainDiv').innerHTML = '';

        document.getElementById('items').onchange = function(){

            value = this.value;

            document.getElementById('mainDiv').innerHTML = '';

            if(value === "Dinner Platter"){
                value = "Dinner_Platter";
            }

            document.getElementById('mainDiv').append(document.getElementById(`${value}Div`));
            document.getElementById(`${value}Div`).style.display = "block";
        };

        if(document.getElementsByClassName('submit_order')){
            document.querySelectorAll('.submit_order').forEach(function(button) {

                button.onclick = function() {

                    user_name = document.getElementById('name').innerHTML;
                    item_select = document.getElementById('items');
                    item = item_select[item_select.selectedIndex].value;

                    if(document.getElementById('sizes') != null){

                        size_select = document.getElementById('sizes');
                        size = size_select[size_select.selectedIndex].value;

                        if(size === "sizes"){
                            alert("Please Select a Size");
                            return;
                        }
                    }

                    if(document.getElementById('is_special') != null){
                        special = document.querySelector('input[name = "is_specialRD"]:checked').value;
                    }

                    if(document.getElementById('types') != null){

                        type_select = document.getElementById('types');
                        type = type_select[type_select.selectedIndex].value;

                        if(type === "types"){
                            alert("Please Select a Type");
                            return;
                        }
                    }

                    if(document.getElementById('extras') != null){
                        var extras = document.getElementsByName("subExtras");
                        var extrasList = [];
                        var extras_print = "";

                        for (var k = 0; k < extras.length; k++) {
                            if (extras[k].checked) {
                                extrasList.push(extras[k].value);
                            }

                        }

                        for (var l = 0; l < extrasList.length; l++) {
                            if(l === 0){
                                extras_print += `with ${extrasList[l]}`;
                            }
                            else if(l === extrasList.length-1) {
                                extras_print += `, and ${extrasList[l]}`;
                            }
                            else{
                                extras_print += `, ${extrasList[l]}`;
                            }
                        }
                    }
    //send info POST --> cart adds an order to the Order model, have the order model have "completed" boolean attribute--> if false, say order is pending in __str__
                    if(document.getElementById('toppings') != null){

                        var toppings = document.getElementsByName("topping");
                        var toppingsList = [];
                        var toppings_print = "";

                        for (var i = 0; i < toppings.length; i++) {
                            if (toppings[i].checked) {
                                toppingsList.push(toppings[i].value);
                            }
                        }

                        for (var j = 0; j < toppingsList.length; j++) {
                            if(j === 0){
                                toppings_print += `with ${toppingsList[j]}`;
                            }
                            else if(j === toppingsList.length-1) {
                                toppings_print += `, and ${toppingsList[j]}`;
                            }
                            else{
                                toppings_print += `, ${toppingsList[j]}`;
                            }
                        }
                    }

                    //dont send POST toppings_print, send toppingsList to get length later for price & add owner group

                    const request = new XMLHttpRequest();

                    request.open('POST', '/cart');

                    request.onload = () => {
                        a = document.createElement("a");
                        a.href = "/cart";
                        a.innerHTML = "Success! Go to Cart";
                        document.querySelector('#mainDiv').append(a);
                    };

                    const data = new FormData();

                    data.append('user_name', user_name);

                    data.append('item', item);

                    if(size){
                        data.append('size', size);
                    }

                    if(type){
                        data.append('type', type);
                    }

                    if(extrasList){
                        data.append('extras', extrasList.length);
                    }

                    if(toppingsList){
                        data.append('toppings', toppingsList.length);
                    }

                    if(special){
                        data.append('is_special', special);
                    }

                    request.send(data);

                    return false;
                };
            });
        }

        if(document.getElementsByClassName('topping')){
            document.querySelectorAll('.topping').forEach(function(checkbox) {
                checkbox.onclick = function() {
                    checked = document.querySelectorAll('input[name="topping"]:checked').length;
                    special = document.querySelector('input[name = "is_specialRD"]:checked').value;

                    if(checked > 3 && special != "special"){
                        alert("You can have up to 3 toppings on a Regular Pizza. Please choose Special Pizza to have 4 or more toppings!");
                        this.checked = false;
                    }
                };
            });
        }
    }
});