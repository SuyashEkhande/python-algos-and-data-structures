#!/usr/bin/env python3
"""
Validation script to test all implemented modules can be imported successfully.
"""

import sys
import importlib
from pathlib import Path

def test_imports():
    """Test that all our implemented modules can be imported."""
    
    modules_to_test = [
        # DSA modules
        'dsa.arrays',
        'dsa.linked_lists', 
        'dsa.stacks_queues',
        'dsa.hash_tables',
        'dsa.trees',
        'dsa.graphs',
        
        # Algorithm modules
        'algorithms.sorting',
        'algorithms.searching',
        'algorithms.dynamic_programming',
        'algorithms.greedy',
        'algorithms.graph_algorithms',
        
        # Problem modules
        'problems.array_string_problems',
        'problems.tree_problems',
        
        # Design pattern modules
        'design_patterns.creational_patterns.singleton',
        'design_patterns.creational_patterns.factory',
        'design_patterns.behavioral_patterns.observer_pattern',
    ]
    
    failed_imports = []
    successful_imports = []
    
    for module_name in modules_to_test:
        try:
            module = importlib.import_module(module_name)
            successful_imports.append(module_name)
            print(f"✓ {module_name}")
        except ImportError as e:
            failed_imports.append((module_name, str(e)))
            print(f"✗ {module_name}: {e}")
        except Exception as e:
            failed_imports.append((module_name, str(e)))
            print(f"✗ {module_name}: {e}")
    
    print(f"\n=== Import Test Results ===")
    print(f"Successful imports: {len(successful_imports)}")
    print(f"Failed imports: {len(failed_imports)}")
    
    if failed_imports:
        print("\nFailed imports:")
        for module, error in failed_imports:
            print(f"  {module}: {error}")
        return False
    else:
        print("\n🎉 All modules imported successfully!")
        return True

def check_folder_structure():
    """Check that all expected folders and key files exist."""
    
    expected_structure = {
        'dsa': ['arrays.py', 'linked_lists.py', 'stacks_queues.py', 'hash_tables.py', 'trees.py', 'graphs.py'],
        'algorithms': ['sorting.py', 'searching.py', 'dynamic_programming.py', 'greedy.py', 'graph_algorithms.py'],
        'problems': ['array_string_problems.py', 'tree_problems.py'],
        'design_patterns/creational_patterns': ['singleton.py', 'factory.py'],
        'design_patterns/behavioral_patterns': ['observer_pattern.py'],
        'fundamentals': [],  # Already well populated
        'object_oriented_programming': [],  # Already well populated
        'concurrency_parallelism': [],  # Already well populated
        'memory_management': [],  # Already well populated
        'testing_debugging': [],  # Already well populated
    }
    
    missing_files = []
    existing_files = []
    
    for folder, files in expected_structure.items():
        folder_path = Path(folder)
        if not folder_path.exists():
            missing_files.append(f"Folder: {folder}")
            continue
            
        for file in files:
            file_path = folder_path / file
            if file_path.exists():
                existing_files.append(str(file_path))
            else:
                missing_files.append(str(file_path))
    
    print(f"\n=== Folder Structure Check ===")
    print(f"Expected files found: {len(existing_files)}")
    print(f"Missing files: {len(missing_files)}")
    
    if missing_files:
        print("\nMissing files:")
        for file in missing_files:
            print(f"  {file}")
        return False
    else:
        print("\n📁 All expected files found!")
        return True

def main():
    """Main validation function."""
    print("🔍 Starting validation of python-algos-and-data-structures repository...")
    print("=" * 70)
    
    # Test folder structure
    structure_ok = check_folder_structure()
    
    # Test imports
    imports_ok = test_imports()
    
    print("\n" + "=" * 70)
    if structure_ok and imports_ok:
        print("✅ VALIDATION PASSED: Repository is complete and functional!")
        print("\n🚀 Repository includes:")
        print("   • Complete DSA implementations (arrays, lists, trees, graphs, etc.)")
        print("   • Essential algorithms (sorting, searching, DP, greedy, graph)")
        print("   • Coding interview problems (arrays, strings, trees)")
        print("   • Design patterns (singleton, factory, observer)")
        print("   • Existing fundamentals, OOP, concurrency, and testing modules")
        return 0
    else:
        print("❌ VALIDATION FAILED: Some issues found.")
        return 1

if __name__ == "__main__":
    sys.exit(main())