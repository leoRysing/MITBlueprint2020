var map;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 42.2809, lng: -71.2378 },
        zoom: 14
    });



    // Try HTML5 geolocation.
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            var pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };

            map.setCenter(pos);
        }
        );
    }


    /*let requestURL = "../data/locations.json"
    let request = new XMLHttpRequest();
    request.open('GET', requestURL)
    request.responseType = 'json';
    request.send();
    request.onload = function() {
        const superHeroes = request.response;
    }
    */


    /*
    for (var i = 0; i < markers.length; i++) {
        addMarker(markers[i]);
    }

    //cluster markers
    var markerCluster = new MarkerClusterer(map, markers,
        { imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m' });

    */

    function addMarker(props) {
        var marker = new google.maps.Marker({
            position: props.coords,
            map: map,
        });

        if (props.iconImage) {
            marker.setIcon(props.iconImage);
        }

        if (props.content) {
            var infoWindow = new google.maps.InfoWindow({
                content: props.content
            });

            marker.addListener('click', function () {
                infoWindow.open(map, marker);
            });
        }
    }

    map.addListener('click', function (e) {
        placeMarker(e.latLng, map);
    });
    console.log("ReadTextClosed");
}

function placeMarker(latLng, map) {
    var marker = new google.maps.Marker({
        position: latLng,
        map: map
    });
    console.log("New marker at " + latLng);
    localStorage.setItem("marker", latLng);
}
