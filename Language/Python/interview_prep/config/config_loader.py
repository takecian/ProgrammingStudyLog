"""
Configuration loader for the Python Interview Preparation System.

This module provides utilities to load and access configuration data
for patterns, difficulty levels, and other system settings.
"""

import json
import os
from typing import Dict, Any, List
from pathlib import Path


class ConfigLoader:
    """Loads and manages configuration data for the interview prep system."""
    
    def __init__(self):
        """Initialize the config loader with default paths."""
        self.config_dir = Path(__file__).parent
        self._patterns_config = None
        self._difficulty_config = None
    
    @property
    def patterns_config(self) -> Dict[str, Any]:
        """Load and cache patterns configuration."""
        if self._patterns_config is None:
            patterns_file = self.config_dir / "patterns.json"
            with open(patterns_file, 'r', encoding='utf-8') as f:
                self._patterns_config = json.load(f)
        return self._patterns_config
    
    @property
    def difficulty_config(self) -> Dict[str, Any]:
        """Load and cache difficulty levels configuration."""
        if self._difficulty_config is None:
            difficulty_file = self.config_dir / "difficulty_levels.json"
            with open(difficulty_file, 'r', encoding='utf-8') as f:
                self._difficulty_config = json.load(f)
        return self._difficulty_config
    
    def get_pattern_info(self, pattern_name: str) -> Dict[str, Any]:
        """Get information about a specific pattern."""
        patterns = self.patterns_config.get("patterns", {})
        return patterns.get(pattern_name, {})
    
    def get_difficulty_info(self, difficulty: str) -> Dict[str, Any]:
        """Get information about a specific difficulty level."""
        levels = self.difficulty_config.get("difficulty_levels", {})
        return levels.get(difficulty, {})
    
    def get_learning_order(self) -> List[str]:
        """Get the recommended learning order for patterns."""
        return self.patterns_config.get("learning_order", [])
    
    def get_progression_criteria(self, transition: str) -> Dict[str, Any]:
        """Get criteria for progressing between difficulty levels."""
        criteria = self.difficulty_config.get("progression_criteria", {})
        return criteria.get(transition, {})
    
    def get_practice_recommendations(self) -> Dict[str, int]:
        """Get daily/weekly practice recommendations."""
        return self.difficulty_config.get("practice_recommendations", {})
    
    def get_patterns_by_difficulty(self, difficulty: str) -> List[str]:
        """Get patterns recommended for a specific difficulty level."""
        difficulty_info = self.get_difficulty_info(difficulty)
        return difficulty_info.get("patterns", [])
    
    def get_time_limit(self, difficulty: str) -> int:
        """Get recommended time limit for a difficulty level."""
        difficulty_info = self.get_difficulty_info(difficulty)
        return difficulty_info.get("time_limit_minutes", 30)
    
    def get_expected_solve_rate(self, difficulty: str) -> int:
        """Get expected solve rate percentage for a difficulty level."""
        difficulty_info = self.get_difficulty_info(difficulty)
        return difficulty_info.get("expected_solve_rate", 50)


# Global config loader instance
config = ConfigLoader()