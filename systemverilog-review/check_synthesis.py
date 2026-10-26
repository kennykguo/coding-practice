"""Basic generic synthesis checks; no technology mapping or timing claims."""
from pathlib import Path
import json
import subprocess

ROOT = Path(__file__).resolve().parent
TOPS = ("counter", "rv_register", "sync_fifo", "sync_ram", "mac", "weight_bank", "stream_sum")

def main():
    reports = []
    for top in TOPS:
        script = (f"read_verilog -sv examples/{top}.sv; "
                  f"hierarchy -check -top {top}; proc; check -assert; "
                  "select -assert-none t:$dlatch")
        result = subprocess.run(["yosys", "-Q", "-T", "-p", script],
                                cwd=ROOT, capture_output=True, text=True)
        if result.returncode:
            raise RuntimeError(result.stdout + result.stderr)
        reports.append({"module": top, "default_parameters": True, "passed": True})
    version = subprocess.check_output(["yosys", "-V"], text=True).strip()
    (ROOT / "synthesis-checks.json").write_text(json.dumps({
        "tool": version, "checks": reports,
        "scope": "Parse, hierarchy, process lowering, structural check, and no inferred latches. No technology mapping or timing analysis."
    }, indent=2) + "\n")
    print(f"PASS: {len(reports)} generic synthesis checks")

if __name__ == "__main__":
    main()
