import requests

def get_food_information():
    product = input("Enter the food you would like to know about: ")
    url = f"https://world.openfoodfacts.org/api/v2/product/{product}.json"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses (4xx and 5xx)
        data = response.json()
        display_food_information(data)
    except requests.exceptions.RequestException as error:
        print(f"Error fetching data: {error}")

def display_food_information(data):
    if 'product' in data and 'nutriments' in data['product']:
        product = data['product']
        serving_size = product.get('serving_size', 'N/A')
        protein = product['nutriments'].get('proteins', 'N/A')
        fat = product['nutriments'].get('fat', 'N/A')
        carbohydrates = product['nutriments'].get('carbohydrates', 'N/A')
        saturated_fat = product['nutriments'].get('saturated-fat', 'N/A')
        fiber = product['nutriments'].get('fiber', 'N/A')
        sugar = product['nutriments'].get('sugars', 'N/A')

        food_information = (
            f"The food information for {product['product_name']}:\n"
            f"Serving Size: {serving_size}\n"
            f"Protein: {protein}\n"
            f"Fat: {fat}\n"
            f"Carbohydrates: {carbohydrates}\n"
            f"Saturated Fats: {saturated_fat}\n"
            f"Fiber: {fiber}\n"
            f"Sugar: {sugar}"
        )

        print(food_information)
    else:
        print("Product information is incomplete or missing.")

get_food_information()