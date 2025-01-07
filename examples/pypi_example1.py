from katakana.core.loader import LookupRunner, LookupType

runner = LookupRunner()

print(runner.run_lookup(LookupType.PYPI_PACKAGE, "")) # Package name