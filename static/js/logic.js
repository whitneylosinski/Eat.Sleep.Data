// Add console.log to check to see if our code is working.
console.log("working");



// We create the tile layer that will be the background of our map.
let streets = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data © <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    // id: 'mapbox.streets',
    accessToken: API_KEY
});

// We create the dark view tile layer that will be an option for our map.
let satelliteStreets = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data © <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    accessToken: API_KEY
});

// Create a base layer that holds both maps.
let baseMaps = {
    Streets: streets,
    SatelliteStreets: satelliteStreets
};

// Create the map object with center, zoom level and default layer.
let map = L.map('mapid', {
    center: [36.2, -86.8],
    //[43.7, -79.3],
    zoom: 11,
    layers: [streets]
})

// Pass our map layers into our layers control and add the layers control to the map.
L.control.layers(baseMaps).addTo(map);

// Accessing the Toronto Neighborhood GeoJSON URL
let nashvilleHoods = "https://raw.githubusercontent.com/whitneylosinski/Eat.Sleep.Data/main/Resources/neighbourhoods.geojson";

function getAreaColor(feature) {

    console.log(feature)
    switch (feature.properties.neighbourhood) {
        case 'District 1': return 'gold';
        case 'District 2': return 'blue';
        case 'District 3': return 'green';
        case 'District 4': return 'red';
        case 'District 5': return 'purple';
        case 'District 6': return 'grey';
        case 'District 7': return 'orange';
        case 'District 8': return 'gold';
        case 'District 9': return 'green';
        case 'District 10': return 'blue';
        case 'District 11': return 'purple';
        case 'District 12': return 'grey';
        case 'District 13': return 'gold';
        case 'District 14': return 'orange';
        case 'District 15': return 'blue';
        case 'District 16': return 'red';
        case 'District 17': return 'orange';
        case 'District 18': return 'purple';
        case 'District 19': return '#0B73F9';
        case 'District 20': return '#910BF9';
        case 'District 21': return '#F1791A';
        case 'District 22': return '#F6F90C';
        case 'District 23': return '#9CF90C';
        case 'District 24': return '#0C5BF9';
        case 'District 25': return '#5D6B7D';
        case 'District 26': return '#1AD358';
        case 'District 27': return '#1A95D3';
        case 'District 28': return '#B51AD3';
        case 'District 29': return '#D3391A';
        case 'District 30': return '#1A58D3';
        case 'District 31': return '#20D31A';
        case 'District 32': return '#0C5BF9';
        case 'District 33': return '#F6F90C';
        case 'District 34': return '#0CF919';
        case 'District 35': return '#0B73F9';

            break;
    }
};

function areaStyle(feature) {
    return {
        fillColor: getAreaColor(feature),
        weight: 2,
        opacity: 2,
        color: 'black',
        fillOpacity: 0.2
    }
};

//let myStyle = {
//color: "blue",
//fillColor: "green",
//fillOpacity: 0.15,
//weight: 2.5

//}

// Grabbing GeoJSON data.
d3.json(nashvilleHoods).then(function (data) {
    console.log(data);

    // Creating a GeoJSON layer with the retrieved data
    L.geoJson(data, {
        style: areaStyle,
        onEachFeature: function (feature, layer) {
            layer.bindPopup("<h3>Neighborhood:" + feature.properties.neighbourhood + "</h3>");
        }

    }).addTo(map);

});

// Then we add our 'graymap' tile layer to the map.
// streets.addTo(map);

    // Different map style id available using valid access token:
    // mapbox://styles/mapbox.streets-v11
    // mapbox://styles/mapbox.light-v10
    // mapbox://styles/mapbox.dark-v10
    // mapbox://styles/mapbox.satellite-v9
    // mapbox://styles/mapbox.satellite-streets-v11
    // mapbox://styles/mapbox/navigation-preview-day-v4
    // mapbox://styles/mapbox/navigation-preview-night-v4
    // mapbox://styles/mapbox/navigation-guidance-day-v4
    // mapbox://styles/mapbox/navigation-guidance-night-v4
    // mapbox://styles/mapbox.outdoors-v11

