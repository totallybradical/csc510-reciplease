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

    let newRows = []
    for (let i = 0; i < recipeTableBodyRows.length; i++) {
        let keep = false;
        let row = recipeTableBodyRows[i];
        dbgPrint(`row ${i}: ${row}`);
        for (let j = 0; j < row.cells.length; j++) {
            let col = row.cells[j];
            dbgPrint(`col ${j}: ${col}`);
            if (col.textContent.includes(filterInput.value)) {
                keep = true;
                break;
            }
        }

        if (keep) {
            newRows.push(row);
        }
    }

    while (recipeTableBody.firstChild) {
        recipeTableBody.removeChild(recipeTableBody.firstChild);
    }
    for (let i = 0; i < newRows.length; i++) {
        recipeTableBody.appendChild(newRows[i]);
    }
}

window.onload = function() {
    dbgPrint('filter.js loaded!');

    recipeTableBody = document.getElementById('recipe-table-body');
    dbgPrint('recipeTableBody:' + recipeTableBody);
    recipeTableBodyRows = []
    for (let i = 0; i < recipeTableBody.rows.length; i++) {
        let keep = false;
        let row = recipeTableBody.rows[i];
        dbgPrint(`row ${i}: ${row}`);
        recipeTableBodyRows.push(row);
    }

    filterInput = document.getElementById('filter-input');
    dbgPrint('filterInput: ' + filterInput);
    filterInput.addEventListener("keyup", handleInput);
}
