from katakana.core.loader import LookupRunner, LookupType

token = "MTMyMzQ3OTA2Mjc5ODI3MDUwNw.GaQ5i2.rl-7CEULaVfYrOR9RDZ7r_98N-1bcRf6CFOwYo"  # Bot token
runner = LookupRunner(discord_token=token)

print(runner.run_lookup(LookupType.DISCORD_USER, 1219031488016679033))