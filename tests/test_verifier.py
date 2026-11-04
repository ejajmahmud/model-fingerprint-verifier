"""Tests for model-fingerprint-verifier."""
import unittest
from model_fingerprint_verifier.verifier import ModelFingerprintVerifier


class TestModelFingerprintVerifier(unittest.TestCase):
    def setUp(self):
        self.v = ModelFingerprintVerifier()

    def test_correct_response_verified(self):
        res = self.v.verify_response("pro-tier", "Calculation: 4373838 is the exact answer.")
        self.assertTrue(res["verified"])
        self.assertEqual(res["status"], "GENUINE")

    def test_wrong_answer_flagged_as_downgrade(self):
        res = self.v.verify_response("pro-tier", "I think the answer is roughly 4000000.")
        self.assertFalse(res["verified"])
        self.assertEqual(res["status"], "SUSPECTED_DOWNGRADE")


if __name__ == "__main__":
    unittest.main()
