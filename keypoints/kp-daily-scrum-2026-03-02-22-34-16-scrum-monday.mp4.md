# Keypoints

**Source:** 2026-03-02 22-34-16 scrum monday_transcribed.txt

### 1. Marius - Jira cleanup and ticket triage

Marius has been going through old Jira tickets to check if they are still relevant, with help from an AI tool to find stale tickets and move them to closed/churned. He is looking for a new task to pick up, otherwise will ensure the node and byte branch is up to date.

### 2. Mihai - Performance fixes and discussion spaces

Mihai completed ticket 7307 (platform-wide performance improvements, now in QA and code reviewed) and ticket 7305 (high priority fix for discussion spaces banner on new/edit post). Notifications work is planned to start this week, pending discussion with Asim since Andrew is out.

### 3. Jayr - Tickets pushed to production and activity side QA

Jayr pushed ticket 7304 to production with minor data cleanup still needed (can be done manually). Ticket 7059 (activity side) is waiting for QA but keeps getting blocked by pre-existing production bugs, so he wants to know if the current state can be pushed. He also sent a proposal to Asim and Andrew on the notifications side and is awaiting feedback.

### 4. Marco - Bug fixes and header edge cases

Marco completed bug fixes and UX/UI improvements on tickets 6211 and 6926 (platform side). He is now working on header edge cases for hub-side customizations (ticket 6880).

### 5. Marcus - Median app migration and white label build service

Marcus spent Friday migrating the remaining Median apps to the in-house build, but some clients have outdated terms of service agreements blocking submission, so he is emailing them individually to resolve it. This week he plans to finish the back-end API connection between membership.io and the white label build service, and will review the plan with Atanas since their last discussion was about a month ago.

### 6. Atanas - Activity log table investigation (700GB)

Atanas investigated the activity log table, the largest table in the MySQL database at 700GB, which has existed since 2019 and is created by the activity log package. The package config supports disabling writes to it, but the open question is whether the data is actively used anywhere. If it can be dropped, it would free up significant storage.
