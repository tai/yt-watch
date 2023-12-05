#!/usr/bin/env python3

import json
import sys

HEAD = """
<html>
<head>
<title>Open Source Summit Japan 2023 Live Streams</title>
<style>
html, body {
  width: 100%;
  height: 100%;
  overflow: hidden;
  margin: 0;
}

body {
  display: flex;
  flex-direction: column;
}

#schedule {
  width: 100%;
  height: 50vh;
  overflow-y: scroll;
}

#item-container {
  width: 100%;
  height: 50vh;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(390px, 1fr));
  overflow-y: scroll;
}

.item {
  padding: 10px;
  border: 1px solid #fff;
}

.item-video {
  width: 380px;
  height: 200px;
}
</style>
<script src="https://code.jquery.com/jquery-3.7.1.slim.min.js"></script>
<script>
$(() => {
  let shown = true
  let top = $('#item-container')
  let bot = $('#schedule')

  top.on('dblclick', ev => {
    if (shown) {
      top.height('100vh')
      bot.height(0)
      shown = false
    }
    else {
      top.height('50vh')
      bot.height('50vh')
      shown = true
    }
  });
});
</script>
</head>
<body>

<div id="item-container">
"""

TAIL = """
</div><!-- /item-container -->

<iframe id="schedule" src="https://events.linuxfoundation.org/open-source-summit-japan/program/schedule/"></iframe>

</body>
</html>
"""

def gen(file):
  vids = json.load(open(file))
  vids = [v for v in vids if 'OSS Japan 2023' in v['title']]

  # HACK: change title to "room - title"
  for v in vids:
    title = v['title']
    n1, n2, n3, n4 = title.split('-', 4)
    title = f"{n3} - {n2}".strip()
    if len(title) > 40:
      title = title[:40] + "..."
    v['title'] = title
  vids = sorted(vids, key=lambda v: v['title'])

  print(HEAD)
  for v in vids:
    url = "https://www.youtube.com/embed/" + v['videoId']
    title = v['title']

    vid = f"""
<div class="item">
{title}<br/>
<iframe class="item-video" src="{url}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>
"""
    print(vid)
  print(TAIL)

if len(sys.argv) < 2:
  print("Usage: yt-watchgen <json>", file=sys.stderr)
  sys.exit(0)
gen(sys.argv[1])
