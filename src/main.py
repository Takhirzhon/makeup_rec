import configparser
from tabulate import tabulate
import data
from data import Product


def get_user_preferences(products):
    print("Enter your skin type (dry, oily, sensitive, combination):")
    skin_type = input().strip().lower()

    print("Enter your preferred brand:")
    brands = [brand.strip() for brand in input().split(',')]

    user_product = Product(brands[0], 'Any', [skin_type])
    matching_products = [product for product in products if product == user_product]

    return skin_type, brands





def sort_products(products, attribute='brand'):
    """
    Sorts the list of products based on the specified attribute.

    :param products: List of products to be sorted
    :param attribute: Attribute based on which the sorting will be done (default: 'brand')
    :return: Sorted list of products
    """
    return sorted(products, key=lambda x: getattr(x, attribute))



def display_recommendations(products):

    """
    Displays the recommended products for the user.

    :param products: List of products to be displayed
    :return: None
    """
    if products:
        print("Recommended products for you:")
        table = [[product.brand, ', '.join(product.suitable_for), product.product_type] for product in products]
        print(tabulate(table, headers=['Brand', 'Suitable For', 'Type'], tablefmt='grid'))
    else:
        print("No products found that match your criteria.")


def aggregate_product_data(products):
    
    """
    Aggregates product data to count the occurrence of each brand.

    :param products: List of products to be aggregated
    :return: Dictionary with brand as key and count as value
    """
    brand_count = {}
    for product in products:
        if product.brand in brand_count:
            brand_count[product.brand] += 1
        else:
            brand_count[product.brand] = 1
    return brand_count

def main():
    config = configparser.ConfigParser()
    config.read('../docs/config.ini')

    try:
        data_file = config['DEFAULT']['DataFilePath']
    except KeyError:
        print("'DataFilePath' not found in config file.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    products = data.load_data(data_file)  # Load product data from a JSON file

    skin_type, brands = get_user_preferences(products)  # Get user preferences and check against products

    # Filter products based on user preferences
    recommendations = [product for product in products if skin_type in product.suitable_for and any(
        brand.strip().lower() == product.brand.lower() for brand in brands)]

    sorted_recommendations = sort_products(recommendations)  # Sort the filtered recommendations

    display_recommendations(sorted_recommendations)  # Display the sorted recommendations

    brand_count = aggregate_product_data(products)  # Aggregate product data
    print("\nProduct availability by brand:")
    brand_table = [[brand, ', '.join(set(product.product_type for product in products if product.brand == brand)), count]
                   for brand, count in brand_count.items()]

    print(tabulate(brand_table, headers=['Brand', 'Type', 'Count'], tablefmt='grid'))

if __name__ == "__main__":
    main()
