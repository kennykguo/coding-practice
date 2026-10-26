"""Run from this folder with Python containing cocotb 2.0.0 and Icarus on PATH."""
from pathlib import Path
import json
import platform
import subprocess
from importlib.metadata import version
import tempfile
import xml.etree.ElementTree as ET
from cocotb_tools.runner import get_runner

ROOT = Path(__file__).resolve().parent
CASES = [("counter", {"LIMIT": n}) for n in (1, 3, 10, 16)]
CASES += [("sync_fifo", {"DEPTH": n}) for n in (1, 3, 8)]
CASES += [(name, {}) for name in
          ("rv_register", "sync_ram", "mac", "weight_bank", "stream_sum", "lane_adders")]

def main():
    report = []
    with tempfile.TemporaryDirectory(prefix="sv-refresher-") as folder:
        for index, (top, parameters) in enumerate(CASES):
            build = Path(folder) / f"{index}-{top}"
            runner = get_runner("icarus")
            runner.build(sources=[ROOT / "examples" / f"{top}.sv"],
                         hdl_toplevel=top, parameters=parameters,
                         build_dir=build, build_args=["-g2012"], always=True)
            result = build / "results.xml"
            runner.test(hdl_toplevel=top, test_module="test_blocks",
                        test_dir=ROOT / "tests", build_dir=build,
                        extra_env={"CASE": top, **{k: str(v) for k, v in parameters.items()}},
                        results_xml=result)
            tree = ET.parse(result)
            assert not tree.findall(".//failure") and not tree.findall(".//error"), top
            report.append({"module": top, "parameters": parameters, "passed": True})
        build = Path(folder) / "shown-cocotb-example"
        runner = get_runner("icarus")
        runner.build(sources=[ROOT / "examples" / "rv_register.sv"],
                     hdl_toplevel="rv_register", build_dir=build, always=True)
        result = build / "results.xml"
        runner.test(hdl_toplevel="rv_register", test_module="test_elastic",
                    test_dir=ROOT / "examples", build_dir=build, results_xml=result)
        tree = ET.parse(result)
        assert not tree.findall(".//failure") and not tree.findall(".//error")
        report.append({"module": "printed cocotb example", "passed": True})
    (ROOT / "verification.json").write_text(json.dumps({"python": platform.python_version(), "cocotb": version("cocotb"), "simulator": subprocess.run(["iverilog", "-V"], capture_output=True, text=True, check=True).stdout.splitlines()[0], "random_seed": 426, "cases": report}, indent=2) + "\n")
    print(f"PASS: {len(report)} simulation configurations/tests")

if __name__ == "__main__":
    main()
