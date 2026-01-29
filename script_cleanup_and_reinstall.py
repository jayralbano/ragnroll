#!/usr/bin/env python3
"""
Clean HuggingFace cache and reinstall Python packages
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

def main():
    print("\n🧹 Cleanup and Reinstall Script")
    print("=" * 50)

    # Define cache paths
    hf_cache = Path.home() / ".cache" / "huggingface"

    # Show what will be deleted
    print(f"\n📂 HuggingFace cache location: {hf_cache}")

    if hf_cache.exists():
        # Calculate size
        total_size = sum(f.stat().st_size for f in hf_cache.rglob('*') if f.is_file())
        size_mb = total_size / (1024 * 1024)
        print(f"   Current size: {size_mb:.2f} MB")
    else:
        print(f"   Cache doesn't exist yet")

    # Confirm deletion
    print("\n⚠️  This will:")
    print("   1. Delete ALL HuggingFace cache")
    print("   2. Reinstall all Python packages")

    response = input("\nContinue? (yes/no): ").strip().lower()

    if response not in ['yes', 'y']:
        print("\n❌ Cancelled")
        sys.exit(0)

    # Delete HuggingFace cache
    print("\n🗑️  Deleting HuggingFace cache...")
    if hf_cache.exists():
        shutil.rmtree(hf_cache)
        print("   ✅ HuggingFace cache deleted")
    else:
        print("   ℹ️  No cache to delete")

    # Reinstall packages
    print("\n📦 Reinstalling packages with uv...")
    try:
        subprocess.run(
            ["uv", "sync", "--reinstall"],
            check=True
        )
        print("   ✅ Packages reinstalled successfully")
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Failed to reinstall packages: {e}")
        sys.exit(1)

    print("\n✨ Done! Everything is clean and reinstalled.\n")

if __name__ == "__main__":
    main()
