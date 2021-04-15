import os

from .utils import TestCase
from .pages.converter import ConverterPage


class MoneyCatConverterTest(TestCase):
    def test_converter_first_field(self):
        self.converter = ConverterPage(self.driver)
        self.converter_form = self.converter.form
        prev = self.converter.Actions.enter_first_field(
            self.converter_form,
            "2"
        )

        self.assertNotEqual(
            self.converter_form.get_second_form_content(),
            prev
        )

    def test_converter_second_field(self):
        self.converter = ConverterPage(self.driver)
        self.converter_form = self.converter.form
        prev = self.converter.Actions.enter_second_field(
            self.converter_form,
            "2"
        )

        self.assertNotEqual(
            self.converter_form.get_first_form_content(),
            prev
        )

    def test_converter_unexceptable_symbols_letters(self):
        self.converter = ConverterPage(self.driver)
        self.converter_form = self.converter.form

        self.converter.Actions.enter_first_field(
            self.converter_form,
            "qwe"
        )

        self.assertEqual(
            self.converter_form.get_first_form_content(),
            ""
        )

    def test_converter_unexceptable_symbols_special_symbols(self):
        self.converter = ConverterPage(self.driver)
        self.converter_form = self.converter.form
        prev = self.converter.Actions.enter_first_field(
            self.converter_form,
            "-!@#$%^&*()_=+"
        )

        self.assertEqual(
            self.converter_form.get_first_form_content(),
            ""
        )

    def test_converter_number_with_point(self):
        self.converter = ConverterPage(self.driver)
        self.converter_form = self.converter.form
        prev = self.converter.Actions.enter_first_field(
            self.converter_form,
           "1.2"
        )

        self.assertNotEqual(
            self.converter_form.get_second_form_content(),
            prev
        )