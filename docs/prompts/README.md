# Wallpaper prompts

The twelve consolidated regeneration prompts for the current set, numbered in the same order as `backgrounds/`. Each combines the creative scene, composition and light, shared style, approved corrections, reference image and native 4K settings.

| # | Wallpaper | Complete prompt |
| --- | --- | --- |
| 01 | [Rain, Steam and Speed](../../backgrounds/01-rain-steam-speed.png) | [01-rain-steam-speed.txt](01-rain-steam-speed.txt) |
| 02 | [London — Thames](../../backgrounds/02-london-thames.png) | [02-london-thames.txt](02-london-thames.txt) |
| 03 | [Venezia](../../backgrounds/03-venezia.png) | [03-venezia.txt](03-venezia.txt) |
| 04 | [Paris — Boulevard](../../backgrounds/04-paris-boulevard.png) | [04-paris-boulevard.txt](04-paris-boulevard.txt) |
| 05 | [Yokohama](../../backgrounds/05-yokohama.png) | [05-yokohama.txt](05-yokohama.txt) |
| 06 | [Genova](../../backgrounds/06-genova.png) | [06-genova.txt](06-genova.txt) |
| 07 | [Manchester](../../backgrounds/07-manchester.png) | [07-manchester.txt](07-manchester.txt) |
| 08 | [New York — East River](../../backgrounds/08-new-york.png) | [08-new-york.txt](08-new-york.txt) |
| 09 | [Liverpool](../../backgrounds/09-liverpool.png) | [09-liverpool.txt](09-liverpool.txt) |
| 10 | [Steam Station](../../backgrounds/10-steam-station.png) | [10-steam-station.txt](10-steam-station.txt) |
| 11 | [San Francisco](../../backgrounds/11-san-francisco.png) | [11-san-francisco.txt](11-san-francisco.txt) |
| 12 | [Paris — Motorcars](../../backgrounds/12-paris-motorcars.png) | [12-paris-motorcars.txt](12-paris-motorcars.txt) |

## Generation settings

`gpt-image-2` · quality `high` · `3840x2160` · PNG · Image API edit · one approved reference · no prompt augmentation · no post-generation upscaling.

Approved references: `output/imagegen/pre-4k/`. Original API outputs: `output/imagegen/native-4k/`. Earlier correction prompts are archived in `output/imagegen/prompt-history/` and are not part of the current set.

Example, from the repository root (set IMAGE_GEN to the bundled imagegen/scripts/image_gen.py):

```sh
python "$IMAGE_GEN" edit --image output/imagegen/pre-4k/01-rain-steam-speed.png --prompt-file docs/prompts/01-rain-steam-speed.txt --model gpt-image-2 --quality high --size 3840x2160 --output-format png --no-augment --out output/imagegen/native-4k/01-rain-steam-speed.png
```

## Exact API history

The consolidated files are clearer regeneration specifications, not verbatim records of the past requests. Exact prompts used to produce the existing 4K images remain in `output/imagegen/prompt-history/exact-4k-api/`, linked from each prompt and from the manifest. Rejected corrections are not included in the consolidated specifications.
