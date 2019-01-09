// from data.js
var tableData = data;

// Reference table body
var tbody = d3.select("tbody");

// Function to create table on the HTML
function createTable(tableData) {
    tableData.forEach((sighting) => {
        var row = tbody.append("tr");
        Object.entries(sighting).forEach(([key, value]) => {
            var cell = tbody.append("td");
            cell.text(value);
        });
    });
};

// Print all the UFO sightings on the HTML page
createTable(tableData);


// Filter by date

var filterButton = d3.select("#filter-btn");

filterButton.on("click", function() {
    d3.event.preventDefault();

    var inputElement = d3.select("#datetime");

    var inputValue = inputElement.property("value");

    var dataFiltered = tableData.filter(sighting => sighting.datetime === inputValue)

    $('#ufo-table').find("td").empty();

    createTable(dataFiltered);

});
