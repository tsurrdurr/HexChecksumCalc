import unittest2
import hexcalc

class TestClass(unittest2.TestCase):
    def test__get_new_hex__input_hex_bad__returns_response(self):
        result = hexcalc.get_new_hex("LUL")
        self.assertEqual("Bad input", result)

    def test__get_new_hex__input_hex_ok19_returns_response(self):
        result = hexcalc.get_new_hex(":106A6000040510060708091369281408D327140819")
        self.assertEqual("Checksum correct", result)

    def test__get_new_hex__input_hex_okB7_returns_response(self):
        result = hexcalc.get_new_hex(":1068600048710620E062206AC06ABDE870400047B7")
        self.assertEqual("Checksum correct", result)

    def test__get_new_hex__input_hex_okED__returns_response(self):
        result = hexcalc.get_new_hex(":1068F000CC3B8DAF96680A2136CB1A4CE47E94E2ED")
        self.assertEqual("Checksum correct", result)

    def test__get_new_hex__input_hex_ok4bytes_returns_response(self):
        result = hexcalc.get_new_hex(":047FFC00FFFFFFFF85")
        self.assertEqual("Checksum correct", result)

    def test__get_new_hex__input_hex_too_long4bytes_returns_response(self):
        result = hexcalc.get_new_hex(":047FFC00FFFFFFFF185")
        self.assertEqual("Too long", result)

    def test__get_new_hex__input_hex_longer__returns_response(self):
        result = hexcalc.get_new_hex(":1068F000CC3B8DAF96680A2136CB1A4CE47E94E2123ED")
        self.assertEqual("Too long", result)

    def test__get_new_hex__input_hex_too_short4bytes_returns_response(self):
        result = hexcalc.get_new_hex(":047FFC00FFFFFFF")
        self.assertEqual("Too short", result)

    def test__get_new_hex__input_hex_shorter__returns_response(self):
        result = hexcalc.get_new_hex(":1068F000CC3B8DAF96680A2136CB1A4CEED")
        self.assertEqual("Too short", result)

    def test__get_new_hex__input_hex_incorrect_checksum__returns_new_hex(self):
        result = hexcalc.get_new_hex(":1068F000CC3B8DAF96680A2136CB1A4CE47E94E212")
        self.assertEqual(":1068F000CC3B8DAF96680A2136CB1A4CE47E94E2ED", result)

if __name__ == "__main__":
    unittest2.main()