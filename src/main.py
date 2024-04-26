import configparser
from tabulate import tabulate
import data

def get_user_preferences():
    print("Enter your skin type (dry, oily, sensitive, combination):")
    skin_type = input().strip().lower()
    print("Enter your preferred brand:")
    brands = [brand.strip() for brand in input().split(',')]
    return skin_type, brands

def sort_products(products, attribute='brand'):
    return sorted(products, key=lambda x: getattr(x, attribute))

def display_recommendations(products):
    if products:
        print("Recommended products for you:")
        table = [[product.brand, ', '.join(product.suitable_for), product.product_type] for product in products]
        print(tabulate(table, headers=['Brand', 'Suitable For', 'Type'], tablefmt='grid'))
    else:
        print("No products found that match your criteria.")

def aggregate_product_data(products):
    brand_count = {}
    for product in products:
        if product.brand in brand_count:
            brand_count[product.brand] += 1
        else:
            brand_count[product.brand] = 1
    return brand_count

def main():
    config = configparser.ConfigParser()
    config.read('./docs/config.ini') 
    try:
        data_file = config['DEFAULT']['DataFilePath']
    except KeyError:
        print("Error: 'DataFilePath' not found in configuration file.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    products = data.load_data(data_file)
    skin_type, brands = get_user_preferences()
    recommendations = [product for product in products if skin_type in product.suitable_for and any(brand.strip().lower() == product.brand.lower() for brand in brands)]
    sorted_recommendations = sort_products(recommendations)
    display_recommendations(sorted_recommendations)

    brand_count = aggregate_product_data(products)
    print("\nProduct availability by brand:")
    brand_table = []
    for brand, count in brand_count.items():
        products_for_brand = [product for product in products if product.brand == brand]
        types_for_brand = ', '.join(set(product.product_type for product in products_for_brand))
        brand_table.append([brand, types_for_brand, count])

    print(tabulate(brand_table, headers=['Brand', 'Type', 'Count'], tablefmt='grid'))

if __name__ == "__main__":
    main()
