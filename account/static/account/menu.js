//when the page loads
document.addEventListener('DOMContentLoaded', () => {
    //checks if element exists to avoid breaking
    if(document.getElementById('mainDiv')){
        //resets div when page loads
        document.getElementById('mainDiv').innerHTML = '';
        //when the dropdown menu with id 'items' is changed by the user
        document.getElementById('items').onchange = function(){
            //stores the user's selection value
            value = this.value;
            //resets div
            document.getElementById('mainDiv').innerHTML = '';
            //just a little syntax error that was caught,
            //an id can't have a space, so just underscore
            if(value === "Dinner Platter"){
                value = "Dinner_Platter";
            }
            //appends premade div for specific menu item and makes if visible
            document.getElementById('mainDiv').append(document.getElementById(`${value}Div`));
            document.getElementById(`${value}Div`).style.display = "block";
        };
        //if any of the 'submit' buttons are clicked do the following
        //just forewarning, I had to kinda 'fake' a single form even
        //though I did use different forms for the different attributes
        //hope it makes sense
        if(document.getElementsByClassName('submit_order')){
            document.querySelectorAll('.submit_order').forEach(function(button) {
                button.onclick = function() {
                    //the user.request value was passed through to javascript via
                    //an invisible p tage, I'm just accessing it here
                    user_name = document.getElementById('name').innerHTML;
                    //gets currently selected menu item
                    item_select = document.getElementById('items');
                    item = item_select[item_select.selectedIndex].value;
                    //error checking - doesn't execute following code if element
                    //doesn't exist so the code doesn't break
                    if(document.getElementById('sizes') != null){
                        //gets currently selected size
                        size_select = document.getElementById('sizes');
                        size = size_select[size_select.selectedIndex].value;
                    }
                    //error checking - doesn't execute following code if element
                    //doesn't exist so the code doesn't break
                    if(document.getElementById('is_special') != null){
                        //gets currently selected radio button
                        special = document.querySelector('input[name = "is_specialRD"]:checked').value;
                    }
                    //error checking - doesn't execute following code if element
                    //doesn't exist so the code doesn't break
                    if(document.getElementById('types') != null){
                        //gets currently selected type
                        type_select = document.getElementById('types');
                        type = type_select[type_select.selectedIndex].value;
                    }
                    //error checking - doesn't execute following code if element
                    //doesn't exist so the code doesn't break
                    if(document.getElementById('extras') != null){
                        var extras = document.getElementsByName("subExtras");
                        var extrasList = [];
                        var extras_print = "";
                        //gets all checked extras
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


                    const request = new XMLHttpRequest();

                    request.open('POST', '/cart/');

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
                        alert("You can have up to 3 toppings on a Regular Pizza. Please choose Special Pizza to have 4 or more toppings");
                        this.checked = false;
                    }
                };
            });
        }
    }
});