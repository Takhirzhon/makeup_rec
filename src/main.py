import configparser
from tabulate import tabulate
import data

def get_user_preferences():
    """
    Prompts the user to input their skin type and preferred brand(s) and returns the input values.

    :return: Tuple containing user's skin type and list of preferred brands
    """

def get_user_preferences():
    print("Enter your skin type (dry, oily, sensitive, combination):")
    skin_type = input().strip().lower()

    print("Enter your preferred brand:")
    brands = [brand.strip() for brand in input().split(',')]

    return skin_type, brands

def sort_products(products, attribute='brand'):
    """
    Sorts the list of products based on the specified attribute.

    :param products: List of products to be sorted
    :param attribute: Attribute based on which the sorting will be done (default: 'brand')
    :return: Sorted list of products
    """

def sort_products(products, attribute='brand'):
    return sorted(products, key=lambda x: getattr(x, attribute))

def display_recommendations(products):
    """
    Displays the recommended products for the user.

    :param products: List of products to be displayed
    :return: None
    """

def display_recommendations(products):
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

def aggregate_product_data(products):
    brand_count = {}
    for product in products:
        if product.brand in brand_count:
            brand_count[product.brand] += 1
        else:
            brand_count[product.brand] = 1
    return brand_count

def main():
    """
    The main function reads the configuration file, extracts the DataFilePath,
    and handles any potential errors that may occur during the process.

    :return: None
    """

def main():
    config = configparser.ConfigParser()
    config.read('../docs/config.ini')

    try:
        # Attempt to read the 'DataFilePath' from the configuration file
        data_file = config['DEFAULT']['DataFilePath']
    except KeyError:
        # Handle KeyError if 'DataFilePath' is not found in the configuration file
        print("'DataFilePath' not found in config file.")
        return
    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"An error occurred: {e}")
        return


    #Load data from data_file
    products = data.load_data(data_file)

    #Get user preferences for skin type and preferred brands
    skin_type, brands = get_user_preferences()

    #Filter products based on user preferences
    recommendations = [product for product in products
                       if skin_type in product.suitable_for and any(
            brand.strip().lower() == product.brand.lower() for brand in brands)]

    #Sort the filtered recommendations
    sorted_recommendations = sort_products(recommendations)

    #Display the sorted recommendations
    display_recommendations(sorted_recommendations)

    # Aggregate product data and display product availability by brand
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
