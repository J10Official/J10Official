# Maintaining this profile

The profile intentionally contains an introduction, research, a compact toolkit, contact details, and an unlabelled animation at the end. Project showcases belong in GitHub's native pinned repositories. Do not restore project panels, a Background section, heading subtitles, or a heading for the animation.

Edit README.md for content. Keep unpublished/private work out of the profile. Do not invent relationships between unrelated projects. Keep publication statuses explicit.

The visual identity uses indigo/cyan terminal graphics and matching heading assets. The header SVGs contain typeset text, simple shapes and a blinking cursor. No AI-generated illustrations are used.

assets/arcade-dark.svg was generated on 21 October 2026 from J10Official public contributions. It is an SVG animation, not an interactive game. It does not automatically refresh. To update its activity snapshot manually:

npx --yes pacman-contribution-graph@5.3.1 --game pacman --username J10Official --platform github --gameTheme github-dark --output assets/arcade-dark.svg

Upstream source and attribution: https://github.com/abozanona/pacman-contribution-graph

Native pins are maintained separately in GitHub; changing them does not require README edits.

The lower header pane runs a 66-second SVG animation: a six-second repository listing followed by ten seconds for each of the six approved project descriptions. Commands are typed before their output appears. The initial name reveal runs once; the hovering bot keeps its own animation. Desktop and mobile descriptions are wrapped separately. Repository names and descriptions are embedded in assets/header.svg and assets/header-mobile.svg, so update both assets if the pins or approved descriptions change. After replacing header assets, update their immutable commit URLs in README.md so GitHub displays the new version.
