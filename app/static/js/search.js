
// filter the table results 
function filterRepos() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("filterTable-input");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

// Add querystring (?language="Python") to the base url (http://localhost:5000/repos) and redirect 
function redirect() {
    debugger
    var currentUrl = window.location.origin + window.location.pathname;
    var search_value = document.getElementById('search_language').value;
    encoded =  encodeURIComponent(search_value)
    console.log("encoded...", encoded)
    
    if (search_value != "default") {
        var querystring = "?language=" + encoded;
        window.location.href = currentUrl + querystring;
    } else {
        var tbodyRef = document.getElementById('myTable').getElementsByTagName('tbody')[0]; 
        tbodyRef.innerHTML = '';
        window.location.href = window.location.origin + window.location.pathname;
    }
};

