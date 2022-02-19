"use strict";

function addRow() {
    var newRow = document.getElementById("new-row");
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
    var directionsDiv = document.getElementById("directions");
    directionsDiv.appendChild(formGroup);

    // update the index
    newRow.setAttribute('data-next-elem', parseInt(idx)+1);
}