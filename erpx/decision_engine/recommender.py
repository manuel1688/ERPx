"""Decision recommender for ERP system"""

from typing import List, Dict, Any
from erpx.decision_engine.rules import RuleEngine, Rule, RuleType


class DecisionRecommender:
    """
    AI-powered decision recommendation engine for ERP
    Analyzes data and provides actionable recommendations
    """
    
    def __init__(self):
        self.rule_engine = RuleEngine()
        self._initialize_default_rules()
    
    def _initialize_default_rules(self) -> None:
        """Initialize default recommendation rules"""
        
        # Inventory reorder rule
        reorder_rule = Rule(
            name="inventory_reorder_alert",
            type=RuleType.INVENTORY_REORDER,
            condition=lambda ctx: (
                ctx.get("inventory_item") and 
                ctx["inventory_item"].needs_reorder()
            ),
            action=lambda ctx: {
                "recommendation": "Reorder inventory",
                "item": ctx["inventory_item"].name,
                "current_quantity": ctx["inventory_item"].quantity,
                "reorder_point": ctx["inventory_item"].reorder_point,
                "suggested_quantity": ctx["inventory_item"].reorder_point * 2
            },
            priority=8,
            description="Alert when inventory needs reordering"
        )
        
        # Resource utilization rule
        utilization_rule = Rule(
            name="resource_utilization_alert",
            type=RuleType.RESOURCE_ALLOCATION,
            condition=lambda ctx: (
                ctx.get("resource") and 
                ctx["resource"].utilization > 80
            ),
            action=lambda ctx: {
                "recommendation": "High resource utilization",
                "resource": ctx["resource"].name,
                "current_utilization": ctx["resource"].utilization,
                "suggestion": "Consider allocating additional resources"
            },
            priority=7,
            description="Alert when resource utilization is high"
        )
        
        # Cost optimization rule
        cost_rule = Rule(
            name="cost_optimization",
            type=RuleType.COST_OPTIMIZATION,
            condition=lambda ctx: (
                ctx.get("total_cost") and 
                ctx.get("budget") and
                ctx["total_cost"] > ctx["budget"] * 0.8
            ),
            action=lambda ctx: {
                "recommendation": "Cost threshold approaching",
                "current_cost": ctx["total_cost"],
                "budget": ctx["budget"],
                "utilization_percentage": (ctx["total_cost"] / ctx["budget"]) * 100,
                "suggestion": "Review spending and consider cost-saving measures"
            },
            priority=9,
            description="Alert when costs approach budget limit"
        )
        
        # Capacity planning rule
        capacity_rule = Rule(
            name="capacity_planning",
            type=RuleType.CAPACITY_PLANNING,
            condition=lambda ctx: (
                ctx.get("resources") and
                len([r for r in ctx["resources"] if r.utilization > 90]) > 0
            ),
            action=lambda ctx: {
                "recommendation": "Capacity expansion needed",
                "overutilized_resources": [
                    {"name": r.name, "utilization": r.utilization}
                    for r in ctx["resources"] if r.utilization > 90
                ],
                "suggestion": "Plan for capacity expansion or load balancing"
            },
            priority=8,
            description="Alert when capacity planning is needed"
        )
        
        self.rule_engine.add_rule(reorder_rule)
        self.rule_engine.add_rule(utilization_rule)
        self.rule_engine.add_rule(cost_rule)
        self.rule_engine.add_rule(capacity_rule)
    
    def add_custom_rule(self, rule: Rule) -> None:
        """Add a custom recommendation rule"""
        self.rule_engine.add_rule(rule)
    
    def get_recommendations(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Get recommendations based on current context
        
        Args:
            context: Dictionary containing ERP data (resources, inventory, etc.)
        
        Returns:
            List of recommendations with actions to take
        """
        return self.rule_engine.execute_rules(context)
    
    def analyze_inventory(self, inventory_items: List[Any]) -> List[Dict[str, Any]]:
        """Analyze inventory and provide recommendations"""
        recommendations = []
        for item in inventory_items:
            context = {"inventory_item": item}
            recs = self.get_recommendations(context)
            recommendations.extend(recs)
        return recommendations
    
    def analyze_resources(self, resources: List[Any]) -> List[Dict[str, Any]]:
        """Analyze resources and provide recommendations"""
        recommendations = []
        
        # Individual resource analysis
        for resource in resources:
            context = {"resource": resource}
            recs = self.get_recommendations(context)
            recommendations.extend(recs)
        
        # Overall capacity analysis
        context = {"resources": resources}
        recs = self.get_recommendations(context)
        recommendations.extend(recs)
        
        return recommendations
    
    def analyze_costs(self, total_cost: float, budget: float) -> List[Dict[str, Any]]:
        """Analyze costs and provide recommendations"""
        context = {
            "total_cost": total_cost,
            "budget": budget
        }
        return self.get_recommendations(context)
