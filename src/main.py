import data
from tabulate import tabulate

def get_user_preferences():
    print("Enter your skin type (dry, oily, sensitive, combination):")
    skin_type = input().strip().lower()
    print("Enter your preferred brand:")
    brands = [brand.strip() for brand in input().split(',')]
    return skin_type, brands

def sort_products(products, attribute='brand'):
    """Sort products based on a specified attribute."""
    return sorted(products, key=lambda x: getattr(x, attribute))

def display_recommendations(products):
    if products:
        print("Recommended products for you:")
        table = [[product.brand, ', '.join(product.suitable_for)] for product in products]
        print(tabulate(table, headers=['Brand', 'Suitable For'], tablefmt='grid'))
    else:
        print("No products found that match your criteria.")

def aggregate_product_data(products):
    """Aggregates products to count how many are available for each brand."""
    brand_count = {}
    for product in products:
        if product.brand in brand_count:
            brand_count[product.brand] += 1
        else:
            brand_count[product.brand] = 1
    return brand_count

def main():
    products = data.load_data()
    skin_type, brands = get_user_preferences()
    recommendations = [product for product in products if skin_type in product.suitable_for and any(brand.strip().lower() == product.brand.lower() for brand in brands)]
    sorted_recommendations = sort_products(recommendations)
    display_recommendations(sorted_recommendations)

    # Display aggregated data
    brand_count = aggregate_product_data(products)
    print("\nProduct availability by brand:")
    brand_table = [[brand, count] for brand, count in brand_count.items()]
    print(tabulate(brand_table, headers=['Brand', 'Count'], tablefmt='grid'))

if __name__ == "__main__":
    main()
