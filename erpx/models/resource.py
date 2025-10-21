"""Resource model for ERP system"""

from dataclasses import dataclass, field
from typing import Dict, Any
from datetime import datetime


@dataclass
class Resource:
    """Represents a resource in the ERP system"""
    
    id: str
    name: str
    type: str
    status: str = "available"
    capacity: float = 100.0
    utilization: float = 0.0
    cost_per_unit: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)
    
    def update_utilization(self, new_utilization: float) -> None:
        """Update resource utilization"""
        if 0 <= new_utilization <= 100:
            self.utilization = new_utilization
        else:
            raise ValueError("Utilization must be between 0 and 100")
    
    def is_available(self) -> bool:
        """Check if resource is available"""
        return self.status == "available" and self.utilization < self.capacity
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert resource to dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "status": self.status,
            "capacity": self.capacity,
            "utilization": self.utilization,
            "cost_per_unit": self.cost_per_unit,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat()
        }
