document.getElementById('weather-form').addEventListener('submit', handleClick);


function handleClick(event) {
    event.preventDefault();
    var city = document.getElementById('city').value;
    if (city == "Current Location"){
        getCurrentLocation();
    } else if (city == "New York") {
        getWeather("OKX", 33, 35);
    } else if (city == "Boston") {
        getWeather("BOX", 71, 90);
    } else if (city == "Orlando") {
        getWeather("MLB", 26, 68);
    } else if (city == "Chicago") {
        getWeather("LOT", 76, 73);
    } else if (city == "Washington") {
        getWeather("LWX", 96, 72);
    } else if (city == "Atlanta") {
        getWeather("FFC", 51, 87);
    } else if (city == "Seattle") {
        getWeather("SEW", 125, 68);
    } else if (city == "San Francisco") {
        getWeather("MTR", 85, 105);
    } else if (city == "Los Angeles") {
        getWeather("LOX", 155, 45);
    } 
}
// Gets users current location and executes function depending on the result.
function getCurrentLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function (position) { success(position); },
            function (e) { unsuccess() },
            { enableHighAccuracy: true });
    } else { 
        var t = document.getElementById("coord");
        t.innerHTML = "&nbsp Geolocation is not supported by this browser.";
    }
}
// If getCurrentLocation() is successfull, makes a call with lat and lng.
function success(position) {
    var lat = position.coords.latitude;
    var lng = position.coords.longitude;
    var url = "https://api.weather.gov/points/" + lat + "," + lng;
    fetch(url)
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            // function returnParams returns offic, gridX, and gridY. Those values are passed to getWeather.
            locationInfo = returnParams(data);
            weather = getWeather(locationInfo[0], locationInfo[1], locationInfo[2]);
        })
        .catch(function(error) {
            console.log(error);
        });
}

function unsuccess() {
    var t = document.getElementById("weather-form");
    t.innerHTML = "&nbsp Geolocation was not allowed by the user. "+
                  "This may be a one-time refusal or you need to "+
                  "check the Location Services on your Settings.";
}
// Returns an array of values for office, gridX, and gridY
function returnParams(data) {
    if (data.type == "Feature") {
        var office = data.properties.cwa;
        var gridX = data.properties.gridX;
        var gridY = data.properties.gridY;
        return [office, gridX, gridY];

    } else {
        weatherInfo.innerHTML = '<p>Failed to retrieve weather information.</p>';
    }
}

function getWeather(office,gridX,gridY) {
    var url = 'https://api.weather.gov/gridpoints/' + office + '/' + gridX + "," + gridY + "/forecast";
    fetch(url)
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            displayWeather(data);
        })
        .catch(function(error) {
            console.log(error);
        });
}

function displayWeather(data) {
    var weatherInfo = document.getElementById('weather-info');
    weatherInfo.innerHTML = '';
    if (data.type === "Feature") {
        var period = data.properties.periods[0].name;
        var temperature = data.properties.periods[0].temperature;
        var trend = data.properties.periods[0].temperatureTrend;
        var humidity = data.properties.periods[0].relativeHumidity.value;
        var windSpeed = data.properties.periods[0].windSpeed;
        var direction = data.properties.periods[0].windDirection;
        var forecast = data.properties.periods[0].detailedForecast;
        var weatherHtml = '<h2>Weather Forecast for ' + period + '</h2>' +
            '<p>Temperature: ' + temperature + ' &#8451;</p>' +
            '<p>Humidity: ' + humidity + '%</p>' +
            '<p>Wind Speed: ' + windSpeed + ' m/s ' + direction + '</p>' +
            '<h3> Forecast </h3>' +
            '<p>' + forecast + '</p>';
        weatherInfo.innerHTML = weatherHtml;
    } else {
        weatherInfo.innerHTML = '<p>Failed to retrieve weather information.</p>';
    }
}