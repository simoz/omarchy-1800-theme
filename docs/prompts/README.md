# Native 4K wallpaper generation

Approved workflow: OpenAI Image API, `gpt-image-2`, `high`, PNG, native `3840x2160`.

All twelve accepted wallpapers were generated using the API at native 3840 × 2160, checked visually and copied unchanged into the repository. Two earlier 1672 × 941 integrated-tool experiments are excluded. Checksums and actual dimensions are recorded in the manifest.

Each text file records the exact prompt. The original paintings and source URLs are listed in `../backgrounds.json`. Input 1 is the corresponding original painting; input 2 is the detail/style reference [Outpost alpine](https://github.com/simoz/omarchy-outpost-theme/blob/main/backgrounds/09-alpine.png).

Use the bundled ImageGen CLI in an environment with `openai`, `pillow` and `OPENAI_API_KEY`. Example:

```sh
python "$IMAGE_GEN" edit --image "$PAINTING_REFERENCE" --image "$OUTPOST_REFERENCE" --prompt-file docs/prompts/02-wanderer.txt --model gpt-image-2 --quality high --size 3840x2160 --output-format png --no-augment --out output/imagegen/02-wanderer.png
```

Inspect every result at full resolution, verify dimensions and absence of lettering, then copy accepted PNGs unchanged into `backgrounds/`. Generate small gallery previews separately. Record checksums and actual dimensions in the manifest. Never label an upscaled draft as native 4K.
