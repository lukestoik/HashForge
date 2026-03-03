# test_hashforge.py
"""
Tests for HashForge module.
"""

import unittest
from hashforge import HashForge

class TestHashForge(unittest.TestCase):
    """Test cases for HashForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HashForge()
        self.assertIsInstance(instance, HashForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HashForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
