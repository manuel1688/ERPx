"""
ERPx - Experimental Enterprise Resource Planning with Decision Support
A new way to manage enterprise resources with AI-powered recommendations
"""

__version__ = "0.1.0"
__author__ = "Manuel"

from erpx.core.erp_system import ERPSystem
from erpx.decision_engine.recommender import DecisionRecommender

__all__ = ["ERPSystem", "DecisionRecommender"]
