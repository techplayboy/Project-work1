"""
drawkit — matplotlib primitives for Project Lumière task images.

Black-on-white schematic style; every helper takes an explicit zorder so white-filled
patches never hide lines by accident. Import from a task's draw script:

    import sys; sys.path.insert(0, ".claude/skills/lumiere-task/scripts")
    from drawkit import *
    fig, ax = new_canvas(14, 10)
    line(ax, [(0, 0), (5, 0)])
    hop(ax, (2, -1), (2, 1), cross_at=0)   # vertical wire hopping over the horizontal one
    dot(ax, 4, 0)                           # real junction
    save_png(fig, ax, "image.png", xlim=(-1, 6), ylim=(-2, 2))

Z-order convention:  lines 3 | white patches 4 | symbols inside patches 6 | dots/arrows 8 | text 9
"""
import math

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, Polygon, Rectangle
from PIL import Image

LW = 1.8
EDGE = "black"
FS = 16

__all__ = [
    "LW", "EDGE", "FS", "new_canvas", "line", "box", "circle", "dot", "txt", "arrow",
    "hop", "ground_hatch", "spring", "tank", "zigzag_resistor", "save_png", "check_png",
    "check_text_overlaps", "save_tiles",
]


def new_canvas(w=14.0, h=10.0, dpi=200):
    fig, ax = plt.subplots(figsize=(w, h), dpi=dpi)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    return fig, ax


def line(ax, pts, lw=LW, z=3, ls="-"):
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=EDGE, lw=lw, ls=ls, solid_capstyle="round", zorder=z)


def box(ax, x, y, w, h, lw=LW, z=4, fill="white"):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=fill, edgecolor=EDGE, lw=lw, zorder=z))


def circle(ax, x, y, r, lw=LW, z=4, fill="white"):
    ax.add_patch(Circle((x, y), r, facecolor=fill, edgecolor=EDGE, lw=lw, zorder=z))


def dot(ax, x, y, ms=6.5):
    """Junction dot: the ONLY way two lines are drawn as connected."""
    ax.plot([x], [y], marker="o", ms=ms, color=EDGE, zorder=8)


def txt(ax, x, y, s, ha="center", va="center", fs=FS, **kw):
    ax.text(x, y, s, ha=ha, va=va, fontsize=fs, color=EDGE, zorder=9, **kw)


def arrow(ax, x, y, dx, dy, lw=LW, scale=15):
    ax.annotate("", xy=(x + dx, y + dy), xytext=(x, y),
                arrowprops=dict(arrowstyle="-|>", lw=lw, color=EDGE, mutation_scale=scale),
                zorder=8)


def hop(ax, p0, p1, cross_at, r=0.18, lw=LW, z=3):
    """Straight horizontal or vertical wire p0->p1 that hops (semicircle) over a
    perpendicular line at coordinate `cross_at` (y for a vertical wire, x for a
    horizontal one). A hop means NOT connected."""
    (x0, y0), (x1, y1) = p0, p1
    if abs(x0 - x1) < 1e-9:      # vertical wire, crossing a horizontal line at y=cross_at
        s = 1 if y1 > y0 else -1
        line(ax, [(x0, y0), (x0, cross_at - s * r)], lw=lw, z=z)
        line(ax, [(x0, cross_at + s * r), (x1, y1)], lw=lw, z=z)
        ax.add_patch(Arc((x0, cross_at), 2 * r, 2 * r, theta1=-90, theta2=90,
                         color=EDGE, lw=lw, zorder=z))
    elif abs(y0 - y1) < 1e-9:    # horizontal wire, crossing a vertical line at x=cross_at
        s = 1 if x1 > x0 else -1
        line(ax, [(x0, y0), (cross_at - s * r, y0)], lw=lw, z=z)
        line(ax, [(cross_at + s * r, y0), (x1, y1)], lw=lw, z=z)
        ax.add_patch(Arc((cross_at, y0), 2 * r, 2 * r, theta1=0, theta2=180,
                         color=EDGE, lw=lw, zorder=z))
    else:
        raise ValueError("hop() needs a horizontal or vertical segment")


def ground_hatch(ax, x, y, w, h, z=2, hatch="///"):
    """Hatched block = stationary housing / ground. Outline plus diagonal hatching."""
    ax.add_patch(Rectangle((x, y), w, h, facecolor="white", edgecolor=EDGE, lw=LW,
                           hatch=hatch, zorder=z))


def spring(ax, x0, y0, x1, n=6, amp=0.20, lw=1.4):
    pts, dx = [(x0, y0)], (x1 - x0) / (n + 1)
    for i in range(n):
        pts.append((x0 + dx * (i + 1), y0 + (amp if i % 2 == 0 else -amp)))
    pts.append((x1, y0))
    line(ax, pts, lw=lw)


def zigzag_resistor(ax, p0, p1, n=6, amp=0.15, lead=0.25, lw=LW):
    """Resistor zigzag between two points (any orientation)."""
    (x0, y0), (x1, y1) = p0, p1
    L = math.hypot(x1 - x0, y1 - y0)
    ux, uy = (x1 - x0) / L, (y1 - y0) / L
    nx, ny = -uy, ux
    a = (x0 + ux * lead, y0 + uy * lead)
    b = (x1 - ux * lead, y1 - uy * lead)
    seg = (L - 2 * lead) / (n + 1)
    pts = [p0, a]
    for i in range(n):
        s = amp if i % 2 == 0 else -amp
        pts.append((a[0] + ux * seg * (i + 1) + nx * s, a[1] + uy * seg * (i + 1) + ny * s))
    pts += [b, p1]
    line(ax, pts, lw=lw)


def tank(ax, x, y, w=1.05):
    line(ax, [(x - w / 2, y), (x + w / 2, y)])
    line(ax, [(x - w / 2 + 0.17, y - 0.18), (x + w / 2 - 0.17, y - 0.18)], lw=1.4)


def check_text_overlaps(fig, ax, shrink_px=2.0):
    """Return WARN strings for every non-empty text whose box touches a drawn line or patch
    outline (labels sitting on a rope/wire/edge make the topology ambiguous)."""
    from matplotlib.transforms import Bbox
    fig.canvas.draw()
    rend = fig.canvas.get_renderer()
    shapes = [("line", l, l.get_transform().transform_path(l.get_path())) for l in ax.lines]
    shapes += [("patch", p_, p_.get_transform().transform_path(p_.get_path())) for p_ in ax.patches]
    out = []
    for t in ax.texts:
        if not t.get_text().strip() or not t.get_visible():
            continue
        bb = t.get_window_extent(rend)
        bb = Bbox.from_extents(bb.x0 + shrink_px, bb.y0 + shrink_px, bb.x1 - shrink_px, bb.y1 - shrink_px)
        hits = [kind for kind, _, path in shapes if path.intersects_bbox(bb, filled=False)]
        if hits:
            x, y = t.get_position()
            out.append(f"WARN text {t.get_text()!r} at ({x:.2f}, {y:.2f}) overlaps {len(hits)} "
                       f"drawn element(s) ({', '.join(sorted(set(hits)))})")
    return out


def save_tiles(path, outdir, cols=3, rows=3, overlap=0.08):
    """Save overlapping zoom tiles of a PNG for close visual inspection (Read each tile)."""
    from pathlib import Path as _P
    im = Image.open(path)
    w, h = im.size
    outdir = _P(outdir); outdir.mkdir(parents=True, exist_ok=True)
    stem = _P(path).stem
    files = []
    for r in range(rows):
        for c in range(cols):
            x0 = max(0, int((c / cols - overlap) * w)); x1 = min(w, int(((c + 1) / cols + overlap) * w))
            y0 = max(0, int((r / rows - overlap) * h)); y1 = min(h, int(((r + 1) / rows + overlap) * h))
            f = outdir / f"{stem}_tile_r{r}c{c}.png"
            im.crop((x0, y0, x1, y1)).save(f)
            files.append(str(f))
    return files


def save_png(fig, ax, path, xlim=None, ylim=None, equal=True, pad=0.20, dpi=200, tiles_dir=None):
    """Save opaque-white RGB PNG at native resolution, run the overlap and PNG checks, and
    (if tiles_dir is given) write zoom tiles that MUST be inspected before handover."""
    if xlim:
        ax.set_xlim(*xlim)
    if ylim:
        ax.set_ylim(*ylim)
    if equal:
        ax.set_aspect("equal")
    ax.axis("off")
    overlaps = check_text_overlaps(fig, ax)
    fig.savefig(path, dpi=dpi, facecolor="white", bbox_inches="tight", pad_inches=pad)
    plt.close(fig)
    Image.open(path).convert("RGB").save(path)
    for msg in overlaps + check_png(path):
        print(msg)
    if tiles_dir:
        tiles = save_tiles(path, tiles_dir)
        print(f"inspect {len(tiles)} zoom tiles in {tiles_dir}")
    print(f"saved {path}")


def check_png(path):
    """Return a list of WARN/ERROR strings for platform image rules."""
    out = []
    im = Image.open(path)
    if im.format not in ("PNG", "JPEG"):
        out.append(f"ERROR image format {im.format} (PNG or JPEG only)")
    if im.mode != "RGB":
        out.append(f"ERROR image mode {im.mode} (save as RGB, no alpha)")
    rgb = im.convert("RGB")
    w, h = rgb.size
    corners = [rgb.getpixel(p) for p in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]]
    if any(min(c) < 245 for c in corners):
        out.append(f"ERROR background not white at corners: {corners}")
    if min(w, h) < 800:
        out.append(f"WARN low resolution {w}x{h}")
    return out
