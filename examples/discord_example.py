from katakana.core.loader import LookupRunner, LookupType

token = ""  # Bot token
runner = LookupRunner(discord_token=token)

print(runner.run_lookup(LookupType.DISCORD_USER, 1219031488016679033)) # User ID here, that is my user ID as an example.
