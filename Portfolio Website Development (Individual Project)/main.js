var tableObj;

$(document).ready(function() {
    tableObj = $('#example').DataTable({
        "searching": true,
    });
});

document.getElementById("btnSubmit").addEventListener("click", function(event) {
    var compname = document.getElementById("compUserInput").value
    var email = document.getElementById("emailUserInput").value
    var password = document.getElementById("passwordUserInput").value

    $.ajax({
        type: "POST",
        url: "./main.php",
        data: {
            compname: compname, 
            email: email, 
            password: password
        }
    }).done(function(result) {
        var jsonObj = JSON.parse(result)
        insertData(jsonObj)
    });
});

function insertData(jsonObj) {
    jsonObj.forEach(row => {
        var userId = row["userId"];
        var compname = row["compName"];
        var email = row["userEmail"];
        var password = row["userPassword"];

        tableObj.row.add([
            userId,
            compname,
            email,
            password
        ]).draw();
    });
}