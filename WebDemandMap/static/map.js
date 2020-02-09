var map;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 42.2809, lng: -71.2378 },
        zoom: 14
    });

    var markers = [
        {
            coords:{lat:42.2863,lng:-71.2312},
            /*iconImage:{
                url:'https://lh3.googleusercontent.com/proxy/qfaafYlkDkXNhtxMYNKdKogCaVSCejQY_Y4hy6D58vCB1eze37wdIGKdoAXpapOvPSf-IhiE5wOZKoisvRuQtXTqDZRFF4HFuhieyMQ',
                size: new google.maps.Size(20, 32),
                //origin: new google.maps.Point(0, 0),
                //anchor: new google.maps.Point(0, 32)
            },*/
            content:'<h1>Needham bruh School</h1>'
        },
        {
            coords:{lat:42.2715,lng:-71.2438},
            content:'<h2>joey home joey home</h2>'
        }
    ];

    for(var i = 0; i < markers.length; i++){
        addMarker(markers[i]);
    }

    function addMarker(props){
        var marker = new google.maps.Marker({
            position:props.coords,
            map:map,
        });

        if(props.iconImage){
            marker.setIcon(props.iconImage);
        }

        if(props.content){
            var infoWindow = new google.maps.InfoWindow({
                content:props.content
            });

            marker.addListener('click', function(){
                infoWindow.open(map, marker);
            });
        }
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
    localStorage.setItem("marker", latLng);
}