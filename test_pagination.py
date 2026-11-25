"""A small example for reviewing a pagination change."""

import unittest


def page_count(item_count: int, page_size: int) -> int:
    """Return the number of pages needed to display all items."""
    if item_count < 0:
        raise ValueError("item_count must be non-negative")
    if page_size <= 0:
        raise ValueError("page_size must be positive")
    return (item_count + page_size - 1) // page_size


class PageCountTests(unittest.TestCase):
    def test_empty_collection(self):
        self.assertEqual(page_count(0, 10), 0)

    def test_exact_multiple(self):
        self.assertEqual(page_count(20, 10), 2)

    def test_partial_last_page(self):
        self.assertEqual(page_count(21, 10), 3)

    def test_invalid_arguments(self):
        for arguments in [(-1, 10), (10, 0), (10, -1)]:
            with self.subTest(arguments=arguments):
                with self.assertRaises(ValueError):
                    page_count(*arguments)


if __name__ == "__main__":
    unittest.main()
