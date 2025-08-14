# Technology Stack

## Primary Languages

- **Python**: Main language for competitive programming solutions and algorithm implementations
  - Version: PyPy 3.6-7.2.0 (optimized for competitive programming performance)
  - Used for: AtCoder, LeetCode, Codeforces solutions, algorithm libraries
- **Swift/Objective-C**: iOS development knowledge and examples
- **C**: Low-level programming for OS development (30daysOS project)
- **Assembly**: NASM/NAS for bootloader and OS kernel development
- **Haskell**: Functional programming examples
- **Rust**: Systems programming examples

## Development Environment

- **Python Runtime**: PyPy 3.6-7.2.0 for performance optimization in competitive programming
- **Build Tools**: 
  - Make (for OS development projects)
  - NASM assembler for assembly code
  - Custom toolchain in `30daysOS/z_tools/`

## Common Commands

### Running Python Solutions
```bash
# For competitive programming problems
python3 solution.py < input.txt

# Using PyPy for performance
pypy3 solution.py < input.txt
```

### OS Development (30daysOS)
```bash
# Build OS image
cd 30daysOS/day3  # or day4
make

# Clean build artifacts
make clean
```

### Testing Solutions
```bash
# Run with sample input
python3 problem.py < sample_input.txt

# Compare output
python3 problem.py < input.txt > output.txt
diff output.txt expected_output.txt
```

## Libraries and Frameworks

### Python Standard Libraries
- `collections`: defaultdict, deque for data structures
- `heapq`: Priority queues for algorithms like Dijkstra
- `bisect`: Binary search operations
- `itertools`: Combinatorial operations
- `math`: Mathematical functions

### Custom Algorithm Libraries
Located in `Libs/` directory:
- Graph algorithms (Dijkstra, Union-Find, etc.)
- Data structures (Segment Tree, Trie)
- Mathematical utilities (GCD, prime generation)
- Search and sorting algorithms

## Code Style Conventions

- Follow Python PEP 8 for general formatting
- Use descriptive variable names for algorithm implementations
- Include time/space complexity comments for algorithms
- Optimize for competitive programming performance when needed
- Use Japanese comments for contest-specific notes when appropriate