function getFoodInformation(product) {
    var url = "https://world.openfoodfacts.org/api/v2/" + product + "/737628064502.json"
    fetch(url)
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            diplayFoodInformation(data);
        })
        .catch(function(error) {
            console.log(error);
        });
}
