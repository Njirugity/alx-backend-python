#!/usr/bin/env python3
""" A script to unit test for utils.access_nested_map
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """ A class to test utils.access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, a, b, expected):
        """Test the return value of a nested map."""
        self.assertEqual(access_nested_map(a, b), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError, 'a'),
        ({"a": 1}, ("a", "b"), KeyError, 'b'),
    ])
    def test_access_nested_map_exception(self, a, b, expceted, expected_key):
        """Test that a KeyError is raised"""
        with self.assertRaises(expceted):
            access_nested_map(a, b)


class TestGetJson(unittest.TestCase):
    """mock requests"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ test that utils.get_json returns the expected result. """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """to mock a_method. Test that when calling a_property twice,
    """
    def test_memoize(self):
        """to mock a_method. Test that when calling a_property twice"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_method:
            my_obj = TestClass()
            first_call = my_obj.a_property
            second_call = my_obj.a_property

            self.assertEqual(first_call, 42)
            self.assertEqual(second_call, 42)

            mock_method.assert_called_once()
