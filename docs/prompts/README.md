# Native 4K wallpaper generation

Approved workflow: OpenAI Image API, `gpt-image-2`, `high`, PNG, native `3840x2160`.

The first native API request returned HTTP 429 `credit_balance_exhausted`. No accepted 4K wallpaper has been produced. The two earlier integrated-tool trials were 1672 × 941 and are excluded.

Each text file records the exact prompt. The original paintings and source URLs are listed in `../backgrounds.json`. Input 1 is the corresponding original painting; input 2 is the detail/style reference [Outpost alpine](https://github.com/simoz/omarchy-outpost-theme/blob/main/backgrounds/09-alpine.png).

Use the bundled ImageGen CLI in an environment with `openai`, `pillow` and `OPENAI_API_KEY`. Example:

```sh
python "$IMAGE_GEN" edit --image "$PAINTING_REFERENCE" --image "$OUTPOST_REFERENCE" --prompt-file docs/prompts/02-wanderer.txt --model gpt-image-2 --quality high --size 3840x2160 --output-format png --no-augment --out output/imagegen/02-wanderer.png
```

Inspect every result at full resolution, verify dimensions and absence of lettering, then copy accepted PNGs unchanged into `backgrounds/`. Generate small gallery previews separately. Record checksums and actual dimensions in the manifest. Never label an upscaled draft as native 4K.
