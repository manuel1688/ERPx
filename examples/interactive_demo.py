#!/usr/bin/env python3
"""
Interactive demo of ERPx
Showcases the recommendation system in an easy-to-understand format
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from erpx import ERPSystem
from erpx.models.resource import Resource
from erpx.models.inventory import InventoryItem
from erpx.models.transaction import Transaction, TransactionType


def print_separator(char="=", length=70):
    """Print a separator line"""
    print(char * length)


def print_section(title):
    """Print a section header"""
    print_separator()
    print(title)
    print_separator()


def display_recommendations(recs, category_name):
    """Display recommendations in a user-friendly format"""
    if not recs:
        print(f"  ✓ No {category_name} issues detected")
        return
    
    print(f"\n  ⚠️  {len(recs)} {category_name} recommendation(s):\n")
    for rec in recs:
        if 'result' in rec:
            result = rec['result']
            print(f"    → {result.get('recommendation', 'N/A')}")
            if 'suggestion' in result:
                print(f"      Action: {result['suggestion']}")
            print()


def main():
    print_section("ERPx - Interactive Demonstration")
    print("\nThis demo shows how ERPx helps you make better decisions\n")
    
    input("Press Enter to start the demo...")
    
    # Step 1: Initialize
    print("\n")
    print_section("STEP 1: Initialize the ERP System")
    print("\nCreating a new ERP system for 'Demo Manufacturing Co.'...")
    erp = ERPSystem(company_name="Demo Manufacturing Co.")
    print("✓ System initialized")
    
    input("\nPress Enter to add resources...")
    
    # Step 2: Add resources
    print("\n")
    print_section("STEP 2: Add Production Resources")
    print("\nAdding 3 production resources with different utilization levels...\n")
    
    resources = [
        ("Production Line A", 95, "⚠️  Almost at max capacity"),
        ("Production Line B", 65, "✓ Normal utilization"),
        ("Production Line C", 30, "💡 Underutilized")
    ]
    
    for name, utilization, status in resources:
        resource = Resource(
            id=f"r{name[-1].lower()}",
            name=name,
            type="manufacturing",
            utilization=utilization,
            cost_per_unit=100.0
        )
        erp.add_resource(resource)
        print(f"  {status} {name}: {utilization}% utilized")
    
    input("\nPress Enter to add inventory...")
    
    # Step 3: Add inventory
    print("\n")
    print_section("STEP 3: Add Inventory Items")
    print("\nAdding inventory with different stock levels...\n")
    
    items = [
        ("Raw Material X", 5, 20, "⚠️  Below reorder point"),
        ("Component Y", 30, 15, "✓ Adequate stock"),
        ("Part Z", 2, 15, "🚨 Critically low")
    ]
    
    for name, qty, reorder, status in items:
        item = InventoryItem(
            id=f"i{name.split()[0][:3].lower()}",
            name=name,
            category="materials",
            quantity=qty,
            reorder_point=reorder,
            unit_cost=100.0
        )
        erp.add_inventory_item(item)
        print(f"  {status} {name}: {qty} units (reorder at {reorder})")
    
    input("\nPress Enter to see system status...")
    
    # Step 4: System status
    print("\n")
    print_section("STEP 4: Current System Status")
    status = erp.get_system_status()
    
    print(f"""
Company: {status['company']}

Resources:
  • Total: {status['resources']['total']}
  • Available: {status['resources']['available']}

Inventory:
  • Total items: {status['inventory']['total_items']}
  • Items needing reorder: {status['inventory']['items_needing_reorder']}
  • Total value: ${status['inventory']['total_value']:,.2f}

Transactions:
  • Total: {status['transactions']['total']}
  • Pending: {status['transactions']['pending']}
""")
    
    input("Press Enter to get AI recommendations...")
    
    # Step 5: Get recommendations
    print("\n")
    print_section("STEP 5: AI-Powered Recommendations")
    print("\nAnalyzing your data and generating recommendations...\n")
    
    recommendations = erp.get_recommendations()
    
    print(f"📊 Analysis Summary:")
    print(f"  • Total recommendations: {recommendations['summary']['total_recommendations']}")
    print(f"  • Critical items: {recommendations['summary']['critical_items']}")
    print(f"  • Overutilized resources: {recommendations['summary']['overutilized_resources']}")
    
    input("\nPress Enter to see inventory recommendations...")
    print("\n📦 Inventory Recommendations:")
    display_recommendations(recommendations['inventory'], "inventory")
    
    input("Press Enter to see resource recommendations...")
    print("\n🔧 Resource Recommendations:")
    display_recommendations(recommendations['resources'], "resource")
    
    input("Press Enter to see cost recommendations...")
    print("\n💰 Cost Recommendations:")
    display_recommendations(recommendations['costs'], "cost")
    
    # Finale
    print("\n")
    print_section("Demo Complete!")
    print("""
Key Takeaways:

1. ERPx automatically monitors your operations
2. It detects issues before they become problems
3. It provides specific, actionable recommendations
4. You can focus on decisions, not data analysis

This is the NEW way to manage enterprise resources!

Try the other examples:
  • python examples/basic_usage.py
  • python examples/advanced_usage.py
""")
    print_separator()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nDemo interrupted. Thanks for trying ERPx!")
    except Exception as e:
        print(f"\n\nError: {e}")
        print("Please ensure you're running from the ERPx root directory")
