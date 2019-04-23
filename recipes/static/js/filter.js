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

function applyAllFilters() {
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

// On change of Keyword Filter box
function handleInput(event) {
    applyAllFilters();
}

$(document).ready(function () {
    // On click of a Favorite <3
    $('button[name=favorite]').click(function () {
        current_button = $(this);
        recipe_id = $(this).val();
        if (current_button.children('span[name=fave_icon]').hasClass('far')) {
            request_url = '/recipes/' + recipe_id + '/favorite';
            $.ajax({
                url: request_url,
                success: function (data) {
                    current_button.children('span[name=fave_icon]').removeClass("far");
                    current_button.children('span[name=fave_icon]').addClass("fas");
                }
            })
        } else {
            request_url = '/recipes/' + recipe_id + '/unfavorite';
            $.ajax({
                url: request_url,
                success: function (data) {
                    current_button.children('span[name=fave_icon]').removeClass("fas");
                    current_button.children('span[name=fave_icon]').addClass("far");
                }
            })
        }
    });

    // On change of Category filter
    $("#category-filter").on("change", function () {
        applyAllFilters();           
    });

    // On change of Favorites Only filter
    $('#favorites-filter').change(function () {
        applyAllFilters(); 
    });
});

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
    applyAllFilters();
}
