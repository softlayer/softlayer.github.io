function titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row') {
    // Declare variables
    var input, filter, ul, li, a, i;
    input = document.getElementById(inputId);
    filter = input.value.toUpperCase();
    methods = document.getElementById(divId);
    li = methods.getElementsByClassName(elementClass);

    // Loop through all list items, and hide those who don't match the search query
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        search_term = "SOFTLAYER_"+a.innerHTML.trim().toUpperCase();
        if (search_term.indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}