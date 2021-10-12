import unittest

from phone_number import PhoneNumber


class PhoneNumberTest(unittest.TestCase):
    def test_1(self):
        ph = PhoneNumber("+1(858)775-2868")

        self.assertEqual("+1(858)775-2868", ph.getOriginalText())
        self.assertEqual("+18587752868",  ph.getStrippedNumber())
        self.assertEqual("(858)775-2868",  ph.getValueAsNorthAmerican())
        self.assertEqual("+1.858.775.2868",  ph.getValueAsInternational())

    def test_2(self):
        ph = PhoneNumber("+1(858)775-2868x123")

        self.assertEqual("+1(858)775-2868x123", ph.getOriginalText())
        self.assertEqual("+18587752868x123", ph.getStrippedNumber())
        self.assertEqual("(858)775-2868x123", ph.getValueAsNorthAmerican())
        self.assertEqual("+1.858.775.2868x123", ph.getValueAsInternational())

    def test_3(self):
        ph = PhoneNumber("+598.123.4567x858")

        self.assertEqual("+598.123.4567x858",ph.getOriginalText())
        self.assertEqual("+5981234567x858",ph.getStrippedNumber())
        self.assertEqual(None,ph.getValueAsNorthAmerican())
        self.assertEqual("+598.123.456.7x858",ph.getValueAsInternational())


    def test_4(self):
        ph = PhoneNumber("+27 1234 5678 ext 4")

        self.assertEqual("+27 1234 5678 ext 4",ph.getOriginalText())
        self.assertEqual("+2712345678x4",ph.getStrippedNumber())
        self.assertEqual(None,ph.getValueAsNorthAmerican())
        self.assertEqual("+27 1234 5678 ext 4",ph.getValueAsInternational())


    def test_5(self):
        ph = PhoneNumber("858-775-2868")

        self.assertEqual("858-775-2868",ph.getOriginalText())
        self.assertEqual("+18587752868",ph.getStrippedNumber())
        self.assertEqual("(858)775-2868",ph.getValueAsNorthAmerican())
        self.assertEqual("+1.858.775.2868",ph.getValueAsInternational())