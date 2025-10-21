"""Tests for decision engine"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from erpx.decision_engine.recommender import DecisionRecommender
from erpx.decision_engine.rules import Rule, RuleType, RuleEngine
from erpx.models.resource import Resource
from erpx.models.inventory import InventoryItem


def test_rule_creation():
    """Test rule creation"""
    rule = Rule(
        name="test_rule",
        type=RuleType.COST_OPTIMIZATION,
        condition=lambda ctx: ctx.get("value", 0) > 100,
        action=lambda ctx: {"result": "action taken"},
        priority=5
    )
    
    assert rule.name == "test_rule"
    assert rule.priority == 5


def test_rule_evaluation():
    """Test rule evaluation"""
    rule = Rule(
        name="test_rule",
        type=RuleType.COST_OPTIMIZATION,
        condition=lambda ctx: ctx.get("value", 0) > 100,
        action=lambda ctx: {"result": "success"}
    )
    
    assert rule.evaluate({"value": 150}) == True
    assert rule.evaluate({"value": 50}) == False


def test_rule_engine():
    """Test rule engine"""
    engine = RuleEngine()
    
    rule1 = Rule(
        name="rule1",
        type=RuleType.COST_OPTIMIZATION,
        condition=lambda ctx: ctx.get("cost", 0) > 1000,
        action=lambda ctx: {"recommendation": "reduce costs"},
        priority=8
    )
    
    rule2 = Rule(
        name="rule2",
        type=RuleType.RESOURCE_ALLOCATION,
        condition=lambda ctx: ctx.get("utilization", 0) > 80,
        action=lambda ctx: {"recommendation": "add resources"},
        priority=7
    )
    
    engine.add_rule(rule1)
    engine.add_rule(rule2)
    
    assert len(engine.rules) == 2
    assert engine.rules[0].priority == 8  # Higher priority first


def test_recommender_initialization():
    """Test decision recommender initialization"""
    recommender = DecisionRecommender()
    
    assert recommender.rule_engine is not None
    assert len(recommender.rule_engine.rules) > 0  # Should have default rules


def test_inventory_recommendations():
    """Test inventory recommendations"""
    recommender = DecisionRecommender()
    
    # Create item that needs reorder
    item = InventoryItem(
        id="i001",
        name="Test Item",
        category="test",
        quantity=5,
        reorder_point=10
    )
    
    recommendations = recommender.analyze_inventory([item])
    
    assert len(recommendations) > 0
    assert any("reorder" in str(rec).lower() for rec in recommendations)


def test_resource_recommendations():
    """Test resource recommendations"""
    recommender = DecisionRecommender()
    
    # Create high utilization resource
    resource = Resource(
        id="r001",
        name="Test Resource",
        type="test",
        utilization=85.0
    )
    
    recommendations = recommender.analyze_resources([resource])
    
    assert len(recommendations) > 0
    assert any("utilization" in str(rec).lower() for rec in recommendations)


def test_cost_recommendations():
    """Test cost recommendations"""
    recommender = DecisionRecommender()
    
    # Set up cost scenario near budget limit
    total_cost = 85000.0
    budget = 100000.0
    
    recommendations = recommender.analyze_costs(total_cost, budget)
    
    assert len(recommendations) > 0
    assert any("cost" in str(rec).lower() for rec in recommendations)


if __name__ == "__main__":
    test_rule_creation()
    test_rule_evaluation()
    test_rule_engine()
    test_recommender_initialization()
    test_inventory_recommendations()
    test_resource_recommendations()
    test_cost_recommendations()
    print("All decision engine tests passed!")
