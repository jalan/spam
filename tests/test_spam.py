"""Tests for the spam module."""

import unittest

import spam


class SystemTest(unittest.TestCase):
    """Tests for spam.system."""

    def test_true(self):
        status = spam.system("true")
        self.assertEqual(status, 0)

    def test_false(self):
        status = spam.system("false")
        self.assertEqual(status, 1)

    def test_command(self):
        status = spam.system("ls")
        self.assertEqual(status, 0)

    def test_command_with_args(self):
        status = spam.system("ls -l")
        self.assertEqual(status, 0)

    def test_command_with_invalid_args(self):
        status = spam.system("ls --unrecognized-option")
        self.assertEqual(status, 2)

    def test_command_not_found(self):
        status = spam.system("command_not_found")
        self.assertEqual(status, 127)

    def test_wrong_arg_type(self):
        with self.assertRaises(TypeError):
            spam.system(0)


class CheckSystemTest(unittest.TestCase):
    """Tests for spam.check_system."""

    def test_true(self):
        spam.check_system("true")

    def test_false(self):
        with self.assertRaises(spam.Error):
            spam.check_system("false")

    def test_command(self):
        spam.check_system("ls")

    def test_command_with_args(self):
        spam.check_system("ls -l")

    def test_command_with_invalid_args(self):
        with self.assertRaises(spam.Error):
            spam.check_system("ls --unrecognized-option")

    def test_command_not_found(self):
        with self.assertRaises(spam.Error):
            spam.check_system("command_not_found")

    def test_wrong_arg_type(self):
        with self.assertRaises(TypeError):
            spam.check_system(0)
