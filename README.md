# biscord-dot
General Bot for discord that I am going to progressively add functionality to

Current Features:
- Automatic updates of stock prices will be sent to the owner/host of the discord bot.
  #Note This functionality will be transitioned to a user base and likely local db rather than just storing host id and sending prices to the host.

Setup:
1. Specify correct ID, Tokens in .env as follows:\n
  DISCORD_TOKEN=xxx.xx.xxx
  OWNER_ID=xx

1.1 Stocks:\n
1.1.1 Add desired stocks to .env in the format of a JSON string that can be parsed as a list e.g STOCKS='["COL:ASX", "DOW:ASX"] 
