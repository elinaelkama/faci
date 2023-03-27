# faci
is a Discord bot, that makes reading audit logs easier and helps keep your server up to date with scheduled events
## Usage and Set Up
to set up the bot on your server you just need to invite faci to join via link: https://discord.com/api/oauth2/authorize?client_id=1054417255389216859&permissions=3216&scope=bot
or from [discords.com/bots](https://discords.com/bots/bot/1054417255389216859)
### Audit Log
![image](https://user-images.githubusercontent.com/95315272/227977264-113e5aa0-9fc4-48a2-9b8f-449f7875ae65.png)

To use audit log you need to create a text channel with a name that starts with **audit**

*note: it's recommended that the channel be visible only to moderators*

Current events that are posted to the audit-channel
- An invite is created
- New member joins
- A member leaves
- A member is kicked
- A member is banned
- A member is on a timeout
- A user is unbanned
### Scheduled Events
![image](https://user-images.githubusercontent.com/95315272/227977482-0731f7a7-442c-4556-b025-2008c95eff44.png)

Like the audit log, you'll need to create a text channel with the name that starts with **event**

*note: this one is recommeded to be visible to everyone*

Current event-related events that are posted to the event-channel
- Event is created
- Event information is updated
- Event is deleted
### Commands
![image](https://user-images.githubusercontent.com/95315272/227976915-e7385c95-b1d3-40ed-963a-cf5e3841a935.png)
All faci commands start with the !-prefix.
1. !choose 
*get a random option from a comma separated list you provide*

example: !choose pancakes, bacon and eggs, hashbrowns

2. !joined 

*returns the time you joined and how long you've been on the server*

3. !created 

*gets the time the server was created and it's age*
## Reporting bugs
To report your possible experienced bugs, please use the Issues tab in GitHub
