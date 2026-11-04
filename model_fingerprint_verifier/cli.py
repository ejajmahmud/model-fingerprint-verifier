"""CLI for model-fingerprint-verifier."""
import sys
import argparse
from .verifier import ModelFingerprintVerifier


def main():
    parser = argparse.ArgumentParser(description="Model Fingerprint Verifier")
    parser.add_argument("--answer", default="The result is 4373838", help="Answer text")
    args = parser.parse_args()

    v = ModelFingerprintVerifier()
    res = v.verify_response("pro-tier", args.answer)
    print(f"Verification status: {res['status']} (Confidence: {res['confidence']})")
    sys.exit(0)


if __name__ == "__main__":
    main()
