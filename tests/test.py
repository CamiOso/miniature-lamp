def calculate_total(products):
    total=0
    for producto in products:
        total+=producto["price"]
    return total
    
def test_calculate_total_with_empty_list():
    print("prueba")
    assert calculate_total([])==0

def test_calculate_total_with_single_product():
    products = [
        {
            "name": "Book1",
            "price": 50
        }
    ]
    print(calculate_total(products))
    assert calculate_total(products) ==10


def test_calculate_total_with_multiple_product():
    products = [
        {
            "name": "Book1",
            "price": 20
        },
        {
            "name": "Pencil",
            "price": 15
        }
    ]
    print(calculate_total(products))
    assert calculate_total(products) ==60



if __name__=="__main__":
    test_calculate_total_with_multiple_product()
    