"""Inventory model for ERP system"""

from dataclasses import dataclass, field
from typing import Dict, Any
from datetime import datetime


@dataclass
class InventoryItem:
    """Represents an inventory item in the ERP system"""
    
    id: str
    name: str
    category: str
    quantity: int = 0
    reorder_point: int = 10
    unit_cost: float = 0.0
    supplier: str = ""
    location: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)
    last_updated: datetime = field(default_factory=datetime.now)
    
    def needs_reorder(self) -> bool:
        """Check if item needs to be reordered"""
        return self.quantity <= self.reorder_point
    
    def update_quantity(self, change: int) -> None:
        """Update inventory quantity"""
        new_quantity = self.quantity + change
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = new_quantity
        self.last_updated = datetime.now()
    
    def calculate_value(self) -> float:
        """Calculate total value of inventory item"""
        return self.quantity * self.unit_cost
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert inventory item to dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "quantity": self.quantity,
            "reorder_point": self.reorder_point,
            "unit_cost": self.unit_cost,
            "supplier": self.supplier,
            "location": self.location,
            "metadata": self.metadata,
            "needs_reorder": self.needs_reorder(),
            "total_value": self.calculate_value(),
            "last_updated": self.last_updated.isoformat()
        }
