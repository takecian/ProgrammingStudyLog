"""
Python techniques library for coding interviews.

This package provides essential Python techniques, data structures, algorithms,
and utilities commonly needed in coding interviews.
"""

from .built_ins import BuiltInTechniques
from .data_structures import CollectionsTechniques, DataStructureUtils
from .algorithms import (
    SearchAlgorithms, 
    SortingAlgorithms, 
    GraphAlgorithms, 
    DynamicProgramming,
    StringAlgorithms
)
from .interview_utils import (
    InputParser,
    OutputFormatter, 
    TestingUtils,
    DataStructureHelpers,
    StringHelpers,
    MathHelpers
)

__all__ = [
    'BuiltInTechniques',
    'CollectionsTechniques',
    'DataStructureUtils',
    'SearchAlgorithms',
    'SortingAlgorithms', 
    'GraphAlgorithms',
    'DynamicProgramming',
    'StringAlgorithms',
    'InputParser',
    'OutputFormatter',
    'TestingUtils',
    'DataStructureHelpers',
    'StringHelpers',
    'MathHelpers'
]

__version__ = '1.0.0'
__author__ = 'Interview Prep System'
__description__ = 'Python techniques and utilities for coding interviews'