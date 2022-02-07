from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/money",
    tags=["Money"],
    responses={404: {"message": "Not found"}}
)

class Money(BaseModel):
    money_value: int
    money_amount: int
    money_type: str

money_db = [
	{
		"money_type":"coins",
		"money_value":1,
		"money_amount": 500
	},
	{
		"money_type":"coins",
		"money_value":5,
		"money_amount": 500
	},
	{
		"money_type":"coins",
		"money_value":10,
		"money_amount": 500
	},
	{
		"money_type":"banknotes",
		"money_value":20,
		"money_amount": 250
	},
	{
		"money_type":"banknotes",
		"money_value":50,
		"money_amount": 250
	},
	{
		"money_type":"banknotes",
		"money_value":100,
		"money_amount": 250
	},
	{
		"money_type":"banknotes",
		"money_value":500,
		"money_amount": 200
	},
	{
		"money_type":"banknotes",
		"money_value":1000,
		"money_amount": 150
	}
]

@router.get("/")
async def get_money():
    return money_db

@router.get("/type/{money_type}")
async def get_mony_by_type(money_type: str):
    typelist = []
    for x in money_db:
            if x['money_type'] == money_type:
               typelist.append(x)
    return typelist

@router.get("/value/{money_value}")
async def get_mony_by_value(money_value: int):
    match = next(m for m in money_db if m['money_value'] == money_value)
    print("------------------------")
    print(match)
    return match

@router.put("/")
async def update_money(money: Money):
    val = money.dict()
    money_value = val['money_value']
    for x in money_db:
        if x['money_value'] == money_value:
            x.update(val)
            break
    return money_db