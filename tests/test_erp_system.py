"""Tests for main ERP system"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from erpx.core.erp_system import ERPSystem
from erpx.models.resource import Resource
from erpx.models.inventory import InventoryItem
from erpx.models.transaction import Transaction, TransactionType


def test_erp_system_initialization():
    """Test ERP system initialization"""
    erp = ERPSystem(company_name="Test Company")
    
    assert erp.company_name == "Test Company"
    assert len(erp.resources) == 0
    assert len(erp.inventory) == 0
    assert len(erp.transactions) == 0
    assert erp.recommender is not None


def test_add_and_get_resource():
    """Test adding and retrieving resources"""
    erp = ERPSystem()
    
    resource = Resource(
        id="r001",
        name="Test Resource",
        type="test"
    )
    
    erp.add_resource(resource)
    
    assert len(erp.get_all_resources()) == 1
    assert erp.get_resource("r001") is not None
    assert erp.get_resource("r001").name == "Test Resource"


def test_add_and_get_inventory():
    """Test adding and retrieving inventory"""
    erp = ERPSystem()
    
    item = InventoryItem(
        id="i001",
        name="Test Item",
        category="test",
        quantity=20
    )
    
    erp.add_inventory_item(item)
    
    assert len(erp.get_all_inventory()) == 1
    assert erp.get_inventory_item("i001") is not None
    assert erp.get_inventory_item("i001").quantity == 20


def test_update_inventory_quantity():
    """Test updating inventory quantity through ERP system"""
    erp = ERPSystem()
    
    item = InventoryItem(
        id="i001",
        name="Test Item",
        category="test",
        quantity=20
    )
    
    erp.add_inventory_item(item)
    erp.update_inventory_quantity("i001", 10)
    
    assert erp.get_inventory_item("i001").quantity == 30


def test_add_transaction():
    """Test adding transactions"""
    erp = ERPSystem()
    
    transaction = Transaction(
        id="t001",
        type=TransactionType.PURCHASE,
        amount=1000.0,
        description="Test transaction"
    )
    
    erp.add_transaction(transaction)
    
    assert len(erp.get_transactions()) == 1
    assert len(erp.get_transactions("pending")) == 1


def test_complete_transaction():
    """Test completing transactions"""
    erp = ERPSystem()
    
    transaction = Transaction(
        id="t001",
        type=TransactionType.SALE,
        amount=500.0,
        description="Test"
    )
    
    erp.add_transaction(transaction)
    erp.complete_transaction("t001")
    
    assert len(erp.get_transactions("completed")) == 1


def test_get_system_status():
    """Test getting system status"""
    erp = ERPSystem(company_name="Test Corp")
    
    # Add some data
    resource = Resource(id="r001", name="Resource", type="test")
    item = InventoryItem(id="i001", name="Item", category="test", quantity=10)
    transaction = Transaction(id="t001", type=TransactionType.PURCHASE, amount=100.0, description="Test")
    
    erp.add_resource(resource)
    erp.add_inventory_item(item)
    erp.add_transaction(transaction)
    
    status = erp.get_system_status()
    
    assert status["company"] == "Test Corp"
    assert status["resources"]["total"] == 1
    assert status["inventory"]["total_items"] == 1
    assert status["transactions"]["total"] == 1


def test_get_recommendations():
    """Test getting recommendations from ERP system"""
    erp = ERPSystem()
    
    # Add resource with high utilization
    resource = Resource(
        id="r001",
        name="Overutilized Resource",
        type="test",
        utilization=85.0
    )
    erp.add_resource(resource)
    
    # Add inventory item that needs reorder
    item = InventoryItem(
        id="i001",
        name="Low Stock Item",
        category="test",
        quantity=5,
        reorder_point=10
    )
    erp.add_inventory_item(item)
    
    recommendations = erp.get_recommendations()
    
    assert "inventory" in recommendations
    assert "resources" in recommendations
    assert "costs" in recommendations
    assert "summary" in recommendations
    assert recommendations["summary"]["total_recommendations"] > 0


if __name__ == "__main__":
    test_erp_system_initialization()
    test_add_and_get_resource()
    test_add_and_get_inventory()
    test_update_inventory_quantity()
    test_add_transaction()
    test_complete_transaction()
    test_get_system_status()
    test_get_recommendations()
    print("All ERP system tests passed!")
