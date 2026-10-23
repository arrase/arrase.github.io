from html import escape
from pathlib import Path
from textwrap import wrap
import yaml

ROOT_DIR = Path(__file__).resolve().parent
PROJECTS_FILE = ROOT_DIR / "projects.yml"
INDEX_FILE = ROOT_DIR / "docs" / "index.md"
README_FILE = ROOT_DIR / "README.md"
ASSETS_DIR = ROOT_DIR / "assets"

THEMES = {
    "dark": {
        "bg_canvas": "#090a0f",
        "bg_surface": "#11131a",
        "border": "#222634",
        "divider": "#1c202c",
        "text_main": "#f4f4f6",
        "text_muted": "#9499ad",
        "accent_primary": "#818cf8",
        "accent_secondary": "#38bdf8",
        "icon_bg": "rgba(129, 140, 248, 0.12)",
        "icon_border": "rgba(129, 140, 248, 0.24)",
        "tag_bg": "rgba(129, 140, 248, 0.08)",
        "tag_border": "#222634",
        "badge_bg": "rgba(129, 140, 248, 0.06)",
    },
    "light": {
        "bg_canvas": "#fafafa",
        "bg_surface": "#ffffff",
        "border": "#e4e4e7",
        "divider": "#f0f0f3",
        "text_main": "#18181b",
        "text_muted": "#52525b",
        "accent_primary": "#4f46e5",
        "accent_secondary": "#0284c7",
        "icon_bg": "rgba(79, 70, 229, 0.08)",
        "icon_border": "rgba(79, 70, 229, 0.20)",
        "tag_bg": "rgba(79, 70, 229, 0.06)",
        "tag_border": "#e4e4e7",
        "badge_bg": "rgba(79, 70, 229, 0.04)",
    },
}

ICON_PATHS = {
    "fas fa-microchip": (
        '<rect x="6" y="6" width="12" height="12" rx="2" fill="none" stroke="{c}" stroke-width="1.8"/>'
        '<rect x="9" y="9" width="6" height="6" rx="1" fill="none" stroke="{c}" stroke-width="1.5"/>'
        '<path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4" stroke="{c}" stroke-width="1.8" stroke-linecap="round"/>'
    ),
    "fas fa-robot": (
        '<rect x="4" y="8" width="16" height="12" rx="3" fill="none" stroke="{c}" stroke-width="1.8"/>'
        '<path d="M12 4v4M9 4h6M2 13h2M20 13h2" stroke="{c}" stroke-width="1.8" stroke-linecap="round"/>'
        '<circle cx="9" cy="14" r="1.4" fill="{c}"/><circle cx="15" cy="14" r="1.4" fill="{c}"/>'
    ),
    "fas fa-file-code": (
        '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" fill="none" stroke="{c}" stroke-width="1.8" stroke-linejoin="round"/>'
        '<path d="M14 2v6h6M10 13l-2 2 2 2M14 13l2 2-2 2" fill="none" stroke="{c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
    ),
    "fas fa-users-gear": (
        '<circle cx="9" cy="8" r="3.5" fill="none" stroke="{c}" stroke-width="1.8"/>'
        '<path d="M3 19c0-3 2.7-5.5 6-5.5s6 2.5 6 5.5" fill="none" stroke="{c}" stroke-width="1.8" stroke-linecap="round"/>'
        '<circle cx="17.5" cy="9.5" r="2.5" fill="none" stroke="{c}" stroke-width="1.6"/>'
        '<path d="M15.5 14c2.5.4 4.5 2.2 4.5 4.8" fill="none" stroke="{c}" stroke-width="1.6" stroke-linecap="round"/>'
    ),
    "fas fa-note-sticky": (
        '<path d="M15.5 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V8.5L15.5 3Z" fill="none" stroke="{c}" stroke-width="1.8" stroke-linejoin="round"/>'
        '<path d="M15 3v6h6M8 13h8M8 17h5" fill="none" stroke="{c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
    ),
    "fas fa-magnifying-glass-chart": (
        '<circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="{c}" stroke-width="1.8"/>'
        '<path d="M15.5 15.5L21 21M8 12v-2M10.5 12V8M13 12v-3" fill="none" stroke="{c}" stroke-width="1.8" stroke-linecap="round"/>'
    ),
    "fab fa-github": (
        '<path d="M15 21v-3.5c0-1 .1-1.4-.5-2 2.8-.3 5.5-1.4 5.5-6a4.6 4.6 0 0 0-1.3-3.2 4.2 4.2 0 0 0-.1-3.2s-1.1-.3-3.5 1.3a12.3 12.3 0 0 0-6.2 0C6.5 2.8 5.4 3.1 5.4 3.1a4.2 4.2 0 0 0-.1 3.2A4.6 4.6 0 0 0 4 9.5c0 4.6 2.7 5.7 5.5 6-.6.6-.6 1.2-.5 2V21" fill="none" stroke="{c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
        '<path d="M9 18c-4.5 1.5-5-2.5-7-3" fill="none" stroke="{c}" stroke-width="1.8" stroke-linecap="round"/>'
    ),
    "fas fa-map-location-dot": (
        '<path d="M12 21s-6-5.3-6-10a6 6 0 1 1 12 0c0 4.7-6 10-6 10Z" fill="none" stroke="{c}" stroke-width="1.8" stroke-linejoin="round"/>'
        '<circle cx="12" cy="11" r="2.2" fill="{c}"/>'
    ),
    "fas fa-circle-dot": (
        '<circle cx="12" cy="12" r="8" fill="none" stroke="{c}" stroke-width="1.8"/>'
        '<ellipse cx="12" cy="12" rx="10" ry="3.5" transform="rotate(-20 12 12)" fill="none" stroke="{c}" stroke-width="1.5"/>'
        '<circle cx="12" cy="12" r="2.5" fill="{c}"/>'
    ),
    "fas fa-atom": (
        '<circle cx="12" cy="12" r="2" fill="{c}"/>'
        '<ellipse cx="12" cy="12" rx="9" ry="3.8" transform="rotate(30 12 12)" fill="none" stroke="{c}" stroke-width="1.6"/>'
        '<ellipse cx="12" cy="12" rx="9" ry="3.8" transform="rotate(-30 12 12)" fill="none" stroke="{c}" stroke-width="1.6"/>'
    ),
}


def render_mkdocs_card(project: dict) -> str:
    tags = "\n".join(
        f'      <span class="card-tag">{escape(tag)}</span>'
        for tag in project["tags"]
    )
    return (
        f'  <a href="{project["url"]}" class="feature-card">\n'
        f"    <div>\n"
        f'      <div class="card-top">\n'
        f'        <i class="{project["icon"]} feature-icon" aria-hidden="true"></i>\n'
        f'        <span class="card-badge">{escape(project["badge"])}</span>\n'
        f"      </div>\n"
        f'      <h3>{escape(project["name"])}</h3>\n'
        f'      <p>{escape(project["description"])}</p>\n'
        f"    </div>\n"
        f'    <div class="card-tags">\n'
        f"{tags}\n"
        f"    </div>\n"
        f"  </a>"
    )


def render_mkdocs_index(data: dict) -> str:
    hero = data["hero"]
    blocks = [
        "---\n"
        "hide:\n"
        "  - navigation\n"
        "  - toc\n"
        "---\n\n"
        '<div class="hero-section">\n'
        '  <div class="hero-eyebrow">\n'
        f'    <i class="{hero["eyebrow_icon"]}" aria-hidden="true"></i>\n'
        f'    <span>{escape(hero["eyebrow"])}</span>\n'
        "  </div>\n"
        f'  <h1>{escape(hero["title"])}</h1>\n'
        '  <p class="hero-subtitle">\n'
        f'    {escape(hero["subtitle"])}\n'
        "  </p>\n"
        "</div>"
    ]

    for section in data["sections"]:
        cards = "\n\n".join(
            render_mkdocs_card(project) for project in section["projects"]
        )
        blocks.append(
            '<div class="section-header">\n'
            f'  <h2>{escape(section["title"])}</h2>\n'
            f'  <span>{escape(section["subtitle"])}</span>\n'
            "</div>\n\n"
            '<div class="projects-grid">\n\n'
            f"{cards}\n\n"
            "</div>"
        )

    return "\n\n".join(blocks) + "\n"


def render_section_svg(section: dict, theme: dict) -> str:
    title = escape(section["title"])
    subtitle = escape(section["subtitle"])
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 896 36" width="896" height="36">\n'
        f'  <text x="2" y="21" fill="{theme["text_main"]}" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', Inter, sans-serif" font-size="15" font-weight="600" letter-spacing="-0.2">{title}</text>\n'
        f'  <text x="894" y="21" text-anchor="end" fill="{theme["text_muted"]}" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', Inter, sans-serif" font-size="12">{subtitle}</text>\n'
        f'  <line x1="0" y1="32" x2="896" y2="32" stroke="{theme["border"]}" stroke-width="1"/>\n'
        "</svg>\n"
    )


def render_card_svg(project: dict, theme: dict) -> str:
    icon_svg = ICON_PATHS[project["icon"]].format(c=theme["accent_primary"])
    badge = "Repo →"
    badge_w = int(len(badge) * 6.5 + 18)
    badge_x = 442 - badge_w
    badge_text_x = badge_x + badge_w / 2

    lines = wrap(project["description"], width=72)[:3]
    desc_nodes = "\n".join(
        f'  <text x="18" y="{63 + idx * 17.5}" fill="{theme["text_muted"]}" '
        f'font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', Inter, sans-serif" font-size="12.5">{escape(line)}</text>'
        for idx, line in enumerate(lines)
    )

    tag_nodes = []
    tx = 18
    for tag in project["tags"]:
        tw = int(len(tag) * 6.6 + 16)
        tag_nodes.append(
            f'  <rect x="{tx}" y="124" width="{tw}" height="20" rx="4" fill="{theme["tag_bg"]}" stroke="{theme["tag_border"]}" stroke-width="1"/>\n'
            f'  <text x="{tx + tw / 2}" y="137.5" text-anchor="middle" fill="{theme["text_muted"]}" '
            f'font-family="ui-monospace, SFMono-Regular, \'JetBrains Mono\', Menlo, Consolas, monospace" font-size="10.5">{escape(tag)}</text>'
        )
        tx += tw + 6
    tags_svg = "\n".join(tag_nodes)

    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 156" width="460" height="156">\n'
        "  <defs>\n"
        '    <linearGradient id="cardLine" x1="0%" y1="0%" x2="100%" y2="0%">\n'
        f'      <stop offset="0%" stop-color="{theme["bg_surface"]}" stop-opacity="0"/>\n'
        f'      <stop offset="50%" stop-color="{theme["accent_primary"]}" stop-opacity="0.45"/>\n'
        f'      <stop offset="100%" stop-color="{theme["bg_surface"]}" stop-opacity="0"/>\n'
        "    </linearGradient>\n"
        "  </defs>\n"
        f'  <rect x="1" y="1" width="458" height="154" rx="10" fill="{theme["bg_surface"]}" stroke="{theme["border"]}" stroke-width="1"/>\n'
        '  <rect x="40" y="1" width="380" height="1" fill="url(#cardLine)"/>\n'
        f'  <rect x="18" y="14" width="28" height="28" rx="7" fill="{theme["icon_bg"]}" stroke="{theme["icon_border"]}" stroke-width="1"/>\n'
        f'  <g transform="translate(23, 19) scale(0.75)">{icon_svg}</g>\n'
        f'  <text x="56" y="33.5" fill="{theme["text_main"]}" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', Inter, sans-serif" font-size="15.5" font-weight="650" letter-spacing="-0.2">{escape(project["name"])}</text>\n'
        f'  <rect x="{badge_x}" y="17" width="{badge_w}" height="21" rx="10.5" fill="{theme["badge_bg"]}" stroke="{theme["border"]}" stroke-width="1"/>\n'
        f'  <text x="{badge_text_x}" y="31" text-anchor="middle" fill="{theme["text_muted"]}" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', Inter, sans-serif" font-size="10.5" font-weight="500">{escape(badge)}</text>\n'
        f"{desc_nodes}\n"
        f'  <line x1="18" y1="114" x2="442" y2="114" stroke="{theme["divider"]}" stroke-width="1"/>\n'
        f"{tags_svg}\n"
        "</svg>\n"
    )


def picture_tag(slug: str, width: str, alt: str) -> str:
    return (
        "<picture>"
        f'<source media="(prefers-color-scheme: dark)" srcset="assets/{slug}-dark.svg">'
        f'<source media="(prefers-color-scheme: light)" srcset="assets/{slug}-light.svg">'
        f'<img alt="{escape(alt)}" src="assets/{slug}-dark.svg" width="{width}">'
        "</picture>"
    )


def generate_profile_assets_and_readme(data: dict) -> str:
    ASSETS_DIR.mkdir(exist_ok=True)
    github_url = data["github_url"]
    blocks = []

    for sec_idx, section in enumerate(data["sections"]):
        sec_slug = f"section-{sec_idx}"
        for mode, theme in THEMES.items():
            (ASSETS_DIR / f"{sec_slug}-{mode}.svg").write_text(
                render_section_svg(section, theme), encoding="utf-8"
            )
        blocks.append(f'<p align="center">{picture_tag(sec_slug, "100%", section["title"])}</p>')

        projects = section["projects"]
        rows = []
        for i in range(0, len(projects), 2):
            row_items = []
            for project in projects[i : i + 2]:
                slug = f"card-{project['repo'].lower()}"
                for mode, theme in THEMES.items():
                    (ASSETS_DIR / f"{slug}-{mode}.svg").write_text(
                        render_card_svg(project, theme), encoding="utf-8"
                    )
                repo_url = f"{github_url}/{project['repo']}"
                row_items.append(
                    f'<a href="{repo_url}">{picture_tag(slug, "49%", project["name"])}</a>'
                )
            rows.append('<p align="center">\n  ' + "\n  ".join(row_items) + "\n</p>")
        blocks.append("\n".join(rows))

    return "\n\n".join(blocks) + "\n"


def main() -> None:
    data = yaml.safe_load(PROJECTS_FILE.read_text(encoding="utf-8"))
    INDEX_FILE.write_text(render_mkdocs_index(data), encoding="utf-8")
    README_FILE.write_text(generate_profile_assets_and_readme(data), encoding="utf-8")


if __name__ == "__main__":
    main()
