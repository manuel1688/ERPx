"""Rule engine for decision making"""

from dataclasses import dataclass
from typing import Callable, List, Dict, Any
from enum import Enum


class RuleType(Enum):
    """Types of rules"""
    RESOURCE_ALLOCATION = "resource_allocation"
    INVENTORY_REORDER = "inventory_reorder"
    COST_OPTIMIZATION = "cost_optimization"
    CAPACITY_PLANNING = "capacity_planning"


@dataclass
class Rule:
    """Represents a business rule"""
    
    name: str
    type: RuleType
    condition: Callable[[Dict[str, Any]], bool]
    action: Callable[[Dict[str, Any]], Dict[str, Any]]
    priority: int = 5
    description: str = ""
    
    def evaluate(self, context: Dict[str, Any]) -> bool:
        """Evaluate if rule condition is met"""
        try:
            return self.condition(context)
        except Exception:
            return False
    
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute rule action"""
        return self.action(context)


class RuleEngine:
    """Engine for evaluating and executing rules"""
    
    def __init__(self):
        self.rules: List[Rule] = []
    
    def add_rule(self, rule: Rule) -> None:
        """Add a rule to the engine"""
        self.rules.append(rule)
        self.rules.sort(key=lambda r: r.priority, reverse=True)
    
    def remove_rule(self, rule_name: str) -> None:
        """Remove a rule from the engine"""
        self.rules = [r for r in self.rules if r.name != rule_name]
    
    def evaluate_rules(self, context: Dict[str, Any]) -> List[Rule]:
        """Evaluate all rules and return matching ones"""
        matching_rules = []
        for rule in self.rules:
            if rule.evaluate(context):
                matching_rules.append(rule)
        return matching_rules
    
    def execute_rules(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Execute all matching rules and return results"""
        matching_rules = self.evaluate_rules(context)
        results = []
        for rule in matching_rules:
            try:
                result = rule.execute(context)
                results.append({
                    "rule": rule.name,
                    "type": rule.type.value,
                    "result": result
                })
            except Exception as e:
                results.append({
                    "rule": rule.name,
                    "type": rule.type.value,
                    "error": str(e)
                })
        return results
