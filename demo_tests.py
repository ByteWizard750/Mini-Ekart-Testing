#!/usr/bin/env python3
import subprocess
import sys

def run_feature_tests(feature_name):
    print(f"Running tests for: {feature_name}")
    print("=" * 40)
    try:
        cmd = [
            sys.executable, "-m", "behave",
            f"features/{feature_name}.feature",
            "--format=pretty",
            "--no-capture"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("STDERR:")
            print(result.stderr)
        print(f"{feature_name} tests finished with code: {result.returncode}")
        return result.returncode == 0
    except Exception as e:
        print(f"Error running {feature_name} tests: {e}")
        return False

def main():
    print("Mini E-Kart Test Runner")
    print("=" * 40)
    features = ["add_to_cart", "remove_from_cart", "total_price", "empty_cart"]

    print("Available test features:")
    for i, f in enumerate(features, 1):
        print(f"{i}. {f}")
    print("5. Run all tests")
    print("0. Exit")

    try:
        choice = input("Enter your choice (0-5): ").strip()
        if choice == "0":
            print("Exiting...")
            return
        elif choice == "5":
            subprocess.run([sys.executable, "run_tests.py"])
        elif choice in ["1", "2", "3", "4"]:
            feature = features[int(choice) - 1]
            run_feature_tests(feature)
        else:
            print("Invalid option. Please enter 0-5.")
    except KeyboardInterrupt:
        print("\nStopped by user.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()