let recipeTableBody = null;
let recipeTableBodyRows = null;
let filterInput = null;
let debug = false;

function dbgPrint(msg) {
    if (debug) {
        console.log('debug: ' + msg);
    }
}

function handleInput(event) {
    dbgPrint('handleInput: ' + event);

    dbgPrint(`filterInput.value: ${filterInput.value}`);
    dbgPrint(`recipeTableBody: ${recipeTableBody}`);
    dbgPrint(`recipeTableBody.rows: ${recipeTableBody.rows}`);

    while (recipeTableBody.firstChild) {
        recipeTableBody.removeChild(recipeTableBody.firstChild);
    }

    recipeTableBodyRows.filter((row) => {
        return Array.from(row.cells).some((col) => {
            return col.textContent.includes(filterInput.value);
        })
    }).forEach((row) => recipeTableBody.appendChild(row));
}

window.onload = function() {
    dbgPrint('filter.js loaded!');

    recipeTableBody = document.getElementById('recipe-table-body');
    dbgPrint('recipeTableBody:' + recipeTableBody);
    recipeTableBodyRows = Array.from(recipeTableBody.rows);
    dbgPrint('recipeTableBodyRows:' + recipeTableBodyRows);

    filterInput = document.getElementById('filter-input');
    dbgPrint('filterInput: ' + filterInput);
    filterInput.addEventListener("keyup", handleInput);
}
