#!/bin/bash

TIMEFMT='%E'; time claude -p "git add .; git commit -m <message>; git push" --dangerously-skip-permissions
