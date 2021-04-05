import unittest
import i18n

class TestI18n(unittest.TestCase):
    def test(self):
        i18n.set("locale", "km")
        txt = i18n.t("hi")
        print(txt)
        assert txt == "សួស្ដី"

        i18n.set("locale", "en")
        txt = i18n.t("hi")
        print(txt)
        assert txt == "hi"


