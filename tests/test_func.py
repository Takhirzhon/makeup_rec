import unittest
from unittest.mock import patch, MagicMock
import os
import sys
sys.path.append(os.path.abspath('../src'))
from main import get_user_preferences, sort_products, aggregate_product_data

class TestProductApp(unittest.TestCase):

    # Test for get_user_preferences
    def test_get_user_preferences(self):
        with patch('builtins.input', side_effect=['dry', 'CeraVe, Lamer']) as mock_input:
            skin_type, brands = get_user_preferences()
            self.assertEqual(mock_input.call_count, 2)
            self.assertEqual(skin_type, 'dry')
            self.assertEqual(brands, ['CeraVe', 'Lamer'])

# If you want to include the test in the TestProductApp class, make sure to indent properly.

    # Test for sort_products
    def test_sort_products(self):
        products = [
            MagicMock(brand='CeraVe', product_type='Moisturizer'),
            MagicMock(brand='Avene', product_type='Sunscreen'),
            MagicMock(brand='Beauty of Joseon', product_type='Moisturizer')
        ]
        sorted_by_brand = sort_products(products, 'brand')
        self.assertEqual([p.brand for p in sorted_by_brand], ['Avene', 'Beauty of Joseon', 'CeraVe'])

    # Test for aggregate_product_data
    def test_aggregate_product_data(self):
        products = [
            MagicMock(brand='CeraVe'),
            MagicMock(brand='Lamer'),
            MagicMock(brand='CeraVe')
        ]
        brand_count = aggregate_product_data(products)
        self.assertEqual(brand_count, {'CeraVe': 2, 'Lamer': 1})

if __name__ == '__main__':
    unittest.main()
