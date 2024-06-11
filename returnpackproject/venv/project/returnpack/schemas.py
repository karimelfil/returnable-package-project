from ninja import Schema
from pydantic import BaseModel
from typing import List
from datetime import date ,time

class customerIn(BaseModel):
    type: str
    firstname: str
    lastname: str
    email: str
    website: str
    workphone: int
    phone: int
    contact: str

class customerOut(Schema):
    id : int
    type: str
    firstname: str
    lastname: str
    email: str 
    website: str 
    workphone: int
    phone: int 
    contact: str = None

class SupplierIn(BaseModel):
    type : str
    firstname : str
    lastname : str
    email : str 
    workphone : int
    phone : int 

class SupplierOut(Schema):
    id : int
    type : str
    firstname : str
    lastname : str
    email : str 
    workphone : int
    phone : int 

class categoryIn(BaseModel):
    name: str
    description : str

class categoryOut(Schema):
    id : int
    name: str
    description : str   

class ItemIn(BaseModel):
    name : str
    description : str
    unit : str
    dimensions: float
    weight : float
    brand : str
    category_id : int

class ItemOut(Schema):
    id : int
    name : str
    description : str
    unit : str
    dimensions : float
    weight : float
    brand : str
    category_id : int

class WarehouseIn(BaseModel):
    name: str
    address: str
    city: str
    country: str
    area: float
    capacity: int
    openingtime: time
    closingtime: time
    type: str  

class WarehouseOut(BaseModel):
    id: int
    name: str
    address: str
    city: str
    country: str
    area: float
    capacity: int
    openingtime: time
    closingtime: time
    type: str

class stockIn(BaseModel):
    name: str
    item_id: int
    warehouse_id: int
    quantity: int

class stockOut(Schema) :
    id : int
    name : str
    item_id : int
    warehouse_id : int 
    quantity: int


class SalesIn(BaseModel):
    amount: float
    date: date
    currency: str
    payment_method: str
    item_id: int
    quantity: int

class SalesOut(BaseModel):
    id : int
    amount: float
    date: date
    currency: str
    payment_method: str
    item_id: int
    quantity: int

class purchaseIn(BaseModel):
    amount: float
    date: date
    currency: str
    payment_method: str
    item_id: int
    quantity: int

class purchaseOut(Schema):
    id : int
    amount: float
    date: date
    currency: str
    payment_method: str
    item_id: int
    quantity: int

class paymentIn(BaseModel):
    amount: float
    date: date
    currency: str
    payment_method: str
    item_id: int
    quantity: int

class paymentOut(Schema):
    id : int
    amount: float
    date: date
    currency: str
    payment_method: str
    item_id: int
    quantity: int

class PackagingCountOut(BaseModel):
    item_id: int
    quantity: int

class packagingIn(BaseModel):
    id : int
    type: str
    item_id: int
    qty: int
    weight: float
    price: float
    capacity: float
    dimensions: float
    unit: str
    storagespace: int

class packagingOut(BaseModel):
    id : int
    type : str
    item_id : int
    qty : int
    weight : float
    price : float
    capacity : float
    dimensions : float
    storagespace : int 

class PackagingMouvmentIn(BaseModel):
    id : int
    name: str
    packaging_id: int
    mouvement: str
    issue_fee : int


class PackagingMouvmentOut(BaseModel):
    id : int
    name: str
    packaging_id: int
    mouvement: str
    issue_fee : float
    issue_bill : float
  
class OrderIn(BaseModel):
    customer_id: int
    packaging_id: int
    item_id: int
    order_date: date
    notes: str
    item_price: float
    returnablepackage_price: float
    status: str 
    order_number: str
    shipping_address: str
    total_amount: float
    payment_method: str

class OrderOut(BaseModel):
    id: int
    customer_id: int
    packaging_id: int
    item_id: int
    order_date: date
    notes: str
    item_price: float
    returnablepackage_price: float
    status: str
    order_number: str
    shipping_address: str
    total_amount: float
    payment_method: str

class ShipmentIn(BaseModel):
    packaging_id:int 
    tracking_number: str
    status: str

class ShipmentOut(BaseModel):
    id : int
    packaging_id:int 
    tracking_number: str
    status: str



class shipmentmouvmentOut(BaseModel):
    status: str
    packaging_id:int 