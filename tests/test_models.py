"""Tests for ERP data models"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from erpx.models.resource import Resource
from erpx.models.inventory import InventoryItem
from erpx.models.transaction import Transaction, TransactionType


def test_resource_creation():
    """Test resource creation and basic operations"""
    resource = Resource(
        id="r001",
        name="Test Resource",
        type="test",
        utilization=50.0
    )
    
    assert resource.id == "r001"
    assert resource.name == "Test Resource"
    assert resource.is_available() == True
    assert resource.utilization == 50.0


def test_resource_utilization_update():
    """Test updating resource utilization"""
    resource = Resource(id="r001", name="Test", type="test")
    
    resource.update_utilization(75.0)
    assert resource.utilization == 75.0
    
    try:
        resource.update_utilization(150.0)
        assert False, "Should raise ValueError for invalid utilization"
    except ValueError:
        pass


def test_inventory_item_creation():
    """Test inventory item creation"""
    item = InventoryItem(
        id="i001",
        name="Test Item",
        category="test",
        quantity=15,
        reorder_point=10
    )
    
    assert item.id == "i001"
    assert item.quantity == 15
    assert item.needs_reorder() == False


def test_inventory_needs_reorder():
    """Test inventory reorder detection"""
    item = InventoryItem(
        id="i001",
        name="Test Item",
        category="test",
        quantity=5,
        reorder_point=10
    )
    
    assert item.needs_reorder() == True


def test_inventory_quantity_update():
    """Test inventory quantity updates"""
    item = InventoryItem(
        id="i001",
        name="Test Item",
        category="test",
        quantity=20
    )
    
    item.update_quantity(10)
    assert item.quantity == 30
    
    item.update_quantity(-15)
    assert item.quantity == 15
    
    try:
        item.update_quantity(-30)
        assert False, "Should raise ValueError for negative quantity"
    except ValueError:
        pass


def test_inventory_value_calculation():
    """Test inventory value calculation"""
    item = InventoryItem(
        id="i001",
        name="Test Item",
        category="test",
        quantity=10,
        unit_cost=50.0
    )
    
    assert item.calculate_value() == 500.0


def test_transaction_creation():
    """Test transaction creation"""
    transaction = Transaction(
        id="t001",
        type=TransactionType.PURCHASE,
        amount=1000.0,
        description="Test transaction"
    )
    
    assert transaction.id == "t001"
    assert transaction.type == TransactionType.PURCHASE
    assert transaction.status == "pending"


def test_transaction_completion():
    """Test transaction completion"""
    transaction = Transaction(
        id="t001",
        type=TransactionType.SALE,
        amount=500.0,
        description="Test"
    )
    
    transaction.complete()
    assert transaction.status == "completed"
    assert transaction.completed_at is not None


if __name__ == "__main__":
    test_resource_creation()
    test_resource_utilization_update()
    test_inventory_item_creation()
    test_inventory_needs_reorder()
    test_inventory_quantity_update()
    test_inventory_value_calculation()
    test_transaction_creation()
    test_transaction_completion()
    print("All model tests passed!")
