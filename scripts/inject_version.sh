#!/bin/sh

replacer="1.1.2"
shortened_hash="$(echo $commit | head -c 7)"

if [[ $tag == "refs/tags/"* ]]; then
    tag_remove="refs/tags/"
    new_tag=${tag#"${tag_remove}"}
    tag=$new_tag
fi

if [ ! -z $tag ]; then
  echo "Tag ${tag} found. Using tag..."
  sed -i "s/define config.version = \"$replacer\"/define config.version = \"${tag}-rpy_${sdk}\"/g" mod/game/options.rpy;
  cat mod/game/options.rpy | grep config.version;
else
  echo "No tag found. Using Git hash..."
  sed -i "s/config.version = \"$replacer\"/config.version = \"${shortened_hash}-rpy_${sdk}\"/g" mod/game/options.rpy;
  cat mod/game/options.rpy | grep config.version;
fi