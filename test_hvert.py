"""unittesting 6 cases from hvert.py
"""

___author__ = "Kelly Jo Law"
__date__ = "October 24, 2023"

import sys
from hvert import determine_contest_site


def test_hvert() -> None:
    """Test hvert.py answer
    """
    assert determine_contest_site("Reykjavik") == "Reykjavik"
    assert determine_contest_site("Kopavogur") == "Reykjavik"
    assert determine_contest_site("Hafnarfjordur") == "Reykjavik"
    assert determine_contest_site("Akureyri") == "Akureyri"
    assert determine_contest_site("Gardabaer") == "Reykjavik"
    assert determine_contest_site("Mosfellsbaer") == "Reykjavik"
    print('all test casses passed...', file=sys.stderr)
