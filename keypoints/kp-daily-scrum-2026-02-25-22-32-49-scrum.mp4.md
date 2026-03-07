# Keypoints

Source: `2026-02-25 22-32-49 scrum.mp4`

### 1. High priority tickets from Jamal

Amar had a call with Jamal who flagged four high-priority tickets. Also discussed a mobile app mailto link issue — Marcus sent details to investigate the app config XML fix.

- 6839 — enterprise customer, assigned to Jayr
- 7055 — in progress
- 7237 — AI chat repeated numbering bug, assigned to Marcus
- 7259 — assigned to Jayr
- 7290 — mobile app mailto link issue

### 2. Jayr's update

- 7259 — ready for QA testing
- 7310 — phase one notifications overhaul, pushed to DevEU with significant changes, also moved to QA
- 7237 — high-priority, assigned to him, will check
- 6839 — high-priority, assigned to him, will check

### 3. SK's update

- 7079 — pushed to prod and closed
- 7187 — pushed to prod and closed
- 7046 — went to prod but not working for one specific account; cloning production DB to debug, progress is slow
- 7292 — in progress
- 7007 — needs to be put in a dev environment for QA testing

### 4. Marius's update

Completed ticket 7307. Now looking back at 7299 which has a possible issue — it crashed when it got to FKW, investigating.

### 5. Mihai's update

Two high-priority tickets fixed: 7229 (duplicate play events from player — fixed on front end and back end, tested on ephemeral, waiting for code review) and 7313 (save/discard functionality bug in playlists — also done). Will also look at mobile app ticket 7290. Three more tickets done yesterday waiting for code review; may do another prod push if enough tickets are ready.

### 6. Atanas's webhook calls table partitioning

Restored production DB cluster snapshot and tested partitioning approach — modifying indices takes ~10s, partitioning takes ~10s, feasible for early-morning production run. Problem: Laravel doesn't natively support table partitioning migrations; the only external package supports PostgreSQL only (MySQL coming). Considering two options: (1) external cron job to create/drop partitions daily + manual partitioning change, or (2) stick with existing daily row deletion (works but causes more I/O). Still deciding.

### 7. Marcus's update

Finished testing his new app updates pipeline yesterday. Today rolling out updates to all existing client apps using the new pipeline. Will also look at the AI chat ticket (7237). Ticket 7290 (mobile app mailto link) was actually already solved before — it was a mailto link handling edge case missed in one in-house app build. Will investigate who reported it and ensure their app gets updated.

### 8. Alkein's update

Fixed a HubSpot registration issue on the summit page. Started working on blog design. Today researching which database to use since deploying on Vercel.

### 9. Asim's pipeline and workflow assessment

Asim asked about the current dev pipeline — is QA or code review a bottleneck? Mihai said code review was slightly delayed because Marius was off yesterday but will catch up today. Both Marius and Jayr are using Claude Code for code reviews alongside manual review. Asim noted friction points in the code review process he wants to address. QA team (Claudiu) reported it's been more chaotic lately — no single big project focus, lots of support/marketing/bug tickets — but production pushes are happening almost daily and workload is manageable.

### 10. QA team AI tools progress

Sherry created a new test case repository matching the new app structure and is working on smoke regression automation for production pushes. Claudiu built a mention tracker bot for the development and QA Slack channels — provides daily briefings on QA mentions, bugs, and issues, and checks Jira for tickets marked as QA. Still noisy and needs better organization; not yet used daily. Used it a couple of times but needs to make the output more readable.

### 11. Jake's ticket bot and Jayr's superpower skill workflow

Jake's ticket bot (v1) has been in use for 1-2 weeks. Devs have given feedback on replication steps accuracy. Big success: the bot handled the summit checkout and 2FA flow implementation — covered three complex tickets that Jayr and Alkein worked on, with Slack threads of 200+ messages. Saved significant time in ticket logging. Asim asked Jayr about his workflow — Jayr explained he scans Slack threads for context and uses a superpower skill to resolve issues, rather than a full agent system. Asim plans a follow-up discussion on these workflows.

### 12. Andrew's notifications epic and shipping summary request

Andrew, Asim, and Jayr have been working on big-picture notifications — it's a bigger epic raising questions about how it works through the app. Andrew missed the last couple of scrums and requested a summary of everything shipped (bugs, QA fixes) over the past two weeks to get his thoughts together on what's in the queue and what the next big rock will be. Amar agreed to prepare and share the list.

### 13. Mio-Smith Agent bot status and Claude Code as alternative

Adam asked about the Mio-Smith Agent bot status. Asim said it's essentially a stale project — a "dinosaur" compared to what it should be. He and Marcus need to revisit it with a better approach given how tech has evolved. Claude Code in GitHub could potentially replace most of what Mio-Smith Agent does. Marcus confirmed it's in a "technical graveyard" but still functional — however it's still using Asim's tokens, so if Asim has a productive day the bot won't work. Adam will take his questions offline.

### 14. Release schedule reminder

Amar reminded the team to communicate about today's release if there will be an additional one. Tomorrow (Wednesday) is the last day for production releases this week — only urgent pushes on Friday.
