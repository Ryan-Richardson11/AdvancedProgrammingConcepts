function getFoodInformation(product) {
    var url = "https://world.openfoodfacts.org/api/v2/product/" + product + ".json";
    fetch(url)
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            displayFoodInformation(data);
        })
        .catch(function(error) {
            console.log(error);
        });
}

function handleClick(event) {
    var food = document.getElementById("food").value
    if (food == "Nutella") {
        getFoodInformation("3017620429484");
    } else if (food == "Peanut Butter") {
        getFoodInformation("0037600106009");
    } else if (food == "Eggs") {
        getFoodInformation("3270190205685");
    } else if (food == "Bread") {
        getFoodInformation("3760049790214");
    } else if (food == "Almonds") {
        getFoodInformation("20724696");
    } else if (food == "Pasta") {
        getFoodInformation("8076802085738")
    }
}

function displayFoodInformation(data) {
    var foodInfo = document.getElementById("food-info")
    foodInfo.innerHTML = '';
    if ('product' in data && 'nutriments' in data['product']) {
        var product = data['product'];
        var servingSize = product['nutriments']['serving_size']
        var protein = product['nutriments']['proteins'];
        var fat = product['nutriments']['fat'];
        var carbohydrates = product['nutriments']['carbohydrates'];
        var saturatedFat = product['nutriments']['saturated-fat'];
        var fiber = product['nutriments']['fiber'];
        var Sugar = product['nutriments']['sugars'];

        var foodHtml = "<h2>The food information for " + product['product_name'] + ":</h2>\n" +
                            "<p>Serving Size: " + (servingSize || "N/A") + "</p>\n" +
                            "<p>Protein: " + (protein || "N/A") + "</p>\n" +
                            "<p>Fat: " + (fat || "N/A") + "</p>\n" +
                            "<p>Carbohydrates: " + (carbohydrates || "N/A") + "</p>\n" +
                            "<p>Saturated Fats: " + (saturatedFat || "N/A") + "</p>\n" +
                            "<p>Fiber: " + (fiber || "N/A") + "</p>\n" +
                            "<p>Sugar: " + (Sugar || "N/A") + "</p>";

        foodInfo.innerHTML = foodHtml;
    } else {
        foodInfo.innerHTML = "<p>Failed to retrieve food information.</p>";
    }
}