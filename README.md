# Best-effort Finnish Hunspell dictionary

Why? The "flagship" Finnish spelling effort, Voikko, is not compatible with webextentions. I do not take any position on how things should be developed, and I do understand how that cameout to be. But from a user's perspective, the sad fact is that Finnish is not a supported spelling language in Thunderbird. As a foreigner living in Finland, who has to write emails in Finnish all the time, this affects my productivity.

As a stopgap solution, I built this best-effort dictionary using the following resources:

  1) The TurkuNLP Finnish parsebank, a large corpus of parsed Finnish. This is my source of (lemma,form) pairs
  2) Voikko to filter this vocabulary to correctly spelled forms
  3) The hunspell-builder program which was developed for the Slovak hunspell project, and which is capable of building a dictionary directly from a list of (lemma,form)

# Evaluation

I am sorry, I have no time to properly evaluate this. I suspect that it might be insufficient for a native Finn fine-tuning carefully crafted text, but it seems more than enough for a foreigner like me, struggling to decide between uutiset and uuttiset. :) One way or another, it is much, much better than nothing!

# License

CC0

# Acknowledgments

TurkuNLP, Voikko, and the authors of huspell-builder

# Release

Built, packaged, and released on 6.12.2023 as Finnish Independence Day present to this glorious country. Hyvää itsenäisyyspäivää!
