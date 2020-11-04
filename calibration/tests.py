from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from calibration.models import Analysis


class AnalysisModelTests(TestCase):
    def setUp(self):
        self.analysis = Analysis.objects.create(
            analysis_name="Nome da Análise",
            substance_name="Nome da Substância",
            absorbance="0.1516,0.3826,0.4281,0.6545,0.7118,0.9565",
            concentration="0.20,0.40,0.60,0.80,1.00,1.2",
        )

    def test_instance(self):
        self.analysis.full_clean()
        self.analysis.save()

        self.assertIsInstance(self.analysis, Analysis)
        self.assertEqual(self.analysis.analysis_name, "Nome da Análise")
        self.assertEqual(self.analysis.substance_name, "Nome da Substância")
        self.assertEqual(
            self.analysis.absorbance, "0.1516,0.3826,0.4281,0.6545,0.7118,0.9565"
        )
        self.assertEqual(self.analysis.concentration, "0.20,0.40,0.60,0.80,1.00,1.2")

    def test_analysis_name_not_null(self):
        self.analysis.analysis_name = None

        with self.assertRaises(ValidationError):
            self.analysis.full_clean()

        with self.assertRaises(IntegrityError):
            self.analysis.save()

    def test_analysis_name_not_blank(self):
        self.analysis.analysis_name = ""

        with self.assertRaises(ValidationError):
            self.analysis.full_clean()

    def test_analysis_name_lesser_than_max_length(self):
        expected_analysis_name = "x" * 255
        self.analysis.analysis_name = expected_analysis_name
        self.analysis.save()

        self.analysis.full_clean()
        self.assertEqual(self.analysis.analysis_name, expected_analysis_name)

    def test_analysis_name_greater_than_max_length(self):
        expected_analysis_name = "x" * 256
        self.analysis.analysis_name = expected_analysis_name
        self.analysis.save()

        with self.assertRaises(ValidationError):
            self.analysis.full_clean()

    def test_substance_name_not_null(self):
        self.analysis.substance_name = None

        with self.assertRaises(ValidationError):
            self.analysis.full_clean()

        with self.assertRaises(IntegrityError):
            self.analysis.save()

    def test_substance_name_not_blank(self):
        self.analysis.substance_name = ""

        with self.assertRaises(ValidationError):
            self.analysis.full_clean()

    def test_substance_name_lesser_than_max_length(self):
        expected_substance_name = "x" * 255
        self.analysis.substance_name = expected_substance_name
        self.analysis.save()

        self.analysis.full_clean()
        self.assertEqual(self.analysis.substance_name, expected_substance_name)

    def test_substance_name_greater_than_max_length(self):
        expected_substance_name = "x" * 256
        self.analysis.substance_name = expected_substance_name
        self.analysis.save()

        with self.assertRaises(ValidationError):
            self.analysis.full_clean()

    def test_absorbance_not_null(self):
        self.analysis.absorbance = None

        with self.assertRaises(ValidationError):
            self.analysis.full_clean()

        with self.assertRaises(IntegrityError):
            self.analysis.save()

    def test_absorbance_not_blank(self):
        self.analysis.absorbance = ""

        with self.assertRaises(ValidationError):
            self.analysis.full_clean()

    def test_absorbance_lesser_than_max_length(self):
        expected_absorbance = "x" * 255
        self.analysis.absorbance = expected_absorbance
        self.analysis.save()

        self.analysis.full_clean()
        self.assertEqual(self.analysis.absorbance, expected_absorbance)

    def test_absorbance_greater_than_max_length(self):
        expected_absorbance = "x" * 256
        self.analysis.absorbance = expected_absorbance
        self.analysis.save()

        with self.assertRaises(ValidationError):
            self.analysis.full_clean()

    def test_concentration_not_null(self):
        self.analysis.concentration = None

        with self.assertRaises(ValidationError):
            self.analysis.full_clean()

        with self.assertRaises(IntegrityError):
            self.analysis.save()

    def test_concentration_not_blank(self):
        self.analysis.concentration = ""

        with self.assertRaises(ValidationError):
            self.analysis.full_clean()

    def test_concentration_lesser_than_max_length(self):
        expected_concentration = "x" * 255
        self.analysis.concentration = expected_concentration
        self.analysis.save()

        self.analysis.full_clean()
        self.assertEqual(self.analysis.concentration, expected_concentration)

    def test_concentration_greater_than_max_length(self):
        expected_concentration = "x" * 256
        self.analysis.concentration = expected_concentration
        self.analysis.save()

        with self.assertRaises(ValidationError):
            self.analysis.full_clean()

    def test_get_absolute_url(self):
        expected_absolute_url = f"/analysis/{self.analysis.pk}"
        self.assertEqual(self.analysis.get_absolute_url(), expected_absolute_url)

    def test_get_str(self):
        expected_str = f"Nome da Análise -> Nome da Substância -> {self.analysis.pk}"
        self.assertEqual(str(self.analysis), expected_str)
