// query URL
var url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_hour.geojson"

// feed data features into createFeatures after querying
d3.json(url, function(data) {
	createFeatures(data.features);
});


// Creates layers 
function createFeatures(X) {

	// popups for each feature
	function featPopUp(feat, layer) {
		layer.bindPopup("<h3>" + feat.properties.place +"</h3>" +
						"<hr><p>" + new Date(feat.properties.time) + "</p></hr>" +
						"<hr><p> Magnitude: " + feat.properties.mag + "</p>");				
	}

	// creates earthquakes to put into Map
	var earthquakes = L.geoJSON(X, {
		featPopUp: featPopUp,
		toLayer: function(feat, latlng) {
			var col;
			var r = 255;
			var g = Math.floor(255-80*feat.properties.mag);
			var b = Math.floor(255-80*feat.properties.mag);
			col= "rgb("+r+" ,"+g+","+ b+")"

			var geoMarkerOptions = {
				radius:4*feat.properties.mag,
				fillColor: color,
				color: "black",
				weight:1,
				opacity:1,
				fillOpacity:0.8
			};

			return L.circleMarker(latlng, geoMarkerOptions);
		}
	});

	// creates Map using local earthquake variable
	map(earthquakes);
}

function map(earthquakes) {

  // Define streetmap and darkmap layers
  var streetLayer = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?" +
  "access_token=pk.eyJ1Ijoic2FtdGltdXJhIiwiYSI6ImNqaWNhdHVrdDFpbW4za3M5cDV3YTcxajMifQ." +
  "v7_rxlFk5zpFtr9ijTomoA");

  var darkLayer = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/dark-v9/tiles/256/{z}/{x}/{y}?" +
  "access_token=pk.eyJ1Ijoic2FtdGltdXJhIiwiYSI6ImNqaWNhdHVrdDFpbW4za3M5cDV3YTcxajMifQ." +
  "v7_rxlFk5zpFtr9ijTomoA");


  var base = {
    "Street Map": streetLayer,
    "Dark Map": darkLayer
  };

  var overlayMaps = {
    Earthquakes: earthquakes
  };

  // map for layers
  var myMap = L.map("map", {
  	center: [30, -100],
  	zoom:5,
  	layers: [streetLayer, darkLayer]
  });



  // layer control
  L.control.layers(base, overlayMaps).addTo(myMap);
}