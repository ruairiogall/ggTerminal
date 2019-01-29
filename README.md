# ggTerminal
Outputs GB &amp; IRE horse races to Terminal

This utility uses data from Sky Sports Racing racecards.

`Pandas` reads in the racecard, cleans it up and uses `tabulate` to print a prettified version to the terminal.

The app will prompt you for a link as such:
`Enter SSR URL `
and it should be supplied with one such as:
`https://www.skysports.com/racing/racecards/newcastle/29-01-2019/873928/watch-sky-sports-racing-sky-415-mares-handicap-hurdle`

![Image of Output](https://user-images.githubusercontent.com/4633232/51897341-753d3680-23a6-11e9-9404-86d37f6af2d8.png)

Currently, this works with rated races only. Support for maidens and novice races is upcoming.
