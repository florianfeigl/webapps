---
id: "7"
title: "Fun with infrastructure and TLDs"
date: 2023-05-28
author: "182bit"
tags: "tld, subdomains, infrastructure"
---
My original intention was to create one user per TLD, thus subdirectories of this users root directory are created to serve different services, e.g. a jitsi server (jitsi.domain.tld), a jekyll blog (jekyll.domain.tld), a nextcloud solution (nextcloud.domain.tld), a fastapi webapp (fastapi.domain.tld), you get the idea.
Seems like this is not possible with jekyll and the approach is more that I will have to collect all the domains under the service of jekyll, e.g. /srv/jekyll/{domain1.tld, domain2.tld, domain3.tld} and so on and so forth, am I correct here?
It does seem that I am able to start jekyll within the target users directory, but an error pops up as soon as jekyll tries to write files (only allowed for owner of the directory).
Let's see if there is a way to doodle around this error, but in case it is not possible (without giving up reasonable directory permissions), I can live with the jekyll-as-a-user solution as well.
