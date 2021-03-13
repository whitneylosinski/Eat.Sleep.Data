// Add console.log to check to see if our code is working.
console.log("working");

///Centering on Nashville map
mapboxgl.accessToken = 'pk.eyJ1Ijoia2VubGlldyIsImEiOiJja2liMzB4eXIwb2k5MnFtdjV6eXFjbDhxIn0.qQA5sH9AwnEl75gT7XuBTA'
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [-86.7816, 36.1627],
    zoom: 9
});



map.on('load', function () {
    map.addSource("nashville", {
        "type": "geojson",
        "data": "https://raw.githubusercontent.com/whitneylosinski/Eat.Sleep.Data/main/Resources/neighbourhoods.geojson"
    });


    map.addLayer({
        "id": "nashville-district-border",
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
            "fill-color": "orange",
            "fill-opacity": 0.2
        }
    });


    map.addControl(
        new MapboxGeocoder({
            accessToken: mapboxgl.accessToken,
            mapboxgl: mapboxgl
        }),
        // "top-center"

    );

    // map.addControl(
    //     new MapboxDirections({
    //         accessToken: mapboxgl.accessToken
    //     }),
    //     "top-left"
    // );

});

// Add full screen control
map.addControl(new mapboxgl.FullscreenControl())
// });

map.on('load', function () {
    map.loadImage(
        'https://raw.githubusercontent.com/kenliew728/png/main/bnb32.png',

        // 'https://docs.mapbox.com/mapbox-gl-js/assets/custom_marker.png',
        // Add an image to use as a custom marker
        function (error, image) {
            if (error) throw error;
            map.addImage('custom-marker', image);

            map.addSource('places', {
                'type': 'geojson',
                'data': {
                    'type': 'FeatureCollection',
                    'features': [
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 1</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.90495, 36.25586]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 2</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.80922, 36.20699]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 3</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.79087, 36.27839]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 4</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.74190, 36.02787]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 5</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.76406, 36.19068]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 6</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.73604, 36.17532]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 7</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.71644, 36.21189]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 8</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.73898, 36.24207]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 9</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.67736, 36.24680]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 10</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.72864, 36.32506]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 11</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.63070, 36.24006]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 12</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.58220, 36.16152]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 13</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.68140, 36.11845]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 14</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.63019, 36.16901]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 15</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.68767, 36.16177]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 16</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.74419, 36.10497]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 17</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.76552, 36.13031]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 18</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.80578, 36.13070]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 19</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.78622, 36.16346]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 20</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.87850, 36.17019]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 21</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.82032, 36.16634]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 22</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.94528, 36.08819]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 23</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.88709, 36.10891]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 24</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.83984, 36.13334]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 25</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.79627, 36.10187]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 26</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.74143, 36.08073]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 27</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.72749, 36.05396]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 28</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.66876, 36.07205]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 29</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.62954, 36.09587]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 30</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.70221, 36.06685]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 31</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.67679, 36.01412]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 32</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.64222, 36.04511]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 33</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.58748, 36.05512]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 34</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.82832, 36.06490]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>District 35</strong>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-86.97236, 36.12008]
                            }
                        }
                    ]
                }
            });

            // Add a layer showing the places.
            map.addLayer({
                'id': 'places',
                'type': 'symbol',
                'source': 'places',
                'layout': {
                    'icon-image': 'custom-marker',
                    'icon-allow-overlap': true
                }
            });
        }
    );

    // Create a popup, but don't add it to the map yet.
    var popup = new mapboxgl.Popup({
        closeButton: false,
        closeOnClick: false
    });

    map.on('mouseenter', 'places', function (e) {
        // Change the cursor style as a UI indicator.
        map.getCanvas().style.cursor = 'pointer';

        var coordinates = e.features[0].geometry.coordinates.slice();
        var description = e.features[0].properties.description;

        // Ensure that if the map is zoomed out such that multiple
        // copies of the feature are visible, the popup appears
        // over the copy being pointed to.
        while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
            coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
        }

        // Populate the popup and set its coordinates
        // based on the feature found.
        popup.setLngLat(coordinates).setHTML(description).addTo(map);
    });

    map.on('mouseleave', 'places', function () {
        map.getCanvas().style.cursor = '';
        popup.remove();

    });
});