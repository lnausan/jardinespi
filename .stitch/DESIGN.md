# Design System: taller dig
**Project ID:** projects/10609280735535981453

## 1. Visual Theme & Atmosphere
Learnify is a playful educational landing system for a three-session digitalization workshop. The visual language feels bright, approachable, and workshop-oriented: hand-drawn illustration, thick ink outlines, generous white space, and energetic primary colors. The experience should feel practical and creative rather than corporate.

Use an off-white paper background as the dominant surface, with sparse decorative doodles: stars, dots, arcs, checkerboard patches, and oversized cropped curves. Keep the composition airy. Large hero areas can leave substantial empty space, especially on mobile, but should always include one strong visual anchor.

Source screens analyzed:
- `projects/10609280735535981453/screens/06465035b99940e7bf33767d52426319`
- `projects/10609280735535981453/screens/92341ca55b854dc9925a5cab5b264022`
- `projects/10609280735535981453/screens/4d9dd0d2b6614ab9baae21a09caed977`

## 2. Color Palette & Roles
- **Paper Background:** `#F8F8F2` to `#FBFAF4`. Main page canvas. Avoid pure white except inside card buttons.
- **Ink:** `#0B0B0B`. Headlines, body text, card borders, illustration outlines, and navigation.
- **Primary Action Coral:** `#F34B35`. Registration buttons, high-emphasis CTAs, and the red session card.
- **Creative Yellow:** `#F7D11F`. Session 1 cards, star accents, and positive learning energy.
- **Workshop Lavender:** `#B783F2`. Session 2 cards, pencil illustration fills, dots, and checkerboard accents.
- **Digital Teal:** `#08A6B2`. Illustration clothing, star accents, and occasional curved line decoration.
- **Soft Gray Linework:** `#E7E5DD`. Low-contrast background arcs and structural doodle lines.
- **Button Surface:** `#FFFFFF`. Secondary card buttons placed inside colored cards.

Maintain high contrast: text on yellow, lavender, and coral cards should remain black. Coral buttons should use white text. White secondary buttons should use black text.

## 3. Typography Rules
Use **Plus Jakarta Sans** as the primary family across headings, navigation, body copy, labels, and CTAs.

- **Logo:** Bold, compact wordmark treatment. Use black text with the first part or leading accent in coral.
- **Hero H1:** Extra-bold, black, very large, tight but readable line height. On mobile, allow 3 to 4 short lines rather than shrinking aggressively.
- **Section/Card Titles:** Extra-bold black, often split across multiple lines. Favor direct, plain Spanish copy.
- **Body Copy:** Medium-weight black, conversational, and larger than typical paragraph text.
- **Navigation:** Semibold black, simple text links with no containers.
- **Buttons:** Bold labels, centered, with stable height and generous horizontal padding.

Letter spacing should stay neutral. The brand relies on weight, scale, and line breaks, not tracking.

## 4. Component Stylings
**Header**
- Full-width top bar on the paper background.
- Left-aligned `Learnify` logo, centered navigation links, and a right-aligned coral registration button.
- Use a thin black divider line below the header on desktop-style layouts.
- Keep the header flat, not floating.

**Primary Buttons**
- Coral fill (`#F34B35`) with black 2px outline.
- Rounded rectangle shape around 12px radius, matching Stitch theme `ROUND_TWELVE`.
- White bold text.
- Avoid shadows; the black stroke provides definition.

**Secondary Card Buttons**
- White fill with black 2px outline.
- Same rounded rectangle geometry as the primary button.
- Black bold text.
- Used for "Mas detalles" actions inside session cards.

**Session Cards**
- Thick black outline, 2px to 3px.
- Rounded corners around 24px to 28px for large cards.
- Solid playful fills: yellow, lavender, and coral.
- Interior layout should include a large title, short body text, one illustrative icon or set of icons, and a bottom CTA.
- Cards can overlap or sit in staggered positions on mobile. This is part of the expressive identity.

**Illustrations & Icons**
- Hand-drawn black outline style with simple flat fills.
- Preferred motifs: pencil, flying character, palette, pen, color wheel, brain, lightbulb, sketchpad, folder, screen, handshake.
- Icons should feel like classroom doodles: simple, charming, and readable at small sizes.

**Decorative Marks**
- Use stars, dots, arcs, large partial circles, and checkerboard blocks.
- Decorations should sit behind or around content, never compete with headline readability.
- Keep linework mostly black or low-contrast gray, with occasional yellow, lavender, teal, and coral fills.

## 5. Layout Principles
- Start with the usable landing experience, not a marketing wrapper.
- Use large breathing room above and around the hero. The mobile hero can be tall and sparse, with illustration placed to the right or below the headline.
- Desktop session cards work best as a three-column row with equal height and consistent CTAs.
- Mobile session cards can become an expressive collage: two cards side by side near the fold and one wider card below.
- Favor hard-edged contrast and clear hierarchy over soft gradients or glass effects.
- Keep content blocks visually direct: headline, subheadline, illustration, cards, action.
- Preserve the paper-like background and doodle system across all screens so variants still feel like one course brand.

## 6. Stitch Generation Notes
When generating or editing new screens for this project, include:
- Platform: responsive landing page, mobile-first with desktop adaptation.
- Theme: playful educational workshop, hand-drawn doodle illustration, paper background.
- Font: Plus Jakarta Sans.
- Roundness: rounded cards and buttons, approximately `ROUND_TWELVE` for controls and larger radii for cards.
- Palette: off-white background, black ink, coral CTA, yellow/lavender/coral session cards, teal accents.
- Avoid: dark mode, glossy gradients, photographic imagery, soft corporate SaaS cards, thin borders, and muted beige-only palettes.
