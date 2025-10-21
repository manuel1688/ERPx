"""
Advanced usage example of ERPx
Demonstrates custom rules and advanced decision support capabilities
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from erpx import ERPSystem
from erpx.models.resource import Resource
from erpx.models.inventory import InventoryItem
from erpx.decision_engine.rules import Rule, RuleType


def main():
    print("=" * 70)
    print("ERPx - Advanced Usage Example")
    print("Custom Business Rules and Decision Support")
    print("=" * 70)
    print()
    
    # Initialize ERP system
    erp = ERPSystem(company_name="Advanced Corp")
    
    # Add custom business rule
    print("1. Adding custom business rule...")
    
    def check_critical_inventory(context):
        """Check if inventory is critically low (below 30% of reorder point)"""
        item = context.get("inventory_item")
        if item:
            return item.quantity < (item.reorder_point * 0.3)
        return False
    
    def critical_inventory_action(context):
        """Action for critically low inventory"""
        item = context["inventory_item"]
        return {
            "recommendation": "CRITICAL: Immediate reorder required",
            "item": item.name,
            "current_quantity": item.quantity,
            "reorder_point": item.reorder_point,
            "urgency": "HIGH",
            "suggested_quantity": item.reorder_point * 3,
            "note": "Consider expedited shipping"
        }
    
    critical_rule = Rule(
        name="critical_inventory_alert",
        type=RuleType.INVENTORY_REORDER,
        condition=check_critical_inventory,
        action=critical_inventory_action,
        priority=10,  # Highest priority
        description="Alert for critically low inventory"
    )
    
    erp.recommender.add_custom_rule(critical_rule)
    print("   ✓ Added custom critical inventory rule")
    
    # Add another custom rule for resource efficiency
    print("2. Adding resource efficiency rule...")
    
    def check_underutilized_resources(context):
        """Check if resources are underutilized"""
        resource = context.get("resource")
        if resource:
            return resource.utilization < 30 and resource.status == "available"
        return False
    
    def underutilized_action(context):
        """Action for underutilized resources"""
        resource = context["resource"]
        return {
            "recommendation": "Resource underutilization detected",
            "resource": resource.name,
            "utilization": resource.utilization,
            "suggestion": "Consider reassigning or consolidating resources",
            "potential_savings": resource.cost_per_unit * (100 - resource.utilization)
        }
    
    efficiency_rule = Rule(
        name="resource_efficiency_alert",
        type=RuleType.RESOURCE_ALLOCATION,
        condition=check_underutilized_resources,
        action=underutilized_action,
        priority=6,
        description="Alert for underutilized resources"
    )
    
    erp.recommender.add_custom_rule(efficiency_rule)
    print("   ✓ Added custom resource efficiency rule")
    
    # Set up test scenario
    print("\n3. Creating test scenario...")
    
    # Add resources with varied utilization
    resources = [
        Resource(
            id="r001",
            name="Manufacturing Unit 1",
            type="manufacturing",
            utilization=95.0,
            cost_per_unit=100.0
        ),
        Resource(
            id="r002",
            name="Manufacturing Unit 2",
            type="manufacturing",
            utilization=25.0,  # Underutilized
            cost_per_unit=100.0
        ),
        Resource(
            id="r003",
            name="Warehouse A",
            type="storage",
            utilization=65.0,
            cost_per_unit=50.0
        )
    ]
    
    for resource in resources:
        erp.add_resource(resource)
    
    # Add inventory with critical and normal levels
    inventory_items = [
        InventoryItem(
            id="i001",
            name="Critical Component X",
            category="components",
            quantity=2,  # Critically low (< 30% of reorder point)
            reorder_point=20,
            unit_cost=500.0,
            supplier="Critical Supplies Inc"
        ),
        InventoryItem(
            id="i002",
            name="Standard Part Y",
            category="parts",
            quantity=15,  # Normal level
            reorder_point=10,
            unit_cost=100.0,
            supplier="Parts Warehouse"
        ),
        InventoryItem(
            id="i003",
            name="Raw Material Z",
            category="raw_materials",
            quantity=1,  # Critically low
            reorder_point=15,
            unit_cost=200.0,
            supplier="Materials Direct"
        )
    ]
    
    for item in inventory_items:
        erp.add_inventory_item(item)
    
    print(f"   ✓ Added {len(resources)} resources")
    print(f"   ✓ Added {len(inventory_items)} inventory items")
    
    # Get comprehensive recommendations
    print("\n" + "=" * 70)
    print("COMPREHENSIVE ANALYSIS & RECOMMENDATIONS")
    print("=" * 70)
    
    recommendations = erp.get_recommendations()
    
    # Display summary
    print(f"\n📊 Summary:")
    print(f"   - Total recommendations: {recommendations['summary']['total_recommendations']}")
    print(f"   - Critical items: {recommendations['summary']['critical_items']}")
    print(f"   - Overutilized resources: {recommendations['summary']['overutilized_resources']}")
    print(f"   - Total inventory value: ${recommendations['summary']['total_inventory_value']:,.2f}")
    
    # Display recommendations by priority
    all_recs = (
        recommendations['inventory'] +
        recommendations['resources'] +
        recommendations['costs']
    )
    
    if all_recs:
        print("\n" + "=" * 70)
        print("PRIORITIZED RECOMMENDATIONS")
        print("=" * 70)
        
        for i, rec in enumerate(all_recs, 1):
            if 'result' in rec:
                result = rec['result']
                print(f"\n[{i}] {rec['rule']} ({rec['type']})")
                print(f"    Recommendation: {result.get('recommendation', 'N/A')}")
                
                if 'urgency' in result:
                    print(f"    ⚠️  Urgency: {result['urgency']}")
                
                if 'item' in result:
                    print(f"    Item: {result['item']}")
                    print(f"    Current: {result.get('current_quantity', 'N/A')} | "
                          f"Reorder at: {result.get('reorder_point', 'N/A')}")
                    if 'suggested_quantity' in result:
                        print(f"    Suggested order: {result['suggested_quantity']} units")
                    if 'note' in result:
                        print(f"    📝 Note: {result['note']}")
                
                if 'resource' in result:
                    print(f"    Resource: {result['resource']}")
                    if 'utilization' in result:
                        print(f"    Utilization: {result['utilization']:.1f}%")
                    if 'potential_savings' in result:
                        print(f"    💰 Potential savings: ${result['potential_savings']:.2f}")
                
                if 'suggestion' in result:
                    print(f"    💡 Suggestion: {result['suggestion']}")
    
    # Demonstrate system status
    print("\n" + "=" * 70)
    print("SYSTEM STATUS")
    print("=" * 70)
    
    status = erp.get_system_status()
    
    print(f"\nCompany: {status['company']}")
    print(f"\nResources:")
    print(f"  Total: {status['resources']['total']}")
    print(f"  Available: {status['resources']['available']}")
    print(f"\nInventory:")
    print(f"  Total items: {status['inventory']['total_items']}")
    print(f"  Items needing reorder: {status['inventory']['items_needing_reorder']}")
    print(f"  Total value: ${status['inventory']['total_value']:,.2f}")
    
    print("\n" + "=" * 70)
    print("This advanced example demonstrates:")
    print("  ✓ Custom business rules")
    print("  ✓ Priority-based recommendations")
    print("  ✓ Complex decision scenarios")
    print("  ✓ Comprehensive system analysis")
    print("=" * 70)


if __name__ == "__main__":
    main()
