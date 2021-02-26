// Add console.log to check to see if our code is working.
console.log("working");

//Centering on Nashville map
mapboxgl.accessToken = API_KEY
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [-86.8, 36.2],
    zoom: 9
});

map.addControl(
    new MapboxGeocoder({
        accessToken: mapboxgl.accessToken,
        mapboxgl: mapboxgl
    })
);

map.addControl(
    new MapboxDirections({
        accessToken: mapboxgl.accessToken
    }),
    "top-left"
);

map.on('load', function () {
    map.addSource("nashville", {
        "type": "geojson",
        "data": "https://raw.githubusercontent.com/whitneylosinski/Eat.Sleep.Data/main/Resources/neighbourhoods.geojson"
    });

    map.addLayer({
        "id": "nashville",
        "type": "line",
        "source": "nashville",
        "layout": {
            "line-join": "round",
            "line-cap": "round",
        },
        "paint": {
            "line-color": "black",
            "line-width": 1.5
        },
    });

    map.addLayer({
        "id": "nashville1",
        "type": "fill",
        "source": "nashville",
        "layout": {},
        "paint": {
            "fill-color": "rgb(0, 58, 116)",
            "fill-opacity": 0.2
        }
    });

    // When a click event occurs on a feature in the states layer, open a popup at the
    // location of the click, with description HTML from its properties.
    map.on('click', 'nashville1', function (e) {
        new mapboxgl.Popup()
            .setLngLat(e.lngLat)
            .setHTML(e.features[0].properties.neighbourhood)
            .addTo(map);
    });

    // Change the cursor to a pointer when the mouse is over the states layer.
    map.on('mouseenter', 'nashville1', function () {
        map.getCanvas().style.cursor = 'pointer';
    });

    // Change it back to a pointer when it leaves.
    map.on('mouseleave', 'nashville1', function () {
        map.getCanvas().style.cursor = '';
    });
});

// Add full screen control
map.addControl(new mapboxgl.FullscreenControl());

// Add zoom and rotation controls to the map.
map.addControl(new mapboxgl.NavigationControl());