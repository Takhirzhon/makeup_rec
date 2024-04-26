import unittest
from unittest.mock import patch, MagicMock
import sys
sys.path.append('../src')
from main import get_user_preferences, sort_products, aggregate_product_data

class TestProductApp(unittest.TestCase):

    # Test for get_user_preferences
    def test_get_user_preferences(self):
        with patch('builtins.input', side_effect=['oily', 'BrandX, BrandY']) as mock_input:
            skin_type, brands = get_user_preferences()
            self.assertEqual(mock_input.call_count, 2)
            self.assertEqual(skin_type, 'oily')
            self.assertEqual(brands, ['BrandX', 'BrandY'])

# If you want to include the test in the TestProductApp class, make sure to indent properly.

    # Test for sort_products
    def test_sort_products(self):
        products = [
            MagicMock(brand='C', product_type='Gel'),
            MagicMock(brand='A', product_type='Serum'),
            MagicMock(brand='B', product_type='Cream')
        ]
        sorted_by_brand = sort_products(products, 'brand')
        self.assertEqual([p.brand for p in sorted_by_brand], ['A', 'B', 'C'])

    # Test for aggregate_product_data
    def test_aggregate_product_data(self):
        products = [
            MagicMock(brand='BrandX'),
            MagicMock(brand='BrandY'),
            MagicMock(brand='BrandX')
        ]
        brand_count = aggregate_product_data(products)
        self.assertEqual(brand_count, {'BrandX': 2, 'BrandY': 1})

if __name__ == '__main__':
    unittest.main()
