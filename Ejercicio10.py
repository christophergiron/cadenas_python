products = input("Introduce your products in your cart separate with a comma: ")
cart = products.split(',')
for products in cart:
    print(products.strip())
