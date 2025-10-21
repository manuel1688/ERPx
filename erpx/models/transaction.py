"""Transaction model for ERP system"""

from dataclasses import dataclass, field
from typing import Dict, Any
from datetime import datetime
from enum import Enum


class TransactionType(Enum):
    """Types of transactions"""
    PURCHASE = "purchase"
    SALE = "sale"
    TRANSFER = "transfer"
    ADJUSTMENT = "adjustment"


@dataclass
class Transaction:
    """Represents a transaction in the ERP system"""
    
    id: str
    type: TransactionType
    amount: float
    description: str
    related_resource_id: str = ""
    related_inventory_id: str = ""
    status: str = "pending"
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)
    completed_at: datetime = None
    
    def complete(self) -> None:
        """Mark transaction as completed"""
        self.status = "completed"
        self.completed_at = datetime.now()
    
    def cancel(self) -> None:
        """Cancel transaction"""
        self.status = "cancelled"
        self.completed_at = datetime.now()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert transaction to dictionary"""
        return {
            "id": self.id,
            "type": self.type.value,
            "amount": self.amount,
            "description": self.description,
            "related_resource_id": self.related_resource_id,
            "related_inventory_id": self.related_inventory_id,
            "status": self.status,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
            "completed_at": self.completed_at.isoformat() if self.completed_at else None
        }
