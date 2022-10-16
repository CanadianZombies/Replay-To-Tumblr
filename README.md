[![Stars](https://img.shields.io/github/stars/canadianzombies/Replay-To-Tumblr.svg?style=plastic)](https://github.com/canadianzombies/Replay-To-Tumblr/stargazers)
[![Issues](https://img.shields.io/github/issues/canadianzombies/replay-to-tumblr?style=plastic)](https://github.com/canadianzombies/Replay-To-Tumblr/issues)
[![Size](https://img.shields.io/github/repo-size/canadianzombies/Replay-To-Tumblr.svg?style=plastic)](https://github.com/canadianzombies/Replay-To-Tumblr)
[![Discord](https://img.shields.io/discord/234145231359049729?style=plastic)](https://discord.gg/bCsV7km9PE)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg?style=plastic)](https://github.com/psf/black)
[![Donate PayPal](https://img.shields.io/badge/donate-paypal-blue.svg?style=plastic)](https://www.paypal.me/livesimmy)


# Replay-To-Tumblr
Replay-To-Tumblr is TumblrPost 2.0 (TumblrPost has been made private now that 2.0 is released)

# Setup

Fill in the tumblr_credentials.json file
Edit replay-to-tumblr.py to fill in your username/file-path/etc.

# Help / Contact

If you need help setting this up, please reach out to me on my live stream: fb.gg/livesimmy
I love to talk shop and code live on stream.

If you aren't able to reach me on FB, then reach out on twitter.com/livesimmy

# Goal of this Script

The goal of this is to push your video to tumblr automatically.

An example of this is when I take an instant replay live on stream (fb.gg/livesimmy) it
takes the instant replay and pushes it to tumblr. Through IFTTT I push the video to twitter.

I also have my tumblr linked to another account and it will do a tweet based off of the random
string that the script generates. So two separate accounts get a post about the live stream
and the clip.

This is vitally useful to engage social media as a tool.

I 100% recommend utilizing social media as your friend to grow your channel!

Good luck streaming!

# Random String
The random string that is generated is generated using a few different systems. These are utilized
to create a different effect on your social media presense. These are tailored to my own stream.
You will need to change them to best fit your own stream.

Most instances where a streamer name will be utilized is located in the STREAMER_NAME global.
Array: Phrases[], this is pre-configured random strings where it implants the STREAMER_NAME at the start
and it randomly takes it and uses it.

Intro: this generates how the tweet will start, with phrases such as 'Breaking News:'. This gives it
some meaning.

From there it will randomly select a number and based on what the number is, it will either select
a random string, generate a random string, use a premade array of strings, and choose/generate accordingly.

Array: captions_to_use[] this is the title of your post on tumblr. It can also be selected for the 
tweet string.

Array: rand_1, rand_2, rand_3, rand_4. These are 4 different arrays that bound together and create a
sentence. These are randomly selected per array and have varying results.

Array: names, verbs, nouns, ends. These 4 arrays create another sentence when bound together. This
is oddly the most in-depth string generator.

Afterwards it assigns a random hashtag from a list of possible hashtags.

Finally it will select from a list of twitter accounts to tag. This will take the first three possible tags
in the array (if there is enough space remaining in the tweet), and fill them in. From there it will
attempt to fill out the rest with random tags.

This ensures that each tweet is something new, each caption for tumblr is also something new.

# Future Updates

This source will be updated as issues are identified.

# Next Steps

Screenshot to tumblr is the next goal. The code is primarily ready for it however it has not been tested
as it is currently hardcoded to upload an MP4. Screenshots are next on the list of to-do.

There will be more possible phrases added to the lists in varying hilarity.
There will also be new hashtags added.


