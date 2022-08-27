# Why NOT to use Repl as a hosting platform

# You should not use Repl.it to host your bot.
It may be a nice option as its "free" but you should use something else considering the major flaws.

- The machines are super underpowered.
- - This means your bot will lag a lot as it gets bigger.
- You'll need a web server alongside your bot to prevent it from being shut off. 
- - This isn't a trivial task, and eats more of the machines power.
- Repl.it uses an ephemeral file system.
- - This means any file you saved via your bot will be overwritten when you next launch.

# IMPORTATNT
- They use a shared IP for everything running on the service.
This one is important - if someone is running a user bot on their service and gets banned, everyone on that IP will be banned. Including you.

Please avoid using repl.it to host your bot. It's not worth the trouble.

If you're looking for free options, consider using AWS/Google Cloud Platform/Azure and its respective free tiers or just pay for an actual VPS.
