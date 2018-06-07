// Set Variables
var $tbody = document.querySelector("tbody");
var $searchInput = document.querySelector("#search");
var $searchButton = document.querySelector("#searchButton");
var filteredData = data;

// Add EventListener
$searchButton.addEventListener("click", handleSearchButtonClick);


/*
  Creates Table in HTML using data.js
  @params: none
  @return: none
*/
function renderTable() {
  $tbody.innerHTML = "";

  //iter through list of dictionaries in data.js
  for (var i = 0; i < filteredData.length; i++) {

    //get dictionary and keys
    var dict = filteredData[i];
    var keys = Object.keys(dict);

    //new row
    var $row = $tbody.insertRow(i);

    //iter through keys and insert each value to a cell
    for (var j = 0; j < keys.length; j++) {
      var key = keys[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = dict[key];
    }
  }
}

/*
  Upon Clicking searchButton, filters Table by datetime
  @params: none
  @return: none
*/
function handleSearchButtonClick() {
  // search input
  var filterDate = $searchInput.value;

  // Set filteredData to an array of all data whose "datetime" matches the filter
  filteredData = data.filter(function(x) {
    var y = x.datetime;
    return y === filterDate;
  });
  renderTable();
}

// Render the table for the first time on page load
renderTable();
