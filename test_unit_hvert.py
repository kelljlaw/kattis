"""unittesting 6 cases from hvert.py
"""


___author__ = "Kelly Jo Law"
__date__ = "October 24, 2023"


import unittest
from hvert import determine_contest_site


class DetermineContestSite(unittest.TestCase):
    """Class for test cases

    Args:
        unittest Testcase
    """
    def test_reykjavik(self) -> None:
        """Test case for Reykjavik
        """
        city = "Reykjavik"
        actual_result = determine_contest_site(city)
        expected_result = "Reykjavik"
        self.assertEqual(actual_result, expected_result)

    def test_kopavogur(self) -> None:
        """Test case for Kopavogur
        """
        city = "Kopavogur"
        actual_result = determine_contest_site(city)
        expected_result = "Reykjavik"
        self.assertEqual(actual_result, expected_result)

    def test_hafnarfjordur(self) -> None:
        """Test case for Hafnarfjordur
        """
        city = "Hafnarfjordur"
        actual_result = determine_contest_site(city)
        expected_result = "Reykjavik"
        self.assertEqual(actual_result, expected_result)

    def test_akureyri(self) -> None:
        """Test case for Akureyri
        """
        city = "Akureyri"
        actual_result = determine_contest_site(city)
        expected_result = "Akureyri"
        self.assertEqual(actual_result, expected_result)

    def test_gardabaer(self) -> None:
        """Test case for Gardabaer
        """
        city = "Gardabaer"
        actual_result = determine_contest_site(city)
        expected_result = "Reykjavik"
        self.assertEqual(actual_result, expected_result)

    def test_mosfellsbaer(self) -> None:
        """Test case for Mosfellsbaer
        """
        city = "Mosfellsbaer"
        actual_result = determine_contest_site(city)
        expected_result = "Reykjavik"
        self.assertEqual(actual_result, expected_result)
