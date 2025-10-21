# ERPx Quick Start Guide

Welcome to ERPx - a new way to manage enterprise resources with AI-powered recommendations!

## What is ERPx?

ERPx is not just another ERP system. It's an **intelligent decision support system** that:
- Tracks your resources, inventory, and transactions
- Analyzes your data continuously
- **Tells you what to do next** with actionable recommendations

## Installation

No external dependencies required! Just Python 3.8+

```bash
git clone https://github.com/manuel1688/ERPx.git
cd ERPx
```

## 5-Minute Tutorial

### Step 1: Import and Initialize

```python
from erpx import ERPSystem
from erpx.models.resource import Resource
from erpx.models.inventory import InventoryItem

# Create your ERP system
erp = ERPSystem(company_name="My Company")
```

### Step 2: Add Your Resources

Resources are anything you use to run your business: machines, people, space, etc.

```python
# Add a manufacturing resource
factory_line = Resource(
    id="line1",
    name="Assembly Line 1",
    type="manufacturing",
    capacity=100.0,
    utilization=85.0,  # Currently at 85% capacity
    cost_per_unit=100.0
)
erp.add_resource(factory_line)
```

### Step 3: Add Your Inventory

Track what you have in stock.

```python
# Add an inventory item
raw_material = InventoryItem(
    id="rm001",
    name="Steel Sheets",
    category="raw_materials",
    quantity=15,
    reorder_point=20,  # Reorder when below 20 units
    unit_cost=50.0,
    supplier="Steel Co"
)
erp.add_inventory_item(raw_material)
```

### Step 4: Get AI Recommendations

This is where the magic happens!

```python
# Get intelligent recommendations
recommendations = erp.get_recommendations()

# See what the system recommends
for rec in recommendations['inventory']:
    print(rec)

for rec in recommendations['resources']:
    print(rec)
```

### Step 5: Check System Status

```python
status = erp.get_system_status()
print(f"Total inventory value: ${status['inventory']['total_value']}")
print(f"Items needing reorder: {status['inventory']['items_needing_reorder']}")
```

## What You Get

### Automatic Alerts

- **Inventory Reorder**: "Your Steel Sheets are running low (15 units). Reorder 40 units."
- **Resource Utilization**: "Assembly Line 1 is at 85% capacity. Consider adding resources."
- **Cost Warnings**: "You've used 80% of your budget. Review spending."
- **Capacity Planning**: "3 resources are over 90% utilized. Plan for expansion."

### Smart Recommendations

Every recommendation includes:
- **What's wrong**: Clear description of the issue
- **Current state**: Actual numbers (quantity, utilization, cost)
- **Suggested action**: Specific steps to take
- **Priority**: How urgent is it

## Advanced: Custom Rules

Want to add your own business logic?

```python
from erpx.decision_engine.rules import Rule, RuleType

# Create a custom rule
my_rule = Rule(
    name="weekend_alert",
    type=RuleType.RESOURCE_ALLOCATION,
    condition=lambda ctx: ctx.get("day") == "Sunday",
    action=lambda ctx: {
        "recommendation": "Weekend operations detected",
        "suggestion": "Consider overtime policies"
    },
    priority=5
)

# Add it to your system
erp.recommender.add_custom_rule(my_rule)
```

## Real-World Example

```python
from erpx import ERPSystem
from erpx.models.inventory import InventoryItem

# Initialize
erp = ERPSystem(company_name="TechParts Inc")

# Add inventory
parts = [
    InventoryItem("p1", "CPU", "electronics", quantity=5, reorder_point=10, unit_cost=200),
    InventoryItem("p2", "RAM", "electronics", quantity=25, reorder_point=15, unit_cost=100),
    InventoryItem("p3", "SSD", "electronics", quantity=3, reorder_point=20, unit_cost=150)
]

for part in parts:
    erp.add_inventory_item(part)

# Get recommendations
recs = erp.get_recommendations()

# System will alert you:
# - CPU needs reorder (5 < 10)
# - SSD needs reorder (3 < 20)
# - RAM is OK (25 > 15)
```

## Run the Examples

See it in action:

```bash
# Basic example
python examples/basic_usage.py

# Advanced example with custom rules
python examples/advanced_usage.py
```

## Run the Tests

```bash
python tests/test_models.py
python tests/test_decision_engine.py
python tests/test_erp_system.py
```

## Key Concepts

### Resources
Physical or virtual assets used in operations (machines, people, space, vehicles, etc.)

### Inventory
Items you buy, make, or sell (raw materials, components, finished products)

### Transactions
Financial or operational events (purchases, sales, transfers, adjustments)

### Recommendations
AI-generated insights telling you what action to take

### Rules
Business logic that triggers recommendations based on conditions

## Philosophy

**Traditional ERP**: "Here's your data"  
**ERPx**: "Here's your data AND here's what to do about it"

## Next Steps

1. Try the examples
2. Add your own data
3. Create custom rules for your business
4. Let ERPx help you make better decisions!

## Need Help?

- Read the full README.md
- Check the examples/ directory
- Look at the tests/ for code examples
- Explore the erpx/ source code

## License

MIT License - Free to use and modify!
