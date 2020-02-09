var map;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 42.2809, lng: -71.2378 },
        zoom: 14
    });

    addMarker({
        coords:{lat:42.2863,lng:-71.2312},
        iconImage:'https://lh3.googleusercontent.com/proxy/qfaafYlkDkXNhtxMYNKdKogCaVSCejQY_Y4hy6D58vCB1eze37wdIGKdoAXpapOvPSf-IhiE5wOZKoisvRuQtXTqDZRFF4HFuhieyMQ'
    })

    function addMarker(prop){
        var marker = new google.maps.Marker({
            position:prop.coords,
            map:map,
            icon:prop.iconImage
        });
    }

    map.addListener('click', function (e) {
        placeMarker(e.latLng, map);
    });
}

function placeMarker(latLng, map) {
    var marker = new google.maps.Marker({
        position: latLng,
        map: map
    });
    console.log("New marker at " + latLng);
}