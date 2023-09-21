def linear_search_product(products, target_product):
    indices = []
    for i, product in enumerate(products):
        if product == target_product:
            indices.append(i)
    return indices

# Example usage:
products = ["Apple", "Banana", "Orange", "Apple", "Grapes"]
target = "Apple"
result = linear_search_product(products, target)
if result:
    print(f"{target} found at indices: {result}")
else:
    print(f"{target} not found in the list.")
  