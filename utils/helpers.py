import json

def load_config(path="config.json"):
    """Load user infrastructure config"""
    with open(path) as f:
        return json.load(f)


def format_score(score):
    """Convert numeric score into label"""
    if score >= 70:
        return "HIGH RISK"
    elif score >= 40:
        return "MODERATE RISK"
    else:
        return "LOW RISK"


def print_report(score, issues):
    """Pretty CLI output"""
    print("\n🔍 ResilienceLens Report")
    print("=" * 35)

    risk_level = format_score(score)
    print(f"Resilience Score: {score}/100 ({risk_level})\n")

    if issues:
        print("Issues Detected:")
        for issue in issues:
            print(f"⚠ {issue}")
    else:
        print("✅ No major issues detected")