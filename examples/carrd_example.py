from katakana.core.loader import LookupRunner, LookupType

runner = LookupRunner()

print(runner.run_lookup(LookupType.CARRD_USER, "")) # Carrd profile
