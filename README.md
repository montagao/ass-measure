# @montagao/ass-measure

A Node.js native addon for measuring dimensions of subtitle lines in ASS (Advanced SubStation Alpha) subtitle files.

## Installation

```bash
npm install @montagao/ass-measure
```

## Description

ass-measure is a native Node.js addon that provides functionality to analyze ASS subtitle files and determine the rendered dimensions of each subtitle line. This is useful for video processing applications, subtitle editors, or any situation where you need to know the actual display size of subtitles.

## Features

- Measures width and height of each subtitle line
- Returns timing information (start and end times)
- Handles all standard ASS subtitle features
- Native implementation for performance

## Usage

```javascript
const measureAss = require('ass-measure');

// Parameters:
// 1. Path to the ASS subtitle file
// 2. Video width in pixels
// 3. Video height in pixels
const subtitleInfo = measureAss('./path/to/subtitles.ass', 1920, 1080);

// Result is an array of subtitle line objects
subtitleInfo.forEach(line => {
  console.log(`Line: "${line.text}"`);
  console.log(`Dimensions: ${line.width}x${line.height} pixels`);
  console.log(`Timing: ${line.startTime} - ${line.endTime}`);
});
```

## CLI Usage Example

You can also use this package directly from the command line:

```bash
node -e "console.log(require('@montagao/ass-measure')('example.ass', 1920, 1080));"
```

Example output:

```
[ass] libass API version: 0x1703000
[ass] libass source: tarball: 0.17.3
[ass] Shaper: FriBidi 1.0.15 (SIMPLE) HarfBuzz-ng 10.0.1 (COMPLEX)
[ass] Using font provider coretext
[ass] Added subtitle file: 'example.ass' (2 styles, 3 events)
[ass] fontselect: (Arial, 400, 0) -> /System/Library/Fonts/Supplemental/Arial.ttf, -1, ArialMT
[
  {
    text: 'This is a test subtitle line 1',
    width: 518,
    height: 51,
    startTime: 1000,
    endTime: 5000
  },
  {
    text: 'This is a test subtitle line 2 with some more text',
    width: 922,
    height: 51,
    startTime: 6000,
    endTime: 10000
  },
  {
    text: 'This is a longer test subtitle line 3 with even more text to check dimensions',
    width: 1434,
    height: 52,
    startTime: 11000,
    endTime: 20000
  }
]
```

## Return Value

The function returns an array of objects with the following properties for each subtitle line:

- `text` - The text content of the subtitle line
- `width` - The width of the rendered subtitle in pixels
- `height` - The height of the rendered subtitle in pixels
- `startTime` - The start time of the subtitle in milliseconds
- `endTime` - The end time of the subtitle in milliseconds

## Requirements

- Node.js 14.x or higher
- C++ compiler compatible with your platform

## Building from Source

If you want to build from source, you'll need:

1. Node.js and npm installed
2. node-gyp installed globally (`npm install -g node-gyp`)
3. C++ build tools for your platform:
   - Windows: Visual Studio Build Tools
   - macOS: Xcode Command Line Tools
   - Linux: GCC and related build tools

Then run:

```bash
git clone https://github.com/montagao/ass-measure.git
cd ass-measure
npm install
```

## License

MIT

## Author

Monta Gao 