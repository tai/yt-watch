#!/usr/bin/env python3

import json
import sys

HEAD = """
<html>
<head>
<title>Open Source Summit Japan 2023 Live Streams</title>
<style>
html, body {
  height: 100%;
}

body {
  display: flex;
  flex-direction: column;
}

.schedule {
  width: 100%;
  height: 1000px;
  overflow-y: scroll;
}

.item-container {
  width: 100%;
  height: 1000px;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  overflow-y: scroll;
}

.item {
  padding: 10px;
  border: 1px solid #fff;
}
</style>
</head>
<body>

<div class="item-container">
"""

TAIL = """
</div><!-- /item-container -->

<iframe class="schedule" src="https://events.linuxfoundation.org/open-source-summit-japan/program/schedule/"></iframe>

</body>
</html>
"""

def gen(file):
  vids = json.load(open(file))
  vids = [v for v in vids if 'OSS Japan 2023' in v['title']]

  print(HEAD)
  for v in vids:
    url = "https://www.youtube.com/embed/" + v['videoId']
    title = v['title']

    vid = f"""
<div class="item">
{title}<br/>
<iframe width="380" height="200" src="{url}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>
"""
    print(vid)
  print(TAIL)

if len(sys.argv) < 2:
  print("Usage: yt-watchgen <json>", file=sys.stderr)
  sys.exit(0)
gen(sys.argv[1])
