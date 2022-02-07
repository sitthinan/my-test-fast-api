from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/product",
    tags=["Product"],
    responses={404: {"message": "Not found"}}
)

class Product(BaseModel):
    product_id: int
    product_name: str
    product_price: float
    product_amount: int

products_db = [
	{
		"product_id":1,
		"product_name":"OISHI Gyoza",
		"product_price": 49,
		"product_amount": 20,
	},
	{
		"product_id":2,
		"product_name":"OISHI Bread Pan",
		"product_price":20,
		"product_amount":13,
	},
	{
		"product_id":3,
		"product_name":"Lays Salt & Vinegar",
		"product_price":20,
		"product_amount":6,
	},
	{
		"product_id":4,
		"product_name":"Pepsi",
		"product_price":19,
		"product_amount":7,
	},
	{
		"product_id":5,
		"product_name":"Cheetos Cheese",
		"product_price":20,
		"product_amount":16,
	},
	{
		"product_id":6,
		"product_name":"Mars Chocolate",
		"product_price":32,
		"product_amount":26,
	},
	{
		"product_id":7,
		"product_name":"Ayran Yogurt",
		"product_price":13,
		"product_amount":2,
	},
	{
		"product_id":8,
		"product_name":"Kit Kat",
		"product_price":23,
		"product_amount":29,
	},
	{
		"product_id":9,
		"product_name":"OISHI Green Tea Lemon",
		"product_price":20,
		"product_amount":9,
	},
	{
		"product_id":10,
		"product_name":"Cheetos Colmillos",
		"product_price":20,
		"product_amount":7,
	},
	{
		"product_id":11,
		"product_name":"Rusk Misk & Elaichi",
		"product_price":39,
		"product_amount":26,
	},
	{
		"product_id":12,
		"product_name":"Chicharrones",
		"product_price":49,
		"product_amount":30,
	},
	{
		"product_id":13,
		"product_name":"Besty Soya Garlic Bhel",
		"product_price":20,
		"product_amount":13,
	},
	{
		"product_id":14,
		"product_name":"Sprite",
		"product_price":14,
		"product_amount":6,
	},
	{
		"product_id":15,
		"product_name":"Coca Cola",
		"product_price":14,
		"product_amount":7,
	},
	{
		"product_id":16,
		"product_name":"Schweppes Agrum",
		"product_price":14,
		"product_amount":8,
	},
	{
		"product_id":17,
		"product_name":"OISHI shrimp Gyoza ",
		"product_price":49,
		"product_amount":11,
	},
	{
		"product_id":18,
		"product_name":"OISHI Takoyaki",
		"product_price":42,
		"product_amount":9,
	},
	{
		"product_id":19,
		"product_name":"OISHI Potato Chips",
		"product_price":20,
		"product_amount":19,
	},{
		"product_id":20,
		"product_name":"OISHI Green Tea lychee",
		"product_price":25,
		"product_amount":22,
	},{
		"product_id":21,
		"product_name":"Pocky",
		"product_price":20,
		"product_amount":10,
	}

]

@router.get("/")
async def get_products():
    return products_db

@router.get("/{product_id}")
async def get_product_by_id(product_id: int):
    match = next(product for product in products_db if product['product_id'] == product_id)
    return match

@router.put("/")
async def update_product(product: Product):
    val = product.dict()
    product_id = val['product_id']
    for x in products_db:
        if x['product_id'] == product_id:
            x.update(val)
            break
    return products_db

@router.post("")
async def add_product(product: Product):
    products_db.append(product.dict())
    return products_db

@router.delete("/{product_id}")
async def delete_product(product_id: int):
    for x in products_db:
        print(x)
        if x['product_id'] == product_id:
             products_db.remove(x)
             break
    return  products_db
