import unittest
from pydantic import ValidationError
from .schemas import *
from .models import *
from datetime import date, time

#SCHEMAS TESTER :
class TestSchemas(unittest.TestCase):

    def test_customerIn_valid(self):
        customer = customerIn(
            type="individual",
            firstname="John",
            lastname="Doe",
            email="john.doe@example.com",
            website="https://example.com",
            workphone=1234567890,
            phone=9876543210,
            contact="primary"
        )
        self.assertEqual(customer.firstname, "John")

    def test_customerIn_invalid(self):
        with self.assertRaises(ValidationError):
            customerIn(
                type="individual",
                firstname="John",
                lastname="Doe",
                email="not-an-email",
                website="https://example.com",
                workphone="invalid-phone",
                phone=9876543210,
                contact="primary"
            )

    def test_SupplierIn_valid(self):
        supplier = SupplierIn(
            type="corporate",
            firstname="Jane",
            lastname="Doe",
            email="jane.doe@example.com",
            workphone=1234567890,
            phone=9876543210
        )
        self.assertEqual(supplier.firstname, "Jane")

    def test_categoryIn_valid(self):
        category = categoryIn(
            name="Electronics",
            description="Devices and gadgets"
        )
        self.assertEqual(category.name, "Electronics")

    def test_ItemIn_valid(self):
        item = ItemIn(
            name="Laptop",
            description="A powerful laptop",
            unit="piece",
            dimensions=15.6,
            weight=1.5,
            brand="BrandName",
            category_id=1
        )
        self.assertEqual(item.name, "Laptop")

    def test_WarehouseIn_valid(self):
        warehouse = WarehouseIn(
            name="Main Warehouse",
            address="1234 Warehouse St",
            city="Warehouse City",
            country="Countryland",
            area=1000.5,
            capacity=500,
            openingtime=time(9, 0),
            closingtime=time(18, 0),
            type="storage"
        )
        self.assertEqual(warehouse.name, "Main Warehouse")

    def test_stockIn_valid(self):
        stock = stockIn(
            name="Stock A",
            item_id=1,
            warehouse_id=1,
            quantity=100
        )
        self.assertEqual(stock.name, "Stock A")

    def test_SalesIn_valid(self):
        sales = SalesIn(
            amount=100.0,
            date=date(2023, 6, 10),
            currency="USD",
            payment_method="credit card",
            item_id=1,
            quantity=1
        )
        self.assertEqual(sales.amount, 100.0)

    def test_purchaseIn_valid(self):
        purchase = purchaseIn(
            amount=200.0,
            date=date(2023, 6, 10),
            currency="USD",
            payment_method="bank transfer",
            item_id=1,
            quantity=2
        )
        self.assertEqual(purchase.amount, 200.0)

    def test_paymentIn_valid(self):
        payment = paymentIn(
            amount=50.0,
            date=date(2023, 6, 10),
            currency="USD",
            payment_method="paypal",
            item_id=1,
            quantity=1
        )
        self.assertEqual(payment.amount, 50.0)

    def test_packagingIn_valid(self):
        packaging = packagingIn(
            id=1,
            type="Box",
            item_id=1,
            qty=10,
            weight=0.5,
            price=5.0,
            capacity=15.0,
            dimensions=30.0,
            unit="cm",
            storagespace=2
        )
        self.assertEqual(packaging.type, "Box")

    def test_PackagingMouvmentIn_valid(self):
        mouvment = PackagingMouvmentIn(
            id=1,
            name="Move A",
            packaging_id=1,
            mouvement="in",
            issue_fee=10
        )
        self.assertEqual(mouvment.name, "Move A")

    def test_OrderIn_valid(self):
        order = OrderIn(
            customer_id=1,
            packaging_id=1,
            item_id=1,
            order_date=date(2023, 6, 10),
            notes="Urgent delivery",
            item_price=100.0,
            returnablepackage_price=5.0,
            status="pending",
            order_number="ORD12345",
            shipping_address="1234 Street, City",
            total_amount=105.0,
            payment_method="credit card"
        )
        self.assertEqual(order.order_number, "ORD12345")

    def test_ShipmentIn_valid(self):
        shipment = ShipmentIn(
            packaging_id=1,
            tracking_number="TRACK12345",
            status="shipped"
        )
        self.assertEqual(shipment.tracking_number, "TRACK12345")

if __name__ == '__main__':
    unittest.main()

class TestOutSchemas(unittest.TestCase):

    def test_customerOut(self):
        customer = customerOut(
            id=1,
            type="individual",
            firstname="John",
            lastname="Doe",
            email="john.doe@example.com",
            website="https://example.com",
            workphone=1234567890,
            phone=9876543210,
            contact="primary"
        )
        self.assertEqual(customer.id, 1)
        self.assertEqual(customer.firstname, "John")

    def test_SupplierOut(self):
        supplier = SupplierOut(
            id=1,
            type="corporate",
            firstname="Jane",
            lastname="Doe",
            email="jane.doe@example.com",
            workphone=1234567890,
            phone=9876543210
        )
        self.assertEqual(supplier.id, 1)
        self.assertEqual(supplier.firstname, "Jane")

    def test_categoryOut(self):
        category = categoryOut(
            id=1,
            name="Electronics",
            description="Devices and gadgets"
        )
        self.assertEqual(category.id, 1)
        self.assertEqual(category.name, "Electronics")

    def test_ItemOut(self):
        item = ItemOut(
            id=1,
            name="Laptop",
            description="A powerful laptop",
            unit="piece",
            dimensions=15.6,
            weight=1.5,
            brand="BrandName",
            category_id=1
        )
        self.assertEqual(item.id, 1)
        self.assertEqual(item.name, "Laptop")

    def test_WarehouseOut(self):
        warehouse = WarehouseOut(
            id=1,
            name="Main Warehouse",
            address="1234 Warehouse St",
            city="Warehouse City",
            country="Countryland",
            area=1000.5,
            capacity=500,
            openingtime=time(9, 0),
            closingtime=time(18, 0),
            type="storage"
        )
        self.assertEqual(warehouse.id, 1)
        self.assertEqual(warehouse.name, "Main Warehouse")

    def test_stockOut(self):
        stock = stockOut(
            id=1,
            name="Stock A",
            item_id=1,
            warehouse_id=1,
            quantity=100
        )
        self.assertEqual(stock.id, 1)
        self.assertEqual(stock.name, "Stock A")

    def test_SalesOut(self):
        sales = SalesOut(
            id=1,
            amount=100.0,
            date=date(2023, 6, 10),
            currency="USD",
            payment_method="credit card",
            item_id=1,
            quantity=1
        )
        self.assertEqual(sales.id, 1)
        self.assertEqual(sales.amount, 100.0)

    def test_purchaseOut(self):
        purchase = purchaseOut(
            id=1,
            amount=200.0,
            date=date(2023, 6, 10),
            currency="USD",
            payment_method="bank transfer",
            item_id=1,
            quantity=2
        )
        self.assertEqual(purchase.id, 1)
        self.assertEqual(purchase.amount, 200.0)

    def test_paymentOut(self):
        payment = paymentOut(
            id=1,
            amount=50.0,
            date=date(2023, 6, 10),
            currency="USD",
            payment_method="paypal",
            item_id=1,
            quantity=1
        )
        self.assertEqual(payment.id, 1)
        self.assertEqual(payment.amount, 50.0)

    def test_packagingOut(self):
        packaging = packagingOut(
            id=1,
            type="Box",
            item_id=1,
            qty=10,
            weight=0.5,
            price=5.0,
            capacity=15.0,
            dimensions=30.0,
            storagespace=2
        )
        self.assertEqual(packaging.id, 1)
        self.assertEqual(packaging.type, "Box")

    def test_PackagingMouvmentOut(self):
        mouvment = PackagingMouvmentOut(
            id=1,
            name="Move A",
            packaging_id=1,
            mouvement="in",
            issue_fee=10.0,
            issue_bill=50.0
        )
        self.assertEqual(mouvment.id, 1)
        self.assertEqual(mouvment.name, "Move A")

    def test_OrderOut(self):
        order = OrderOut(
            id=1,
            customer_id=1,
            packaging_id=1,
            item_id=1,
            order_date=date(2023, 6, 10),
            notes="Urgent delivery",
            item_price=100.0,
            returnablepackage_price=5.0,
            status="pending",
            order_number="ORD12345",
            shipping_address="1234 Street, City",
            total_amount=105.0,
            payment_method="credit card"
        )
        self.assertEqual(order.id, 1)
        self.assertEqual(order.order_number, "ORD12345")

    def test_ShipmentOut(self):
        shipment = ShipmentOut(
            id=1,
            packaging_id=1,
            tracking_number="TRACK12345",
            status="shipped"
        )
        self.assertEqual(shipment.id, 1)
        self.assertEqual(shipment.tracking_number, "TRACK12345")

    def test_shipmentmouvmentOut(self):
        shipment_mouvment = shipmentmouvmentOut(
            status="in transit",
            packaging_id=1
        )
        self.assertEqual(shipment_mouvment.status, "in transit")
        self.assertEqual(shipment_mouvment.packaging_id, 1)


if __name__ == '__main__':
    unittest.main()



from django.test import TestCase

#MODELS TESTER :
class ModelTestCase(TestCase):
    
    def setUp(self):
        self.customer = Customer.objects.create(
            type="individual",
            firstname="John",
            lastname="Doe",
            email="john.doe@example.com",
            website="https://example.com",
            workphone=1234567890,
            phone=9876543210,
            contact="primary"
        )
        self.supplier = Supplier.objects.create(
            type="corporate",
            firstname="Jane",
            lastname="Doe",
            email="jane.doe@example.com",
            workphone=1234567890,
            phone=9876543210
        )
        self.category = Category.objects.create(
            name="Electronics",
            description="Devices and gadgets"
        )
        self.item = Item.objects.create(
            name="Laptop",
            description="A powerful laptop",
            unit="piece",
            dimensions=15.6,
            weight=1.5,
            brand="BrandName",
            category=self.category
        )
        self.warehouse = Warehouse.objects.create(
            name="Main Warehouse",
            address="1234 Warehouse St",
            city="Warehouse City",
            country="Countryland",
            area=1000.5,
            capacity=500,
            openingtime="09:00:00",
            closingtime="18:00:00",
            type="storage"
        )
        self.stock = Stock.objects.create(
            name="Stock A",
            item=self.item,
            warehouse=self.warehouse,
            quantity=100,
            customer=self.customer
        )
        self.packaging = Packaging.objects.create(
            type="Box",
            item=self.item,
            quantity=10,
            weight=0.5,
            price=5.0,
            capacity=15.0,
            dimensions=30.0,
            unit="cm",
            storagespace=2.0
        )

    def test_customer_creation(self):
        self.assertEqual(self.customer.type, "individual")
        self.assertEqual(self.customer.firstname, "John")

    def test_supplier_creation(self):
        self.assertEqual(self.supplier.type, "corporate")
        self.assertEqual(self.supplier.firstname, "Jane")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Electronics")
        self.assertEqual(self.category.description, "Devices and gadgets")

    def test_item_creation(self):
        self.assertEqual(self.item.name, "Laptop")
        self.assertEqual(self.item.unit, "piece")
        self.assertEqual(self.item.category.name, "Electronics")

    def test_warehouse_creation(self):
        self.assertEqual(self.warehouse.name, "Main Warehouse")
        self.assertEqual(self.warehouse.city, "Warehouse City")
        self.assertEqual(self.warehouse.capacity, 500)
    
    def test_stock_creation(self):
        self.assertEqual(self.stock.name, "Stock A")
        self.assertEqual(self.stock.item.name, "Laptop")
        self.assertEqual(self.stock.warehouse.name, "Main Warehouse")
        self.assertEqual(self.stock.quantity, 100)
        self.assertEqual(self.stock.customer.firstname, "John")

    def test_packaging_creation(self):
        self.assertEqual(self.packaging.type, "Box")
        self.assertEqual(self.packaging.item.name, "Laptop")
        self.assertEqual(self.packaging.quantity, 10)
        self.assertEqual(self.packaging.weight, 0.5)
        self.assertEqual(self.packaging.price, 5.0)
        self.assertEqual(self.packaging.capacity, 15.0)
        self.assertEqual(self.packaging.dimensions, 30.0)
        self.assertEqual(self.packaging.unit, "cm")
        self.assertEqual(self.packaging.storagespace, 2.0)
    
    def test_sales_creation(self):
        sales = Sales.objects.create(
            amount=100.0,
            date="2023-06-10",
            currency="USD",
            payment_method="credit card",
            item=self.item,
            quantity=1
        )
        self.assertEqual(sales.amount, 100.0)
        self.assertEqual(sales.currency, "USD")

    def test_purchase_creation(self):
        purchase = Purchase.objects.create(
            amount=200.0,
            date="2023-06-10",
            currency="USD",
            payment_method="bank transfer",
            item=self.item,
            quantity=2
        )
        self.assertEqual(purchase.amount, 200.0)
        self.assertEqual(purchase.currency, "USD")

    def test_payment_creation(self):
        payment = Payment.objects.create(
            amount=50.0,
            date="2023-06-10",
            currency="USD",
            payment_method="paypal",
            item=self.item,
            quantity=1
        )
        self.assertEqual(payment.amount, 50.0)
        self.assertEqual(payment.currency, "USD")

    def test_packagingmouvment_creation(self):
        packaging_mouvment = PackagingMouvment.objects.create(
            name="Move A",
            packaging=self.packaging,
            mouvement="in",
            issue_fee=10.0,
            issue_bill=50.0
        )
        self.assertEqual(packaging_mouvment.name, "Move A")
        self.assertEqual(packaging_mouvment.mouvement, "in")

    def test_order_creation(self):
        order = Order.objects.create(
            customer=self.customer,
            packaging=self.packaging,
            item=self.item,
            order_date="2023-06-10",
            notes="Urgent delivery",
            item_price=100.0,
            returnablepackage_price=5.0,
            status="pending",
            order_number="ORD12345",
            shipping_address="1234 Street, City",
            total_amount=105.0,
            payment_method="credit card"
        )
        self.assertEqual(order.order_number, "ORD12345")
        self.assertEqual(order.status, "pending")

    def test_shipment_creation(self):
        shipment = Shipment.objects.create(
            packaging=self.packaging,
            tracking_number="TRACK12345",
            status="shipped"
        )
        self.assertEqual(shipment.tracking_number, "TRACK12345")
        self.assertEqual(shipment.status, "shipped")

if __name__ == '__main__':
    unittest.main()


