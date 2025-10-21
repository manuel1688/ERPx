# ERPx - Experimental Enterprise Resource Planning

**A new way to manage enterprise resources with AI-powered recommendation decision system**

ERPx is an innovative approach to Enterprise Resource Planning that integrates intelligent decision support directly into resource management. Instead of just tracking resources, inventory, and transactions, ERPx actively analyzes your business data and provides actionable recommendations to optimize operations.

## 🚀 Key Features

- **AI-Powered Decision Support**: Intelligent recommendation engine that analyzes your business data
- **Resource Management**: Track and optimize resource allocation and utilization
- **Inventory Control**: Smart inventory management with automatic reorder alerts
- **Transaction Tracking**: Complete transaction lifecycle management
- **Rule-Based Intelligence**: Customizable business rules for automated decision-making
- **Cost Optimization**: Budget monitoring and cost-saving recommendations
- **Capacity Planning**: Proactive alerts for capacity constraints

## 🎯 What Makes ERPx Different

Traditional ERP systems are passive - they store and display data. ERPx is **active** - it thinks about your data and tells you what to do next. The integrated recommendation engine continuously monitors your operations and provides:

- **Inventory Reorder Alerts**: Automatically detects when stock is low
- **Resource Utilization Warnings**: Identifies overutilized resources before they become bottlenecks
- **Cost Management Insights**: Alerts when spending approaches budget limits
- **Capacity Planning Recommendations**: Predicts when you'll need to expand capacity

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/manuel1688/ERPx.git
cd ERPx

# No external dependencies required!
# The system uses only Python standard library
```

## 🏃 Quick Start

```python
from erpx import ERPSystem
from erpx.models.resource import Resource
from erpx.models.inventory import InventoryItem

# Initialize the ERP system
erp = ERPSystem(company_name="My Company")

# Add a resource
resource = Resource(
    id="r001",
    name="Production Line A",
    type="manufacturing",
    utilization=85.0
)
erp.add_resource(resource)

# Add inventory
item = InventoryItem(
    id="i001",
    name="Raw Material",
    category="raw_materials",
    quantity=5,
    reorder_point=10,
    unit_cost=100.0
)
erp.add_inventory_item(item)

# Get AI-powered recommendations
recommendations = erp.get_recommendations()
print(recommendations)
```

## 📚 Examples

Run the included example to see ERPx in action:

```bash
python examples/basic_usage.py
```

This will demonstrate:
- Setting up resources, inventory, and transactions
- Getting system status
- Receiving AI-powered recommendations
- Understanding the decision support system

## 🏗️ Architecture

```
erpx/
├── core/              # Main ERP system
├── models/            # Data models (Resource, Inventory, Transaction)
├── decision_engine/   # AI recommendation system
│   ├── recommender.py # Main recommendation engine
│   └── rules.py       # Rule engine for business logic
└── utils/             # Utility functions
```

## 🧠 Decision Engine

The heart of ERPx is its decision engine, which uses a rule-based system to analyze your business data:

1. **Rules Evaluation**: Continuously evaluates business rules against current data
2. **Pattern Recognition**: Identifies patterns that require attention
3. **Recommendation Generation**: Creates actionable recommendations with specific suggestions
4. **Priority Management**: Orders recommendations by importance

### Built-in Rules

- **Inventory Reorder Alert**: Triggers when inventory falls below reorder point
- **Resource Utilization Alert**: Warns when resources exceed 80% utilization
- **Cost Optimization**: Alerts when costs approach 80% of budget
- **Capacity Planning**: Identifies when capacity expansion is needed

### Custom Rules

You can add your own business rules:

```python
from erpx.decision_engine.rules import Rule, RuleType

custom_rule = Rule(
    name="my_custom_rule",
    type=RuleType.COST_OPTIMIZATION,
    condition=lambda ctx: ctx.get("value") > 1000,
    action=lambda ctx: {"recommendation": "Take action", "value": ctx["value"]},
    priority=7,
    description="My custom business rule"
)

erp.recommender.add_custom_rule(custom_rule)
```

## 📊 Use Cases

- **Manufacturing**: Optimize production line utilization and material inventory
- **Retail**: Manage stock levels and predict reorder needs
- **Logistics**: Balance fleet capacity and delivery schedules
- **Services**: Optimize resource allocation and capacity planning
- **Any Business**: Get intelligent insights from your operational data

## 🔧 Development

```bash
# Install development dependencies
pip install -r requirements.txt

# Run tests (if available)
pytest tests/

# The system is designed to be extended:
# - Add new data models in erpx/models/
# - Create custom rules in erpx/decision_engine/
# - Extend the ERP system in erpx/core/
```

## 🤝 Contributing

Contributions are welcome! This is an experimental project exploring new approaches to ERP systems.

## 📄 License

MIT License - see LICENSE file for details

## 🎓 Philosophy

ERPx represents a new paradigm in enterprise software:
- **From Passive to Active**: Systems should recommend, not just record
- **From Historical to Predictive**: Look forward, not just backward
- **From Complex to Simple**: Powerful doesn't mean complicated
- **From Reactive to Proactive**: Prevent problems before they occur

Traditional ERP = "Here's what happened"  
**ERPx** = "Here's what to do next"
