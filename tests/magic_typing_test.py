"""Tests for josepy.magic_typing."""
import sys
import unittest
import warnings
from unittest import mock


class MagicTypingTest(unittest.TestCase):
    """Tests for josepy.magic_typing."""
    def test_import_success(self):
        try:
            import typing as temp_typing
        except ImportError:  # pragma: no cover
            temp_typing = None  # pragma: no cover
        typing_class_mock = mock.MagicMock()
        text_mock = mock.MagicMock()
        typing_class_mock.Text = text_mock
        sys.modules['typing'] = typing_class_mock
        if 'josepy.magic_typing' in sys.modules:
            del sys.modules['josepy.magic_typing']  # pragma: no cover
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            from josepy.magic_typing import Text
        self.assertEqual(Text, text_mock)
        del sys.modules['josepy.magic_typing']
        sys.modules['typing'] = temp_typing


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
