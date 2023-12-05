#!/bin/sh

dump() {
  local url="$1"

  http "$url" | sed -ne 's/^.*ytInitialData = //p' | jq -r '.contents[].tabs[] | select(.tabRenderer.title =="ライブ") | [.tabRenderer.content[].contents[].richItemRenderer.content.videoRenderer | select(.videoId) | {videoId: .videoId, title:.title.runs[].text}] | sort_by(.title) | @json'
}

YTURL=$1
: ${YTURL:=https://www.youtube.com/@LinuxfoundationOrg/streams}

dump "$YTURL"
