# 1800 · Omarchy 4

A pixel art theme for Omarchy inspired by nineteenth-century cities, steam travel and harbors in the mist.

## Backgrounds

Twelve wallpapers, all native 3840 × 2160. Click a preview to open the full-resolution PNG.

| | | |
| --- | --- | --- |
| [![Rain, Steam and Speed](docs/previews/01-rain-steam-speed.jpg)](backgrounds/01-rain-steam-speed.png)<br>Rain, Steam and Speed | [![London — Thames](docs/previews/02-london-thames.jpg)](backgrounds/02-london-thames.png)<br>London — Thames | [![Venezia](docs/previews/03-venezia.jpg)](backgrounds/03-venezia.png)<br>Venezia |
| [![Paris — Boulevard](docs/previews/04-paris-boulevard.jpg)](backgrounds/04-paris-boulevard.png)<br>Paris — Boulevard | [![Yokohama](docs/previews/05-yokohama.jpg)](backgrounds/05-yokohama.png)<br>Yokohama | [![Genova](docs/previews/06-genova.jpg)](backgrounds/06-genova.png)<br>Genova |
| [![Manchester](docs/previews/07-manchester.jpg)](backgrounds/07-manchester.png)<br>Manchester | [![New York — East River](docs/previews/08-new-york.jpg)](backgrounds/08-new-york.png)<br>New York — East River | [![Liverpool](docs/previews/09-liverpool.jpg)](backgrounds/09-liverpool.png)<br>Liverpool |
| [![Steam Station](docs/previews/10-steam-station.jpg)](backgrounds/10-steam-station.png)<br>Steam Station | [![San Francisco](docs/previews/11-san-francisco.jpg)](backgrounds/11-san-francisco.png)<br>San Francisco | [![Paris — Motorcars](docs/previews/12-paris-motorcars.jpg)](backgrounds/12-paris-motorcars.png)<br>Paris — Motorcars |


[Scene prompts and generation settings](docs/prompts/README.md) are included.

## Inspiration

Steam trains, sailing ships, gas lamps and early motorcars connect cities across Europe, Japan and America. Golden daylight and blue nights share the same painterly pixel art style, inspired by Rain, Steam and Speed by Joseph Mallord William Turner.

## Installation

Run on your Omarchy 4 machine:

```sh
omarchy-theme-install https://github.com/simoz/omarchy-1800-theme
```

To switch back, select your previous theme from Omarchy's theme menu.

## Shell

Dark green surfaces, parchment text and brass borders carry through the bar, menus, launcher and dialogs. Selected rows use a muted sage background. Shell surfaces are opaque; personal settings can override them.

## Palette

![1800 palette](docs/palette.svg)

| Role | Color |
| --- | --- |
| Ink background | `#202725` |
| Surfaces | `#2D3631` |
| Parchment text | `#F0E7D4` |
| Brass accent | `#D8B078` |
| Sage selection | `#46554D` |
| Secondary text | `#B5B6A7` |

`colors.toml` contains the theme palette, including bright terminal variants. `icons.theme` selects `Yaru-wartybrown`.

Opaque-color contrast: primary text **12.40:1** on the background; primary text **6.41:1** on selection; secondary text **6.07:1** on lighter surfaces. The eight semantic terminal colors exceed **4.5:1** on the main background. Transparency and application customizations may change these results.

## Compatibility

Uses the Omarchy 4 central palette and `shell.toml`.

## Image credits

Artwork created with OpenAI image generation. Wallpapers are native 3840 × 2160, with no post-generation upscaling. Gallery previews are reduced copies.

## License

See the [MIT License](LICENSE).
