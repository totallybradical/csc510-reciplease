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

    // Category Filter
    var category_box = document.getElementById("category-filter");
    var category = category_box.value;
    if (category != "(All Categories)") {
        $('#recipe-table-body tr').filter(function () {
            //category from row
            var category_row = $(this)[0].cells[1].innerText;
            $(this).toggle(category_row == category);
        });
    } else {
        $('#recipe-table-body tr').filter(function () {
            $(this).toggle(true);
        });
    }

    // Apply Text Filter
    $('#recipe-table-body tr').filter(function () {
        //category from row
        row = $(this)[0];
        console.log(row);
        var not_already_hidden = !($(this).css('display') == 'none');
        var contains_filter = Array.from(row.cells).some((col) => {
            return col.textContent.toLowerCase().includes(
                filterInput.value.toLowerCase()
            );
        });
        $(this).toggle(contains_filter && not_already_hidden);
    });
}

window.onload = function () {
    dbgPrint('filter.js loaded!');

    recipeTableBody = document.getElementById('recipe-table-body');
    dbgPrint('recipeTableBody:' + recipeTableBody);
    recipeTableBodyRows = Array.from(recipeTableBody.rows);
    dbgPrint('recipeTableBodyRows:' + recipeTableBodyRows);

    filterInput = document.getElementById('filter-input');
    dbgPrint('filterInput: ' + filterInput);
    filterInput.addEventListener("keyup", handleInput);
}
