from api.product import get_products
from utils.formatter import format_data

products = get_products()
result = format_data(products)
print(result)
