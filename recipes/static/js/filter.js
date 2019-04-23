let recipeTableBody = null;
let recipeTableBodyRows = null;
let filterInput = null;
let faveFilter = null;
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

    // Reset
    $('#recipe-table-body tr').filter(function () {
        $(this).toggle(true);
    });

    // Apply Category Filter
    var category_box = document.getElementById("category-filter");
    var category = category_box.value;
    if (category != "(All Categories)") {
        $('#recipe-table-body tr').filter(function () {
            //category from row
            var category_row = $(this)[0].cells[1].innerText;
            $(this).toggle(category_row == category);
        });
    }

    // Apply Favorites Filter
    if (faveFilter.checked) {
        $('#recipe-table-body tr').filter(function () {
            //category from row
            row = $(this)[0];
            var not_already_hidden = !($(this).css('display') == 'none');
            var is_fave = $(this).find('span[name=fave_icon]').hasClass('fas');
            $(this).toggle(not_already_hidden && is_fave);
        });
    }            

    // Apply Text Filter
    $('#recipe-table-body tr').filter(function () {
        //category from row
        row = $(this)[0];
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

    faveFilter = document.getElementById('favorites-filter');
}
