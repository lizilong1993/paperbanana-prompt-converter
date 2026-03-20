import json
from pathlib import Path

from paperbanana_converter import run_single_conversion


def run() -> int:
    base = Path(__file__).resolve().parent
    cases = json.loads((base / "test_cases.json").read_text(encoding="utf-8"))
    passed = 0
    for case in cases:
        result = run_single_conversion(case["input"])
        converted = result["converted_prompt"]
        ok = all(k.lower() in converted.lower() for k in case["expected_keywords"])
        improved = result["comparison"]["improvement"] >= 0
        valid_score = result["validation"]["score"] >= 75
        if ok and improved and valid_score:
            passed += 1
        print(f"[{case['id']}] ok={ok} improved={improved} valid_score={result['validation']['score']} improvement={result['comparison']['improvement']}")
    total = len(cases)
    print(f"passed={passed}/{total}")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(run())
