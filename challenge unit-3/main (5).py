
def linearSearchProduct(ProductList, targetProduct):
  indices = []

  for index, Product in enumerate(ProductList):
    if Product == targetProduct:
      indices.append(index)

  return indices


# Example usage:
Products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
target2 = "apple"
result = linearSearchProduct(Products, target)
print(result)