"use strict";

function addDirectionRow() {
    var newRow = document.getElementById("table-div");
    var idx = newRow.getAttribute('data-next-elem');
    console.log(idx);

    // Create the new div element
    var formGroup = document.createElement("div");
    var input = document.createElement("input");
    input.name = 'title' + idx;
    var textarea = document.createElement("textarea");
    textarea.name = 'text' + idx;
    textarea.className = 'form-control';
    formGroup.appendChild(input);
    formGroup.appendChild(textarea);

    // append the formGroup
    var directionsDiv = document.getElementById("table-div");
    directionsDiv.appendChild(formGroup);

    // update the index
    newRow.setAttribute('data-next-elem', parseInt(idx)+1);
}

function addIngredientRow() {
    var table = document.getElementById('table-div');
    var idx = table.getAttribute('data-next-elem');
    console.log(idx);

    // Create the new div element
    var formGroup = document.createElement("div");
    formGroup.className = 'form-group'
    var input;

    var fields = ['name', 'amount', 'measurement', 'preparation']
    for (let i = 0; i < fields.length; ++i) {
        input = document.createElement("input");
        input.name = fields[i] + idx;
        input.setAttribute('value', 'a');
        formGroup.appendChild(input);
    }

    // append the formGroup
    var directionsDiv = document.getElementById("table-div");
    directionsDiv.appendChild(formGroup);

    // update the index
    table.setAttribute('data-next-elem', parseInt(idx)+1);
}