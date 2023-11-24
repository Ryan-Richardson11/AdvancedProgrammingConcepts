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
    if (data.product && data.product.nutriments) {
        console.log(data)
        var product = data.product;
        var servingSize = product.serving_size;
        var protein = product.nutriments.proteins;
        var fat = product.nutriments.fat;
        var carbohydrates = product.nutriments.carbohydrates;
        var saturatedFat = product.nutriments.saturated-fat;
        var fiber = product.nutriments.fiber;
        var Sugar = product.nutriments.sugars;

        var foodInformation = "The food information for " + data.product + ":\n" +
                            "Serving Size: " + (servingSize || "N/A") + "\n" +
                            "Protein: " + (protein || "N/A") + "\n" +
                            "Fat: " + (fat || "N/A") + "\n" +
                            "Carbohydrates: " + (carbohydrates || "N/A") +
                            "Saturated Fats: " + (saturatedFat || "N/A") +
                            "Fiber: " + (fiber || "N/A") +
                            "Sugar: " + (Sugar || "N/A");

        console.log(foodInformation);
    } else {
        console.log("Product information is incomplete or missing.");
    }
}

getFoodInformation();