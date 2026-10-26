// Glass Motion: Apple-style squircle (continuous-curvature corners) for cards, pills, icon tiles and buttons.
// A plain border-radius corner jumps from straight to curved; a squircle eases into the curve, which reads as premium.
// Usage:  squircle(el, 48)          -> clips el to a squircle with ~48px corners (re-run if el resizes)
//         squirclePath(w, h, r, s)  -> SVG path string, e.g. for the white rim stroke drawn on top of a glass card
// s = smoothing 0..1 (0.6 ≈ iOS icons / Apple site). r is capped at min(w,h)/2, so r = h/2 gives a squircle pill.

function squirclePath(w, h, r, s = 0.6) {
  r = Math.min(r, w / 2, h / 2);
  const p = Math.min((1 + s) * r, w / 2, h / 2); // the curve starts p px from each corner (longer lead-in than a circle)
  const k = 0.5523 + 0.25 * s;                   // control reach; 0.5523 = circular arc, larger = softer shoulder
  const q = p * k;
  return [
    `M ${p} 0 L ${w - p} 0`,
    `C ${w - p + q} 0 ${w} ${p - q} ${w} ${p}`,
    `L ${w} ${h - p}`,
    `C ${w} ${h - p + q} ${w - p + q} ${h} ${w - p} ${h}`,
    `L ${p} ${h}`,
    `C ${p - q} ${h} 0 ${h - p + q} 0 ${h - p}`,
    `L 0 ${p}`,
    `C 0 ${p - q} ${p - q} 0 ${p} 0 Z`,
  ].join(' ');
}

function squircle(el, r, s = 0.6) {
  el.style.borderRadius = '0';
  el.style.clipPath = `path('${squirclePath(el.offsetWidth, el.offsetHeight, r, s)}')`;
  return el;
}

if (typeof module !== 'undefined') module.exports = { squirclePath, squircle };
