"""Main ERP system implementation"""

from typing import List, Dict, Any, Optional
from erpx.models.resource import Resource
from erpx.models.inventory import InventoryItem
from erpx.models.transaction import Transaction, TransactionType
from erpx.decision_engine.recommender import DecisionRecommender


class ERPSystem:
    """
    Main ERP system with integrated decision support
    A new way to manage enterprise resources with AI-powered recommendations
    """
    
    def __init__(self, company_name: str = "My Company"):
        self.company_name = company_name
        self.resources: Dict[str, Resource] = {}
        self.inventory: Dict[str, InventoryItem] = {}
        self.transactions: List[Transaction] = []
        self.recommender = DecisionRecommender()
    
    # Resource Management
    def add_resource(self, resource: Resource) -> None:
        """Add a resource to the system"""
        self.resources[resource.id] = resource
    
    def get_resource(self, resource_id: str) -> Optional[Resource]:
        """Get a resource by ID"""
        return self.resources.get(resource_id)
    
    def get_all_resources(self) -> List[Resource]:
        """Get all resources"""
        return list(self.resources.values())
    
    def update_resource_utilization(self, resource_id: str, utilization: float) -> None:
        """Update resource utilization"""
        if resource_id in self.resources:
            self.resources[resource_id].update_utilization(utilization)
    
    # Inventory Management
    def add_inventory_item(self, item: InventoryItem) -> None:
        """Add an inventory item to the system"""
        self.inventory[item.id] = item
    
    def get_inventory_item(self, item_id: str) -> Optional[InventoryItem]:
        """Get an inventory item by ID"""
        return self.inventory.get(item_id)
    
    def get_all_inventory(self) -> List[InventoryItem]:
        """Get all inventory items"""
        return list(self.inventory.values())
    
    def update_inventory_quantity(self, item_id: str, change: int) -> None:
        """Update inventory quantity"""
        if item_id in self.inventory:
            self.inventory[item_id].update_quantity(change)
    
    # Transaction Management
    def add_transaction(self, transaction: Transaction) -> None:
        """Add a transaction to the system"""
        self.transactions.append(transaction)
    
    def get_transactions(self, status: Optional[str] = None) -> List[Transaction]:
        """Get transactions, optionally filtered by status"""
        if status:
            return [t for t in self.transactions if t.status == status]
        return self.transactions
    
    def complete_transaction(self, transaction_id: str) -> bool:
        """Complete a transaction"""
        for transaction in self.transactions:
            if transaction.id == transaction_id:
                transaction.complete()
                return True
        return False
    
    # Decision Support & Recommendations
    def get_recommendations(self) -> Dict[str, Any]:
        """
        Get AI-powered recommendations for the entire system
        This is the key innovation - a recommendation decision system
        """
        all_recommendations = {
            "inventory": [],
            "resources": [],
            "costs": [],
            "summary": {}
        }
        
        # Analyze inventory
        inventory_recs = self.recommender.analyze_inventory(
            self.get_all_inventory()
        )
        all_recommendations["inventory"] = inventory_recs
        
        # Analyze resources
        resource_recs = self.recommender.analyze_resources(
            self.get_all_resources()
        )
        all_recommendations["resources"] = resource_recs
        
        # Analyze costs
        total_cost = sum(
            item.calculate_value() 
            for item in self.get_all_inventory()
        )
        budget = 100000.0  # Default budget
        cost_recs = self.recommender.analyze_costs(total_cost, budget)
        all_recommendations["costs"] = cost_recs
        
        # Generate summary
        all_recommendations["summary"] = {
            "total_recommendations": (
                len(inventory_recs) + 
                len(resource_recs) + 
                len(cost_recs)
            ),
            "critical_items": sum(
                1 for item in self.get_all_inventory() 
                if item.needs_reorder()
            ),
            "overutilized_resources": sum(
                1 for res in self.get_all_resources() 
                if res.utilization > 80
            ),
            "total_inventory_value": total_cost
        }
        
        return all_recommendations
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get overall system status"""
        return {
            "company": self.company_name,
            "resources": {
                "total": len(self.resources),
                "available": sum(
                    1 for r in self.resources.values() 
                    if r.is_available()
                )
            },
            "inventory": {
                "total_items": len(self.inventory),
                "items_needing_reorder": sum(
                    1 for i in self.inventory.values() 
                    if i.needs_reorder()
                ),
                "total_value": sum(
                    i.calculate_value() 
                    for i in self.inventory.values()
                )
            },
            "transactions": {
                "total": len(self.transactions),
                "pending": len(self.get_transactions("pending")),
                "completed": len(self.get_transactions("completed"))
            }
        }
