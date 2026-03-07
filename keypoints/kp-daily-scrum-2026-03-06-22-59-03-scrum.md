# Keypoints

Source: `2026-03-06 22-59-03 scrum_transcribed.txt`

### 1. Trial cancellation resume button broken (7369) — HIGH PRIORITY

Claudiu reported that the "resume subscription" button on the subscription page doesn't work for trial accounts — it fails to remove the scheduled cancellation, meaning users who want to reactivate their trial (and eventually pay) are blocked. No visible errors in network/console. Jayr already investigated via Claude Code and added a fix suggestion in the ticket. Assigned to Jayr as owner, but can be reassigned. Jake and Adam flagged this as high priority due to direct financial/revenue impact.

### 2. DB cleanup tickets and AWS cost optimization epic (7364, 7365, 7366, 6384)

Jake raised three DB cleanup tickets he logged: 7364 (activity log table cleanup, synced with Asim — biggest cost driver), 7365 (expired magic links table cleanup), and 7366 (failed jobs table cleanup). Alkein pointed out these are duplicates of tickets that already exist under epic 6384 (AWS cost optimization) and noted the activity log table has code dependencies (custom model traits, an Elasticsearch index) that need to be fully removed rather than just toggling off. Jake pushed to expedite the epic rather than continuing to kick it down the road; Adam will coordinate offline with the team to prioritize quick wins.

### 3. Jayr's notification epic updates (7354, 7350, 7355, 7353)

Jayr is auditing notification code using a human+AI hybrid approach across four tickets: 7354 (UI testing — found issues, had to re-spin AI for fixes), 7350 (manual testing with agent corrections and memory/training storage), 7355 (requires mobile testing — Claudiu and Marcus already have an initial discussion thread), and 7353 (received feedback from Claudiu, code is up on comments environment with further fixes needed). A key blocker is lack of a UI testing pipeline, forcing manual testing. Adam offered support team resources (Jamal, Brandon, Rashid) for manual UI testing once Jayr gets environments ready; they agreed to discuss a preferred test template offline.

### 4. Adam's push for Jira ticket documentation

Adam called out a recurring problem: discussions and context are happening in Slack threads but not making it into Jira tickets, leaving tickets with no detail or transparency. He emphasized this is an "everybody thing" and urged the team to start capturing conversation details in tickets. Marcus suggested linking Slack threads directly into tickets (as support already does) rather than re-summarizing; Adam agreed the key goal is simply having transparency on tickets regardless of method.

### 5. Marcus's updates — mobile app builder backend (7016, 7017), AI chat numbering fix, and shared secret storage

Marcus is spinning up a test app for Jayr and continuing work on tickets 7016 and 7017 (backend connection for mobile app builder integration with the platform). The AI chat numbering support ticket (Wayne Stiles) is still in progress but lower priority — Marcus hasn't been able to replicate the issue, and Adam suggested the language model upgrade to 5.2 may have already fixed it, so they agreed to merge the prompt fix and close it unless the issue recurs. Marcus is also planning to research a shared secret storage solution to centralize API keys currently being passed around, especially for the local office team.

### 6. Marius finishing 6919 and picking up Chargebee subscription work from Jayr

Marius is wrapping up ticket 6919 (just one edge case left to test), after which he'll be free for new work. Adam noticed that nearly everything in Jira is assigned to Jayr and suggested Marius pick up some of his backend tickets to improve velocity. Marius volunteered to take the Chargebee subscription ticket since he has prior experience with subscriptions, and Jayr confirmed he'd already added initial investigation notes on it.

### 7. Marco's completed tickets — onboarding loading states (7036) and thumbnail blur customization (4697)

Marco completed two tickets: 7036 fixed the onboarding flow when users skip AI creation, which previously had no loading states making it look buggy — now shows proper UX feedback. Ticket 4697 addressed thumbnail customization in the feature section where custom thumbnails always had an unwanted blur effect from outdated designs — users now have an option to disable the blur.

### 8. Mihai's updates — 7367 nearly done and internal CLI tool for Mio

Mihai reported ticket 7367 is nearly done (10 more minutes after scrum). He also built an MVP internal CLI tool for interacting with Mio, posted it in a thread for Asim to review — Asim confirmed he saw it and will discuss it Monday as it may tie into something he's working on. Mihai hadn't created a ticket for the CLI tool since it was a self-initiated project, but both Adam and Asim emphasized that any work being done should always be tracked in a ticket — worst case it just gets closed, and the context could be useful for AI or future reference down the road.

### 9. Milan's backlog cleanup and hub UI 2.0 proposal (3710), and Asim's Monday AI Innovation Lab roundtable with written scrum proposal

Milan is cleaning up the old backlog, pulling out tasks important for user experience — including modernizing players to free up mobile real estate where control buttons are cramped. He highlighted hub UI 2.0 (ticket 3710) as the most impactful item: it's old but if prioritized would solve many hub-related edge cases and modernize the hub UI, though it needs further discussion. Asim closed by confirming he'll send an invite for a casual AI Innovation Lab roundtable on Monday around 10 a.m. to kick off the team's AI/gen-dev initiative. Adam proposed doing a written scrum on Monday instead of a live one, so the scrum context from Friday carries over without two back-to-back extended meetings, and Asim agreed.
