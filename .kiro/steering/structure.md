# Project Structure

## Root Level Organization

```
├── AtCoder/           # AtCoder contest solutions
├── LeetCode/          # LeetCode problem solutions  
├── Codeforces/        # Codeforces contest solutions
├── GoogleCodeJam/     # Google Code Jam solutions
├── GoogleKickStart/   # Google Kick Start solutions
├── Libs/              # Reusable algorithm implementations
├── Practice/          # Practice implementations
├── 30daysOS/          # OS development project
├── Language/          # Language-specific examples
├── SystemDesignPractice/ # System design study materials
├── kaggle/            # Kaggle competition work
├── hackerrank/        # HackerRank solutions
├── algoexpert/        # AlgoExpert problem solutions
├── paiza/             # Paiza contest solutions
├── private/           # Private study materials
└── others/            # Miscellaneous projects
```

## Contest Platform Structure

### AtCoder (`AtCoder/`)
- `ABC/`: AtCoder Beginner Contest solutions (numbered directories)
- `ARC/`: AtCoder Regular Contest solutions
- `AGC/`: AtCoder Grand Contest solutions
- `Contests/`: Special contest solutions
- `ari_beginner/`: Problems from competitive programming textbook
- `seisen10/`: Selected 10 problems for practice
- `typical_dp/`: Dynamic programming focused problems

### LeetCode (`LeetCode/`)
- Organized by problem number ranges (0/, 100/, 200/, etc.)
- `mock_interview/`: Mock interview problems
- `top-interview-questions/`: Curated interview problems

## Algorithm Library (`Libs/`)

Core algorithm implementations for reuse:
- `dijkstra.py`: Shortest path algorithm
- `union_find.py`: Disjoint set data structure
- `segment_tree.py`: Range query data structure
- `eratosthenes.py`: Prime number generation
- `knapsack.py`: Dynamic programming solution
- `trie.py`: Prefix tree implementation
- `warshall_floyd.py`: All-pairs shortest path

## Utility Files

- `snippet_for_cp.py`: Competitive programming code snippets
- `snippet_for_leetcode.py`: LeetCode-specific utilities
- `README.md`: Main documentation with problem-solving patterns
- `ARCHITECTURE.md`: Software architecture patterns
- `SYSTEM_DESIGN.md`: System design study notes
- `BEHAVIOURAL.md`: Behavioral interview preparation

## Special Projects

### OS Development (`30daysOS/`)
- `day1/`, `day2/`, etc.: Progressive OS development
- `z_tools/`: Custom build tools and utilities
- Assembly and C source files for bootloader and kernel

### Language Examples (`Language/`)
- `Haskell/`: Functional programming examples
- `Objective-C/`: iOS development examples  
- `Rust/`: Systems programming examples

## File Naming Conventions

- Contest problems: Use platform-specific naming (e.g., `abc001_a.py`)
- Algorithm implementations: Descriptive names (e.g., `dijkstra.py`)
- Study materials: Uppercase markdown files (e.g., `SYSTEM_DESIGN.md`)
- Utility scripts: Lowercase with underscores (e.g., `snippet_for_cp.py`)

## Directory Guidelines

- Each contest platform has its own top-level directory
- Problem solutions are grouped by contest or problem set
- Reusable code goes in `Libs/` directory
- Documentation and study materials at root level
- Private or sensitive materials in `private/` directory