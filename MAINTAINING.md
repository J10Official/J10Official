# Maintaining this profile

The profile intentionally contains an introduction, research, a compact toolkit, contact details, and an unlabelled animation at the end. Project showcases belong in GitHub's native pinned repositories. Do not restore project panels, a Background section, heading subtitles, or a heading for the animation.

Edit README.md for content. Keep unpublished/private work out of the profile. Do not invent relationships between unrelated projects. Keep publication statuses explicit.

The visual identity uses indigo/cyan terminal graphics and matching heading assets. The header SVGs contain typeset text, simple shapes and a blinking cursor. No AI-generated illustrations are used.

assets/arcade-dark.svg was generated on 21 October 2026 from J10Official public contributions. It is an SVG animation, not an interactive game. It does not automatically refresh. To update its activity snapshot manually:

npx --yes pacman-contribution-graph@5.3.1 --game pacman --username J10Official --platform github --gameTheme github-dark --output assets/arcade-dark.svg

Upstream source and attribution: https://github.com/abozanona/pacman-contribution-graph

Native pins are maintained separately in GitHub; changing them does not require README edits.

The lower header pane is a continuous scrolling SVG terminal session. It types ls ~/pinned, leaves a fresh prompt below the listing, then chains cd and gh repo view on the same command line for each approved project description. New lines scroll earlier content upward inside the lower pane; each description stays available for about six seconds with an idle prompt beneath it. A final cd ~ && clear makes the approximately 67–68 second loop restart naturally. The upper name reveal runs once and the hovering bot remains independent. Desktop and mobile wrapping are separate. Repository names and descriptions are embedded in assets/header.svg and assets/header-mobile.svg; update both when the approved pins or descriptions change. After replacing header assets, update their immutable commit URLs in README.md so GitHub displays the new version.
