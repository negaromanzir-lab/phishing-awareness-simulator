
import unittest

from phishing_simulator import SCENARIOS, detect_warning_signs


class TestPhishingSimulator(unittest.TestCase):

    def test_five_scenarios_exist(self):
        self.assertEqual(len(SCENARIOS), 5)

    def test_each_scenario_has_required_fields(self):
        required = {
            "subject", "sender", "message", "answer", "explanation"
        }

        for scenario in SCENARIOS:
            with self.subTest(subject=scenario["subject"]):
                self.assertTrue(required.issubset(scenario.keys()))
                self.assertIn(scenario["answer"], ("p", "l"))

    def test_urgent_message_has_warning(self):
        scenario = {
            "subject": "Urgent account suspension",
            "sender": "Security <security@example.invalid>",
            "message": "Act immediately to verify your password",
        }

        warnings = detect_warning_signs(scenario)

        self.assertTrue(any("Urgency" in w for w in warnings))
        self.assertTrue(any("sensitive information" in w for w in warnings))

    def test_link_is_detected(self):
        scenario = {
            "subject": "Review this",
            "sender": "Example <sender@example.invalid>",
            "message": "Visit http://example.invalid/page",
        }

        warnings = detect_warning_signs(scenario)

        self.assertTrue(any("link" in w.lower() for w in warnings))

    def test_macro_warning_is_detected(self):
        scenario = {
            "subject": "Invoice",
            "sender": "Billing <billing@example.invalid>",
            "message": "Open the attachment and enable macros",
        }

        warnings = detect_warning_signs(scenario)

        self.assertTrue(any("attachment" in w.lower() for w in warnings))

    def test_detection_returns_a_list(self):
        warnings = detect_warning_signs(SCENARIOS[0])

        self.assertIsInstance(warnings, list)


if __name__ == "__main__":
    unittest.main(verbosity=2)
