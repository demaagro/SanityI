# test_sanityio.py
"""
Tests for SanityIO module.
"""

import unittest
from sanityio import SanityIO

class TestSanityIO(unittest.TestCase):
    """Test cases for SanityIO class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SanityIO()
        self.assertIsInstance(instance, SanityIO)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SanityIO()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
