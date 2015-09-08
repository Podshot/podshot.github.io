---
layout: post
title:  "Two Together and status update"
date:   2015-09-08 20:18:14
categories: update
---
Hello again! I felt it was time for another update on a variety of things
since it has been about a month since my last post. So let's get on with it.

<h3>Two Together</h3>
Ever since the public demo of Two Together, I have gotten amazing feedback
on how to improve the game and make it better, however, with school and
life sometimes getting in the way of me being able to work on the various
projects I love to contribute to. So I have decided to open source it so
anyone who wants to learn how to make games (with my method/code layout)
can have some help. This will also allow me to be able to get help when 
I get stuck on a problem/bug. The Github repository can be found <a href="https://github.com/Podshot/TwoTogether">here</a>

<h3>MCEdit-Unified</h3>
Recently I tweeted a picture teasing a new "waypoints" feature in MCEdit-Unified.
I want to explain the details of how they will be stored before the update is
released. To start off, all the waypoints will be stored in a NBT file named "mcedit_waypoints.dat"
in the world save folder. This NBT format outline can be found <a href="https://gist.github.com/Podshot/c30d9b980cde4e7485d6">here</a>
Each world will have their own mcedit_waypoints.dat file, and to remove all waypoints in a world,
you just need to delete the file. You will also be able to create/delete waypoints through the waypoint dialog inside MCEdit 