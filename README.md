# The Funniest Out-of-Office

[![competition](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf)
[![rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/m1651/makefun-funniest-out-of-office/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf)
[![reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/m1651/makefun-funniest-out-of-office/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf)

> Out until Monday. My inbox is being handled by my houseplant, which got promoted yesterday and has already missed two deadlines.

## How it works

`main.py` holds a single hand-written out-of-office line. Before writing anything it validates the line the same way the competition gate does: 1–140 characters, not only whitespace, a single line, valid UTF-8, no control characters, no trailing whitespace, and no link. If the line fails any check, the program exits non-zero with a clear error and writes nothing. On success it writes the line to `/output/entry.txt` and prints it.

## Run it

```sh
python3 main.py
```

The entry line is printed to stdout and written to `/output/entry.txt`.
