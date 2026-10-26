---
name: glass-motion
description: Sunil's "Glass Motion" style, learned frame by frame from three Instagram reels by the same creator — Dbc1KrKh2wV (IndiCreative agency, portrait, "Most agencies sell you ads… we build your empire"), DbAZ41xz1E3 (IndiCreative, landscape, "Stop guessing, start dominating") and DanFrE6zIZ0 (a Spotify concept ad in green, landscape, "Music moves fast… feel every beat"). One accent colour per video (yellow/gold, or the brand colour, e.g. Spotify green), voice-over driven, every spoken phrase typed or focus-pulled on screen, keyboard-click and glass-tick sound effects on a music bed. Two worlds that swap on hard flash cuts. The light world is a slowly flowing liquid yellow-to-white gradient with tight black Helvetica/Inter Display type that types on letter by letter with a caret, gold-gradient word fills, squircle black app-icon chips inline in a sentence, dark SaaS stat cards that count up, real website screenshots under a gold magnifier. The dark world is black with a gold under-glow and a thin gold arc, where Apple-style LIQUID GLASS pills (refracting, chromatic-fringed, white rim-lit capsules) grow out of a dot and slide in a row on a camera truck, real ad creatives fan behind them, and a white search-bar pill types a word. Motion is expo/power4 ease-out on everything (fast start, long silky settle, no bounce), motion blur on fast moves, blur-to-sharp focus pulls, and a white-bloom transition that collapses into the next pill. Use it whenever Sunil says "glass motion", "liquid glass", "the yellow agency reel", "the IndiCreative reel", "the Spotify reel", "the Dbc1KrKh2wV / DbAZ41xz1E3 / DanFrE6zIZ0 reel", "the Boardit / BRB / TwoSix / AA.OS / Cloots / Uber reel", "Arpit's reels", or asks for an explainer "with glass buttons like that reel", even if he doesn't name the skill. Builds with HyperFrames.
---

# Glass Motion

Learned 2026-10-26 from three reels by one creator, all in `assets/ref/` with Whisper transcripts:
`Dbc1KrKh2wV.mp4` (1076x1914 portrait, 24.8 s, yellow), `DbAZ41xz1E3.mp4` (1904x1078 landscape, 24.8 s, yellow),
`DanFrE6zIZ0.mp4` (1904x1078 landscape, 11.8 s, Spotify green). All 30 fps, faceless, voice-over + music + SFX.
The system is identical across them; only the accent colour and props change. It works in both portrait and landscape.
Keyframes for reels 2 and 3: `reel2_keyframes.jpg`, `reel3_keyframes.jpg`. Reel 1 details below.
Look at the stills in `assets/ref/` before building: `t5.4.jpg` and `pills_30fps.jpg` (glass pills, frame by frame),
`t8.4.jpg` (search pill), `t1.6.jpg` (inline icon chip), `t13.0.jpg` (screenshot + italic headline), `tr1.jpg`
(bloom-to-pill transition), `tr2.jpg` (table stack + whip), `tr3.jpg` (count-up card + punch-in), `motion.txt`
(per-frame motion energy for the whole reel).

House rules from his other skills still hold: real content only (real screenshots, logos, numbers checked against the
audio), captions are their own file, render at the source fps, no AI images, no bullet-dot chips. Show a beat table
before coding. Note: the glass pills ARE the point of this style, so the "no pill clusters" rule of insta-motion does
not apply here — but they never bounce.

## 1. The two worlds

| | Light world | Dark world |
|---|---|---|
| Background | Liquid gradient: saturated yellow `#FFD000`–`#F9C900` in two opposite corners, cream `#FFF6C8` and white `#FFFFFF` blobs between, plus one soft glossy "fold" streak. It flows slowly the whole time (domain-warped noise or 3–4 big blurred blobs drifting ~20–40 px/s). Never static. | Pure black `#000`, warm gold glow rising from the bottom third (`#E0A000` → `#5A3A00` → black, radial, very soft), one thin gold rim-lit arc (a giant circle's edge) sweeping across. |
| Type | Black `#0A0A0A` | White `#FFFFFF` with a faint glow |
| Props | Dark SaaS cards, squircle icon chips, screenshots, gold magnifier, ghosted 3-D glass shapes (triangles, speech bubbles) blurred in the background | Liquid-glass pills, white search pill, fanned real creatives, data tables |

Alternate worlds every 3–6 s. The switch is a hard cut on a beat (often with a 2-frame white flash) or the bloom
transition below.

## 2. Type

- Primary: **Helvetica Neue / Inter Display**, medium–semibold, tight tracking (`letter-spacing: -0.04em`), sentence case.
  One short line centred, ~60–70 px at 1080 wide for phrases, up to ~180 px for a single hero word ("Growth").
- Emphasis 1 – **gold gradient fill**: the word's fill runs top-to-bottom from near-black `#1A1400` to gold `#C89A00`
  (`background-clip:text`), e.g. "Sell you Ads.", "Nothing", "guesswork.".
- Emphasis 2 – **italic contrast in one line**: regular + italic + bold italic (`This *isn't* ***theory***`), or heavy
  italic + light italic (`***Nothing*** *runs*` / `*in* ***isolation.***`). The two halves sit on opposite sides of a
  picture, top-left and bottom-right.
- **Type-on with caret**: letters appear one per frame-ish (≈ 18–25 chars/s) with a thin `|` caret that stays a beat
  after the last letter, then the line leaves. Words that aren't typed instead focus-pull in (blur 12px → 0, opacity
  0 → 1, 0.35 s, expo-out) and arrive slightly spread, settling tight.
- Exits: the whole line whips sideways with heavy horizontal motion blur, or zooms past camera (hero word scales 1 →
  3 and blurs out), or blurs and fades.
- Accent small caps: a bold yellow `#FFD000` uppercase word on the light world ("CREATIVE") revealed by a white
  light-wipe.

## 3. Liquid-glass pill (the signature)

What the frames show (`t5.4.jpg`, `pills_30fps.jpg`):

1. **Capsule**, height ≈ 0.1 × frame width (≈ 105 px), radius = height/2, label in white Helvetica medium ≈ 0.7 × height.
2. **Body is clear, not frosted**: you see the background through it, but **refracted** – the content is magnified and
   bent toward the rim, strongest in the last ~20 % at each end (a lens), and *mirrored/stretched* at the curved caps.
3. **Chromatic fringe** at the caps: red/yellow/green separation where bright content passes the edge.
4. **Rim**: a crisp 2–3 px white inner stroke, brightest top-left and bottom-right, plus a soft white outer glow
   (≈ 8–14 px, 35 % opacity). A darker inner shadow under the top rim gives thickness.
5. **Tint**: over black it reads as smoky graphite (`rgba(255,255,255,0.06)` fill + top sheen gradient
   `rgba(255,255,255,0.18)` → 0 over the top 45 %).
6. Over a photo, the photo is visible through the pill and warps as the pill moves — this motion is what sells "liquid".

Build in HyperFrames with an SVG filter on a backdrop copy (deterministic, seek-safe):
`references/glass-pill.html` has the working component — `feTurbulence`-free: a radial displacement map
(`feImage` of a capsule-shaped normal map) → `feDisplacementMap` (scale 40–60) on the background layer clipped to the
capsule, run three times with slightly different scales for R, G, B (`feColorMatrix` split + `feBlend screen`) for the
fringe, then rim stroke, sheen and glow on top. Never use CSS `backdrop-filter: blur()` alone — that gives frosted
glass, which is the wrong look.

Variants:
- **Search pill** (`t8.4.jpg`): solid light-grey/white capsule `#E9E9E9` with a thick white rim, black label typed
  with caret, a black circle on the right holding a gold magnifier icon. Pops in as a white bloom (see 5).
- **Inline icon chip** (`t1.6.jpg`): black squircle (radius 22 %) with a glossy diagonal sheen, a gold glyph inside,
  sitting inline between words like a word itself.

## 4. Motion and easing (measured)

From `motion.txt` (frame-difference energy): almost every move spikes in 1–3 frames and then decays smoothly over
0.6–1.3 s. That is an **exponential ease-out**, not ease-in-out.

- Default for entrances, slides, scale-ups, counters: `expo.out` (or `power4.out`), 0.7–1.0 s.
- Camera trucks across a row of pills: `power3.inOut`, 1.2–1.6 s, the row drifts the whole time it's on screen (never
  fully parked); a second, slower drift (`sine.inOut`) keeps going underneath.
- Fast moves get real motion blur (directional blur proportional to velocity, ~20–40 px at peak) — every whip in the
  reel is smeared, never crisp.
- Focus pull on arrival: blur 10–16 px → 0 alongside the move.
- Scale entrances start from a dot/sliver: a pill grows from ~5 % width to full in 0.35 s, slightly overshooting in
  *size of glow* only, not geometry. **No bounce, no spring, no rotation.**
- Counters (`tr3.jpg`): 9 % → 27 % over ~1.2 s, `expo.out`, with a hard punch-in cut (scale ~1.6×) half way so the
  last numbers land big. The card's line chart draws on with the count.
- Background never stops: the liquid gradient flows continuously; in the dark world the gold glow breathes slowly.
- Hard cuts are on beats: 3.33, 8.87, 15.6, 17.6, 20.13 s in the reference — about one every 3–5 s.

## 5. Signature transitions

1. **Bloom → pill** (`tr1.jpg`): a white light bar sweeps up through the frame (2–3 frames), floods to white, then the
   white blob contracts (expo.out, 0.4 s) into a white pill that sharpens into the next word ("Connected").
2. **Whip with blur**: content exits sideways with motion blur while the next line types in.
3. **Stack fly-through** (`tr2.jpg`): stacked data cards rise and scale past camera with vertical motion blur, the
   next scene's text emerging from the blur.
4. **Zoom-through hero word**: "Growth" fills the frame, then scales past camera into the next line.
5. **Light-wipe reveal**: a soft white streak passes across a word, leaving it revealed in yellow.

## 6. Scene vocabulary (from the reference, in order)

1. Hook line types on over the liquid gradient, faint 3-D glass speech bubbles drift behind.
2. "Sell you [icon chip] Ads." – the chip is part of the sentence.
3. Dark stat card ("Conversion Rate 9 % → 27 %, ▲ 12.8 %, mini bar chart, Track/Report pills") with count-up and punch-in.
4. Dark world: glass pills "Ads / Funnels / Websites / Follow-up" in a row, real ad creatives fanned behind, camera
   trucking left; the "Websites" pill becomes a white search pill that types.
5. Bloom → "Connected" pill. Then "Build to work as one." types word by word.
6. Real website screenshot slides across under a gold magnifier, split italic headline around it.
7. Real result screenshots carousel past ("guesswork.").
8. Dark world: "This isn't theory" over a stack of real ads-manager tables, fly-through.
9. Hero word "Growth isn't left to chance" zooms through.
10. "CREATIVE" light-wipe, then the closing lines type with caret: "We don't run your marketing. / We build your empire|".

## 6b. More vocabulary from reels 2 and 3

- **One accent per video**: yellow/gold `#FFD000` for the agency, Spotify green `#1ED760` (glow `#22FF55`) for the
  Spotify ad. The dark world's bottom glow, the active slider fill, the icon discs and the light-world gradient all
  take that one colour. Everything else is black, white and greys.
- **Frosted text pill + hand cursor** (reel 2 "We turn"): a translucent pill wraps the line; a white hand cursor
  presses it and the pill dims/blurs (press state), then the next word comes.
- **Avatar nodes on a glowing line** (reel 2 "Real clients"): accent-coloured user discs with small black name tags
  ride along a thin white glowing curve, entering one by one.
- **Frosted cards on the light world** (reel 2 "Google Ads"): white translucent rounded card with a small accent tag
  pill on top and 3 lines of black body text, the last line fading out; cards slide past in a row.
- **Dark chat / phone UI**: black rounded panel, a message bubble types, accent send button; a phone mockup with the
  client's real site.
- **Stat + screenshot**: big gold number ("600%", "5X") left of a real result screenshot with a light label to the right.
- **CTA**: accent "Book now" pill + black circle "+" button, a white hand cursor clicks it; then the brand wordmark
  types on over the dark world; final word ("Today!") shrinks away.
- **Media player card** (reel 3): dark rounded player with album art, title/artist, accent progress slider with a knob
  that slides, transport icons; the card tilts and whips away with motion blur.
- **Liquid volume pill** (reel 3): a black vertical capsule with a speaker icon stretches taller and fills with the
  accent colour from the bottom like liquid, then the fill floods the whole screen into the brand end card.
- **Word wobble** (reel 3 "rhythm"): one emphasis word's letters ripple on a wave (sine displacement per letter)
  while the rest stays still.
- Light-on-dark text gets a soft white bloom (`text-shadow: 0 0 18px rgba(255,255,255,.45)`).
- Fonts: SF Pro Display / Helvetica Neue look (use **Inter Display** or **SF Pro Display** Medium). Brand ads may use the
  brand's own face for the end card only.

## 6c. Sound design (all three reels)

Measured with `scripts/sfx_scan.py` (onsets vs. visual cuts vs. Whisper word times) and spectrograms
(`reel1_spectrogram.png`, `sfx_typing_and_pills_spectrogram.png`).

- **Music bed**: modern, punchy, beat-driven instrumental — ~96 BPM (reel 1), ~136 BPM (reel 2), ~118 BPM (reel 3).
  Strong sub-bass kick, never ducks hard under the voice; the VO sits on top, compressed and bright.
- **The drop**: music cuts out (sub-bass vanishes) for ~0.5 s right before the world switch, then slams back on the
  hard cut (reel 1: 3.7–4.3 s silence → hit at 4.31 s with the first glass pill). Silence/stop on reel 2's 6.47 s cut too.
- **Keyboard typing clicks**: every type-on with a caret gets real keyboard clicks, one per letter, irregular 80–150 ms
  apart, broadband short transients (reel 1 "Growth isn't left to cha|" 18.6–19.9 s, "We build your empire|" 23.3–24.2 s;
  reel 2 "Dominating|"). This is the most recognisable sound of the style.
- **Glass ticks / sparkle**: bright, short tonal blips (3–8 kHz, 80–130 ms) as each glass pill pops in (reel 1 at
  4.4, 5.1, 6.1, 6.9 s), sometimes a rising chirp for the search pill.
- **Whooshes**: soft airy swish (~150–300 ms, high band, no bass) on whips and camera trucks; a short riser before
  the white bloom transition.
- **UI clicks**: a soft mouse click when the hand cursor presses a button (reel 2 "Book now").
- No booms on every cut, no cartoon sounds. SFX are quiet and tight to the frame they belong to; most of the energy is
  music + voice.

## 6d. More reels by the creator (@arpit_clipsyk), learned 2026-10-26

- `DcxzGXdzf5S_sfx_showcase.mp4` — "365 Vision" SaaS explainer shown as a "final client video.mp4" card over its
  editing timeline, **sound effects only** (no VO, no music). Light ice-blue world (`#3FB6E8` accent, white/sky
  liquid gradient), glass app-icon tiles floating around a word, glass nav bar clicked by a cursor, "In real time"
  glass pill over a real landscape photo, dashboard cards, kanban, heat-map screen, "Automate [Reports]" with pills
  stacking (Reports → Signatures → Invoices) as a cursor clicks, "+ REQUEST VISIT" button click, 365 logo reveal,
  closing line types on. Frames at each sound: `DcxzGXdzf5S_sfx_event_frames.jpg`.
- `DZhrghqTeMR.mp4` — motivational "1% at a time", landscape. Navy world with a **magenta/violet under-glow**, then
  blue. New moves: a whole line **wobbles on a wave** ("Nobody changes overnight"); big typed words leave an **echo
  trail** (3–4 ghost copies offset along the motion); the "1%" glass pill **stretches into a long glass progress bar**
  with a knob that slides; floating glass icon tiles; "Habits.|" typed inside a glass pill over soft bokeh discs;
  **gauge arc counting 47 → 65 %**; white rounded finance card ($50.475) whose line chart draws on.
- `DZerV6QzxuZ.mp4` — "Every day starts with a plan", landscape. Periwinkle/violet `#5B6CFF` light world + black
  world with a violet ribbon. New moves: **glass pills linked by a thin vertical line, added one under another**
  as a checklist ("Wake up early → study → exercise"); giant word "Edit" focus-pulls in; a **dark glass input bar
  that types the sentence and widens with it**; frosted squircle card holding three 3-D icons; letters of "accident."
  warp; a **glowing orb with expanding ripple rings** holding "It's a system.".

So far every reel: one accent colour, light liquid world + dark glow world, glass pills, typing with a caret,
expo-out easing, real UI.

## 6d-2. Batch 2 — eight more client reels (learned 2026-10-26)

All in `assets/ref/batch2/`: each `<id>.mp4` (1904x1078, 30 fps) with `_sheet.jpg` (one tile = 0.5 s, row = 3 s),
`_transcript.json`, `_sfxscan.txt`. Frame-by-frame strips: `strip_*.jpg`. Spectrograms with words: `spec_*.png`.
The creator (Arpit Kaushik) builds them in After Effects; we rebuild the same look in HyperFrames.

| reel | client / product | palette and world |
|---|---|---|
| `DeJWYotBeBi` | BRB Socially (UAE web + AI-visibility agency) | near-white `#F4F8F8`, crimson `#C8102E` accent, light world only |
| `Ded8xK4hAzP` | Boardit (board-meeting SaaS) v1 | cream `#F3E6D3` sky over a wavy violet/pink horizon band; black world with violet glow |
| `DdyWK-qhRYA` | Boardit v2 | cream / lilac / pink blurred-blob mesh; pink-sky landscape photos and a 3-D room render behind the UI |
| `DdOIJrIhoa2` | AA.OS (home-improvement CRM) | pink-white silk with a glossy crimson ribbon fold |
| `Dcfx1cXB23S` | 365 Vision **with VO** (same edit as the SFX showcase) | ice blue `#3FB6E8` on white/sky, real mountain photo |
| `DcNwQoSzIwq` | Uber spec ad | white and light grey only, black type, Uber's own UI; green appears once ("Booking Confirmed!") |
| `DcIjzeezbpP` | Cloots (fashion app) teaser, **music only, no VO** | black with a green corner glow, 3-D iPhone |
| `DbKzlmTTNwR` | TwoSix Creative (clinic marketing) | white with a peach `#F2A766` silk swoosh; black world with a copper ribbon |

### What's new in the design

- **Three background families** (plus photos). Pick one per video:
  1. *Clean white with accent blobs at the edges*: soft blurred accent clouds sit in the corners and breathe. A **giant
     blurred accent smear** sweeps through the frame (6–8 frames) and works as the wipe between lines (BRB).
  2. *Silk ribbon*: one satin fold of the accent colour, lit like fabric, slowly turning. White + accent in the light
     world, black + copper/accent in the dark world (AA.OS, TwoSix). The ribbon is the only decoration.
  3. *Mesh gradient*: 2–3 pastel blobs (cream / lilac / pink) drifting, sometimes with a wavy, slightly pixel-stepped
     horizon band across the lower third (Boardit).
  Photo backdrops: a real landscape, a 3-D room or a pink-sky landscape under the glass UI. On AA.OS the room photo
  starts in a **red-orange duotone / gradient-map grade** and animates to its normal colours.
- **Type is small and calm**. Most lines are ~30–36 px on a 1904 frame (~1.7 % of width), centred in lots of empty
  space. Only one hero word per few seconds goes huge (`shouldn't|`, `Juggle`, `Growth`, `Paying clients.|`).
  Inter / SF Pro Display medium, sentence case, tight tracking. Brand reels sometimes use the client's face
  (Cloots uses a condensed sans, in a light-italic + bold mix around the phone).
- **Accent ink on the newest word** (in almost every reel): each word arrives in the accent colour, a little lighter,
  blurred and offset 4–8 px up, then settles into black within ~0.3 s. So the line reads black with a coloured
  "leading edge" (`It names your competitor.`, `Be the brand people choose.`, `Get in touch`).
- **Mixed weight inside a line**: light italic + bold (`*A* **lead**`, `Fills out / the *form*`,
  `The job **gets** booked *on the* calender`). Two short lines placed either side of a picture.
- **Typing in a selection box** (Boardit v1): the typed text sits in a solid accent selection box (looks like selected
  text) with white letters, sized to the text. The camera **punches in ~2× mid-typing with a blur frame and then pans to
  follow the caret**, so earlier words slide off the left edge.
- **Echo exit**: a line leaves by stuttering into 2–4 offset ghost copies ("Board meeting", "Startttt") then blurs out.
- **Icon replacing a letter**: `Gr⬆wth` (black circle with an up arrow as the "o"), `Pr✕blem` (red circle with an X);
  a megaphone glyph before "AI". Icons drop in on a punch-in.
- **Word – UI chip – word**: a real UI element stands in for a word in the sentence: `One [Booking Confirmed!] Ride.`,
  `Plan your ride [Pick up now ▾] [One way ▾]`. Chips land with a small tilt (≈ -6°) that settles to 0.

### New props and scenes

- **AI chat composer as the hook**: "How can I help, today?" chat box (white card, or dark glass on Boardit), a prompt
  types in with an accent caret, the hand cursor clicks the send arrow, then the answer comes in (avatars of
  competitors, a search dropdown "Recommending you|").
- **Stacking command pills** (TwoSix "Strategy / Content / Meta Ads / CRM / Follow-up", Boardit v2
  "Agendas / Roles / Live polls"): every new pill grows from a small accent blob, arrives **tinted in the accent
  (copper/brown) and blurred, then cools to black (or white glass) in ~0.4 s**. The stack scrolls up one row each time,
  so the newest pill always lands in the same spot, and the parked cursor "clicks" it. Earlier pills drift off the top.
- **Glass pills on a glowing line**: pills sit on a thin white glowing line that runs like a metro map across the
  dark world; the cursor follows the line and the next pill appears further along (Boardit v1 "Agenda → Documents").
- **Floating 3-D icons gather**: isometric glossy document / calendar / people icons drift in from the edges and
  cluster around the line of text (Boardit), or a row of glossy 3-D app icons in the accent (AA.OS) that the cursor
  sweeps across.
- **Glass app tiles over a photo**: Google and ChatGPT icons in a glass tile over a landscape, the second tile slides
  out of the first.
- **Device fan**: phone + tablet mockups with the client's real websites, fanned in perspective, sliding in from the
  right while the headline types on the left with an accent CTA pill under it.
- **Logo carousel**: client logos in white circles, a row sliding left under a hovering cursor (social proof).
- **Real product UI in browser frames**: tilted in 3-D, stacked, panned; zoomed crops where the cursor opens a
  dropdown or toggles a setting; a meeting window, a heat map, a poll card with bars. Always the client's real UI.
- **Chat bubbles on the ribbon**: accent bubble "Hi! We saw your request…" and a light reply bubble.
- **Hand-drawn signatures** scribble on around "The client signs."
- **3-D iPhone** (Cloots): turns from edge-on to face camera, shows the app, the product photo crops out of the
  screen, captions wrap the phone in stacked italic/bold.
- **Dark stat card**: "Website attention 3,888 → 4,637 ▲ +45 %" counts up with a green trend arrow.
- **Highlight bar reveal**: a glowing yellow bar wipes across, leaving the words behind it ("Built by people").
- **Client video tiles**: real talking-head clips fanned behind a glass pill word ("Clinics").
- **Logo reveal**: the icon comes in huge (cropped by the frame), spins/scales down to size, then the wordmark slides
  out from behind it or types on. The tagline types after, word by word with accent ink.
- **CTA**: accent button ("Let's Talk ⌄", "Book now +") clicked by the cursor → turns into a green "Consultation
  Booked!" pill → logo → website URL typed letter by letter in the accent with a caret.
- **World switch on Uber**: the whole background flashes white ↔ light grey on a beat instead of a colour change.

### Pacing

A new idea every ~1–1.5 s, one line + one visual at a time. 25–30 s total for a full SaaS/agency spot; the
music-only teaser is 16 s.

### Sound (measured, see `*_sfxscan.txt` and `spec_*.png`)

- Music bed tempos: 108 (BRB, AA.OS), 112 (Boardit v1), 123 (Boardit v2), 129 (TwoSix, Uber), 136 (365 Vision),
  ~86/172 (Cloots). VO is loud, bright and compressed; music sits well under it but never fully ducks.
- **The drop before a switch is the rule in every reel**: the music thins or stops for 0.2–1.3 s and comes back on the
  cut with a sub boom. Cloots 4.6–5.9 s (bass filtered out, then "Meet cloots"); BRB 4.5–4.8 s gap, then a sub boom
  under the red smear wipe; TwoSix dropouts at 4.4, 8.1, 13.3 and 18.2 s, each right before a world switch.
- **Sub booms** (below 64 Hz, ~0.4–0.6 s) mark the major scene changes, about one every 3–6 s (Boardit v1 at ≈ 5.8,
  12, 14.7, 18.2, 22 s).
- SFX are sparse in VO reels: 8–21 non-voice hits in 26–30 s, so about one every 1.5 s, always on a visual event
  (cursor click, pill pop, whoosh on a wipe, typing on big typed words). Voice and music do most of the work.
- The ending: the music stops or drops for the CTA, then a button click and a bright ping (BRB 24.07 s), and the logo
  lands on a last hit.

## 6e. Sound-effect library (use these)

`assets/sfx/DcxzGXdzf5S/` holds 23 clean 48 kHz stereo WAVs cut from the SFX-only showcase, plus
`00_full_sfx_track.wav` and `INDEX.md` (what each one plays under, with times). Use them first; place each effect to
the frame of its visual event, the way the showcase does:

| visual event | file |
|---|---|
| icons / tiles / pills pop in | `01_icon_pops`, `17_ui_ping` |
| floating glass, sparkle moments | `02_sparkle_shimmer` |
| line changes, gentle move | `03_soft_whoosh_word_swap` |
| typing with a caret | `12_typing_short`, `16_typing_au`, `22_typing_the`, `23_typing_tail_outro` (loop/trim per letter count), `04_type_tick` for a single letter |
| key word lands / world switch | `05_whoosh_impact_connected`, `13_low_thump`, `09_sub_drop` |
| cards land one by one | `06_card_thumps_x4` (split into 4 hits) |
| big pan / screen flies in or out | `07_low_swoosh_pan`, `14_sub_whoosh_heatmap`, `11_bright_swoosh_cards` |
| cursor clicks | `08_mouse_clicks_x3`, `20_click_request_visit` |
| glass pill arrives | `10_glass_pill_whoosh_in` |
| highlight / reveal ping | `15_ping_rise` |
| pills stacking one after another | `18_pill_pop_notes_stack` (rising tonal pops) |
| build-up into the next section | `19_riser_whoosh` |
| logo / end card | `21_logo_boom_reveal` |

These are cut from a mixed reel, so each clip may carry a faint tail of its neighbour. The creator gives the clean
pack away ("Comment SFX"); if Sunil gets it, drop it in `assets/sfx/pack/` and prefer it. For client deliveries, check
he's happy with the licence. `scripts/sfx_events.py <wav>` lists the effects in any SFX-only track.

## 6f. Apple design rules (Sunil's brief, 2026-10-26) — apply to every Glass Motion build

He shared the "Apple website conversion hack" notes and wants them built in. Translated from web pages to video:

1. **Squircles, not rounded rectangles.** Every card, icon tile, button, panel, phone/screen frame and video card uses
   a squircle (continuous-curvature corner: the straight edge eases into the curve). Use
   `references/squircle.js` → `squircle(el, r)` (clip) or `squirclePath(w,h,r)` (for the rim stroke / glow outline,
   drawn as SVG so the glass rim follows the same curve). Default smoothing 0.6, r ≈ 22 % of the short side for tiles,
   24–48 px for cards at 1080 wide. Full **pills stay true capsules** (`border-radius: h/2`). Plain `border-radius` on a
   card is a mistake. Comparison: `assets/ref/squircle_vs_radius.png`.
2. **Tactile "scroll" motion.** On a website, scrolling turns the product in your hand. In video, the playhead is the
   scroll. Every hero object (phone, dashboard, card, product photo) is always moving slightly: a slow 3-D turn
   (rotateY/rotateX 4–12° across the beat, `perspective: 1600px`), a gentle push-in (scale 1 → 1.04), parallax between
   layers (background 0.3×, mid 0.6×, front 1×), and the light sheen sweeping across the glass as it turns. Sections
   hand off like a scroll: the outgoing scene keeps moving up/away while the next one rises in (`power3.inOut`
   for the handoff, `expo.out` for the arrival). Never a static hold. This adds to the expo-out rule in section 4;
   it doesn't replace it.
3. **One idea at a time.** One idea per beat: one line of text and one visual, nothing else on screen. Let it land
   (hold ≥ 0.6 s after it settles), then clear it before the next. Specs and lists are broken into single beats,
   never dumped as a grid at once. When a list must show, build it one item per spoken item (like the stacking pills
   or the checklist pills) and dim the earlier items. The beat table (one row = one idea) is the plan for this.

## 7. Build

Use HyperFrames (read `hyperframes`, `hyperframes-core`, `hyperframes-animation` first). One paused GSAP timeline,
seek-safe. Start from `references/glass-pill.html` for the pill. Render at the source fps; 1080x1920 for reels, or
whatever frame the task gives. Deliver graphics as opaque full-screen MP4 chunks per range unless he asks for alpha.
