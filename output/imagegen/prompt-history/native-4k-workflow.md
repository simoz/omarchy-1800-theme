# Native 4K revisions

Each numbered text file is the exact prompt submitted to the OpenAI Image API via the bundled ImageGen CLI. Input images are the approved compositions backed up in `output/imagegen/pre-4k/`, in the same numbered order as `backgrounds/`.

Settings: `gpt-image-2`, quality `high`, size `3840x2160`, PNG, one reference per edit, no prompt augmentation and no post-generation upscaling.

Example (run from the project root; set IMAGE_GEN to the bundled imagegen/scripts/image_gen.py):

```sh
python "$IMAGE_GEN" edit --image output/imagegen/pre-4k/01-rain-steam-speed.png --prompt-file docs/prompts/native-4k/01-rain-steam-speed.txt --model gpt-image-2 --quality high --size 3840x2160 --output-format png --no-augment --out output/imagegen/native-4k/01-rain-steam-speed.png
```

The images are artistic interpretations of nineteenth-century scenes, not documentary historical reconstructions. Preserve the approved compositions and corrections when regenerating. API rendering can introduce small differences.
