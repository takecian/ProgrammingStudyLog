"""
Core data models for the Python Interview Preparation System.

This module defines the fundamental data structures used throughout
the interview preparation system, including problems, solutions,
and user progress tracking.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from datetime import datetime
from enum import Enum


class Difficulty(Enum):
    """Problem difficulty levels."""
    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"


class PatternType(Enum):
    """Problem-solving pattern categories."""
    TWO_POINTERS = "Two Pointers"
    SLIDING_WINDOW = "Sliding Window"
    FAST_SLOW_POINTERS = "Fast & Slow Pointers"
    MERGE_INTERVALS = "Merge Intervals"
    CYCLIC_SORT = "Cyclic Sort"
    IN_PLACE_REVERSAL = "In-place Reversal of LinkedList"
    TREE_BFS = "Tree Breadth First Search"
    TREE_DFS = "Tree Depth First Search"
    TWO_HEAPS = "Two Heaps"
    SUBSETS = "Subsets"
    MODIFIED_BINARY_SEARCH = "Modified Binary Search"
    BITWISE_XOR = "Bitwise XOR"
    TOP_K_ELEMENTS = "Top 'K' Elements"
    K_WAY_MERGE = "K-way merge"
    DYNAMIC_PROGRAMMING = "Dynamic Programming"
    TOPOLOGICAL_SORT = "Topological Sort"
    GRAPH_TRAVERSAL = "Graph Traversal"
    SYSTEM_DESIGN = "System Design"


@dataclass
class Example:
    """Test case example for a problem."""
    input_data: str
    expected_output: str
    explanation: Optional[str] = None


@dataclass
class Solution:
    """A solution approach for a coding problem."""
    approach_name: str  # "Brute Force", "Optimized", "Python Idioms"
    code: str
    time_complexity: str
    space_complexity: str
    explanation: str
    key_insights: List[str] = field(default_factory=list)
    python_features: List[str] = field(default_factory=list)  # Built-ins, libraries used
    
    def __post_init__(self):
        """Validate solution data after initialization."""
        if not self.approach_name.strip():
            raise ValueError("Solution must have an approach name")
        if not self.code.strip():
            raise ValueError("Solution must have code")


@dataclass
class Problem:
    """A coding interview problem with multiple solutions and metadata."""
    id: str
    title: str
    difficulty: Difficulty
    pattern: PatternType
    description: str
    examples: List[Example] = field(default_factory=list)
    constraints: List[str] = field(default_factory=list)
    hints: List[str] = field(default_factory=list)
    solutions: List[Solution] = field(default_factory=list)
    related_problems: List[str] = field(default_factory=list)
    python_techniques: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        """Validate problem data after initialization."""
        if not self.id.strip():
            raise ValueError("Problem must have an ID")
        if not self.title.strip():
            raise ValueError("Problem must have a title")
        if not self.description.strip():
            raise ValueError("Problem must have a description")
    
    def add_solution(self, solution: Solution) -> None:
        """Add a solution to this problem."""
        self.solutions.append(solution)
    
    def get_solution_by_approach(self, approach_name: str) -> Optional[Solution]:
        """Get a solution by its approach name."""
        for solution in self.solutions:
            if solution.approach_name == approach_name:
                return solution
        return None
    
    def get_optimal_solution(self) -> Optional[Solution]:
        """Get the most optimal solution (usually the last one added)."""
        return self.solutions[-1] if self.solutions else None


@dataclass
class PracticeSessionResult:
    """Result of a single practice session."""
    problem_id: str
    start_time: datetime
    end_time: Optional[datetime] = None
    solved: bool = False
    hints_used: int = 0
    attempts: int = 0
    solution_approach: Optional[str] = None
    time_taken_seconds: Optional[int] = None
    
    @property
    def duration_seconds(self) -> Optional[int]:
        """Calculate session duration in seconds."""
        if self.end_time and self.start_time:
            return int((self.end_time - self.start_time).total_seconds())
        return None


@dataclass
class UserProgress:
    """User's learning progress and performance metrics."""
    user_id: str
    completed_patterns: Dict[str, int] = field(default_factory=dict)  # pattern -> problems solved
    practice_sessions: List[PracticeSessionResult] = field(default_factory=list)
    weak_areas: List[str] = field(default_factory=list)
    strengths: List[str] = field(default_factory=list)
    total_problems_solved: int = 0
    total_practice_time_seconds: int = 0
    created_at: datetime = field(default_factory=datetime.now)
    last_updated: datetime = field(default_factory=datetime.now)
    
    def add_practice_session(self, session: PracticeSessionResult) -> None:
        """Add a practice session result."""
        self.practice_sessions.append(session)
        if session.solved:
            self.total_problems_solved += 1
        if session.duration_seconds:
            self.total_practice_time_seconds += session.duration_seconds
        self.last_updated = datetime.now()
    
    @property
    def average_solve_time_seconds(self) -> float:
        """Calculate average time to solve problems."""
        solved_sessions = [s for s in self.practice_sessions if s.solved and s.duration_seconds]
        if not solved_sessions:
            return 0.0
        return sum(s.duration_seconds for s in solved_sessions) / len(solved_sessions)
    
    @property
    def success_rate(self) -> float:
        """Calculate success rate as percentage."""
        if not self.practice_sessions:
            return 0.0
        solved_count = sum(1 for s in self.practice_sessions if s.solved)
        return (solved_count / len(self.practice_sessions)) * 100
    
    def get_pattern_progress(self, pattern: PatternType) -> int:
        """Get number of problems solved for a specific pattern."""
        return self.completed_patterns.get(pattern.value, 0)
    
    def update_pattern_progress(self, pattern: PatternType, problems_solved: int) -> None:
        """Update progress for a specific pattern."""
        self.completed_patterns[pattern.value] = problems_solved
        self.last_updated = datetime.now()


@dataclass
class LearningPath:
    """A structured learning path with ordered topics."""
    name: str
    description: str
    difficulty_level: Difficulty
    patterns: List[PatternType] = field(default_factory=list)
    estimated_hours: int = 0
    prerequisites: List[str] = field(default_factory=list)
    
    def add_pattern(self, pattern: PatternType) -> None:
        """Add a pattern to this learning path."""
        if pattern not in self.patterns:
            self.patterns.append(pattern)


@dataclass
class StudySession:
    """A focused study session on a specific topic."""
    topic: str
    pattern: PatternType
    problems: List[str] = field(default_factory=list)  # Problem IDs
    time_limit_minutes: int = 45
    created_at: datetime = field(default_factory=datetime.now)
    completed: bool = False
    
    def add_problem(self, problem_id: str) -> None:
        """Add a problem to this study session."""
        if problem_id not in self.problems:
            self.problems.append(problem_id)