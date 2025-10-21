"""
Basic usage example of ERPx - Experimental ERP with Decision Support
Demonstrates the recommendation decision system capabilities
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from erpx import ERPSystem
from erpx.models.resource import Resource
from erpx.models.inventory import InventoryItem
from erpx.models.transaction import Transaction, TransactionType


def main():
    print("=" * 70)
    print("ERPx - Experimental Enterprise Resource Planning")
    print("with AI-Powered Recommendation Decision System")
    print("=" * 70)
    print()
    
    # Initialize ERP system
    erp = ERPSystem(company_name="Demo Corporation")
    
    print("1. Setting up resources...")
    # Add some resources
    resources = [
        Resource(
            id="r001",
            name="Production Line A",
            type="manufacturing",
            capacity=100.0,
            utilization=85.0,
            cost_per_unit=50.0
        ),
        Resource(
            id="r002",
            name="Warehouse Storage",
            type="storage",
            capacity=100.0,
            utilization=65.0,
            cost_per_unit=20.0
        ),
        Resource(
            id="r003",
            name="Delivery Fleet",
            type="logistics",
            capacity=100.0,
            utilization=95.0,
            cost_per_unit=75.0
        )
    ]
    
    for resource in resources:
        erp.add_resource(resource)
    print(f"   Added {len(resources)} resources")
    
    print("\n2. Setting up inventory...")
    # Add inventory items
    inventory_items = [
        InventoryItem(
            id="i001",
            name="Raw Material A",
            category="raw_materials",
            quantity=5,
            reorder_point=10,
            unit_cost=100.0,
            supplier="Supplier Co"
        ),
        InventoryItem(
            id="i002",
            name="Component B",
            category="components",
            quantity=25,
            reorder_point=15,
            unit_cost=50.0,
            supplier="Parts Inc"
        ),
        InventoryItem(
            id="i003",
            name="Finished Product C",
            category="finished_goods",
            quantity=8,
            reorder_point=20,
            unit_cost=200.0,
            supplier="Internal"
        )
    ]
    
    for item in inventory_items:
        erp.add_inventory_item(item)
    print(f"   Added {len(inventory_items)} inventory items")
    
    print("\n3. Creating transactions...")
    # Add some transactions
    transactions = [
        Transaction(
            id="t001",
            type=TransactionType.PURCHASE,
            amount=5000.0,
            description="Raw material purchase",
            related_inventory_id="i001"
        ),
        Transaction(
            id="t002",
            type=TransactionType.SALE,
            amount=8000.0,
            description="Product sale",
            related_inventory_id="i003"
        )
    ]
    
    for transaction in transactions:
        erp.add_transaction(transaction)
    print(f"   Added {len(transactions)} transactions")
    
    # Get system status
    print("\n" + "=" * 70)
    print("SYSTEM STATUS")
    print("=" * 70)
    status = erp.get_system_status()
    print(f"\nCompany: {status['company']}")
    print(f"\nResources:")
    print(f"  - Total: {status['resources']['total']}")
    print(f"  - Available: {status['resources']['available']}")
    print(f"\nInventory:")
    print(f"  - Total items: {status['inventory']['total_items']}")
    print(f"  - Items needing reorder: {status['inventory']['items_needing_reorder']}")
    print(f"  - Total value: ${status['inventory']['total_value']:,.2f}")
    print(f"\nTransactions:")
    print(f"  - Total: {status['transactions']['total']}")
    print(f"  - Pending: {status['transactions']['pending']}")
    print(f"  - Completed: {status['transactions']['completed']}")
    
    # Get AI-powered recommendations
    print("\n" + "=" * 70)
    print("AI-POWERED RECOMMENDATIONS (Decision Support System)")
    print("=" * 70)
    recommendations = erp.get_recommendations()
    
    print(f"\nSummary:")
    print(f"  - Total recommendations: {recommendations['summary']['total_recommendations']}")
    print(f"  - Critical items: {recommendations['summary']['critical_items']}")
    print(f"  - Overutilized resources: {recommendations['summary']['overutilized_resources']}")
    
    if recommendations['inventory']:
        print(f"\n📦 Inventory Recommendations ({len(recommendations['inventory'])}):")
        for rec in recommendations['inventory']:
            if 'result' in rec:
                result = rec['result']
                print(f"   • {result['recommendation']}")
                print(f"     Item: {result['item']}")
                print(f"     Current: {result['current_quantity']} | Reorder at: {result['reorder_point']}")
                print(f"     Suggested order: {result['suggested_quantity']} units")
    
    if recommendations['resources']:
        print(f"\n🔧 Resource Recommendations ({len(recommendations['resources'])}):")
        for rec in recommendations['resources']:
            if 'result' in rec:
                result = rec['result']
                print(f"   • {result['recommendation']}")
                if 'resource' in result:
                    print(f"     Resource: {result['resource']}")
                    print(f"     Utilization: {result['current_utilization']:.1f}%")
                    print(f"     → {result['suggestion']}")
                elif 'overutilized_resources' in result:
                    print(f"     → {result['suggestion']}")
                    for res in result['overutilized_resources']:
                        print(f"       - {res['name']}: {res['utilization']:.1f}%")
    
    if recommendations['costs']:
        print(f"\n💰 Cost Recommendations ({len(recommendations['costs'])}):")
        for rec in recommendations['costs']:
            if 'result' in rec:
                result = rec['result']
                print(f"   • {result['recommendation']}")
                print(f"     Current: ${result['current_cost']:,.2f} | Budget: ${result['budget']:,.2f}")
                print(f"     Utilization: {result['utilization_percentage']:.1f}%")
                print(f"     → {result['suggestion']}")
    
    print("\n" + "=" * 70)
    print("This demonstrates ERPx's innovative decision recommendation system")
    print("A new way to manage enterprise resources with AI-powered insights!")
    print("=" * 70)


if __name__ == "__main__":
    main()
