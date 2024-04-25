import data

def get_user_preferences():
    print("Enter your skin type (dry, oily, sensitive, combination):")
    skin_type = input()
    print("Enter your preferred brands (comma-separated, e.g., BrandA, BrandB):")
    brands = input().split(',')
    return skin_type, brands

def sort_products(products, attribute='brand'):
    """Sort products based on a specified attribute."""
    return sorted(products, key=lambda x: getattr(x, attribute))

def display_recommendations(products):
    if products:
        print("Recommended products for you:")
        for product in products:
            print(f"- {product}")
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
    recommendations = [product for product in products if skin_type in product.suitable_for and product.brand in brands]
    sorted_recommendations = sort_products(recommendations)
    display_recommendations(sorted_recommendations)

    # Display aggregated data
    brand_count = aggregate_product_data(products)
    print("\nProduct availability by brand:")
    for brand, count in brand_count.items():
        print(f"{brand}: {count} products")

if __name__ == "__main__":
    main()
