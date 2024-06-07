# srtass

A simple script that shifts the timecode of subtitle file.  

---
### Usage

To open help menu, type:
```bash
python ./srtass.py --help
```
To shift subtitles forward, type an amount of time, for example:
```bash
python ./srtass.py filename.srt -s 5
```
To shift subtitles backward, type an amount of time in negative, for example:
```bash
python ./srtass.py filename.srt -s -5
```
To shift multiple files, type:
```bash
python ./srtass.py filename1.srt filename2.ass arguments
```
or
```bash
python ./srtass.py folder arguments
```
