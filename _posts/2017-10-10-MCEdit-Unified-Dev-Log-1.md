---
layout: post
title: "MCEdit-Unified Dev Log: Road to v1.6.0.0 Part 1"
date: 2017-10-05
comments: true
categories: mcedit
---
<h3>Part 1: Getting builds flowing</h3>
<h4>Background</h4>
Since the beginning, the MCEdit-Unified team has had a very *interesting* build/release pipeline. Up to this point,
all of our releases had been built by Project Organizer/Leader @Khroki. He had access to both Mac and Windows
machines, so he was in the best position to build our releases. However, if we wanted to test a feature when it
was compiled, we would have to wait for him to build a testing build. We thought about finding a continuous
integration service to periodically build testing releases, but we couldn't find one that ran a Windows 
environment, so we just stayed with out current system.

<h4>The problem</h4>
While our system had been successful so far, it relied on Khroki's availability and resulted in us having to
find days when both we were available to test the compiled build and address any last minute issues and that
Khroki had enough time to build the release and notify us of any errors. With our various schedules and the
fact that we're located around the world, it took a lot of effort. However, now with none of us being able 
to contact Khroki, we had to build testing releases ourselves and without any references to our old build 
set up.

<h4>Setting the stage (Environment)</h4>
When I started looking for a Continuous Integration system that supported a Windows environment, I recalled that
@codewarrior0 had a system similar to the one we wanted to implement. The service he used called Appveyor had an 
option for a Windows environment. The next step is to configure the said environment. Appveyor uses a [YAML file](https://github.com/Khroki/MCEdit-Unified/blob/master/appveyor.yml) to
handle the environment and build stages. Since we can just build MCEdit-Unified from two commands, we just set one
build stage to run {% highlight shell %} pip install -r requirements.txt {% endhighlight %} which installs all of
the requirements needed to run MCEdit and another to run {% highlight shell %} pyinstaller mcedit-ci.spec -y {% endhighlight %} 
which runs our PyInstaller script to actually build the executable.

<h4>Building the build script</h4>
With the environment set up, I now needed to create a completely new build script for PyInstaller since we couldn't
get the one we've previously used for our releases from Khroki (see "The problem" section). While looking over how
CodeWarrior0 organized his build system, I realized that the PyInstaller build script is actually just a python script
with some fancy functions that PyInstaller imports to know how to build the executable. Using MCEdit2's script as a
reference, we created a automated [build script](https://github.com/Khroki/MCEdit-Unified/blob/master/mcedit-ci.spec) 
that includes all of our data files (like filters, schematics, etc) andmoves DLL binaries into the executable's folder. 
After all of this happens, the directory is collected into a ZIP file for uploading.

<h4>Conclusion</h4>
With all of this inplace, we're now able to build testing releases on a regular basis without needing to install various
utilities and programs. While we would've liked something like this set up earlier, we feel that introducing this for 
1.6.0.0 will help us make a smoother and more stable release.

*I'm going to try to make weekly posts on projects I'm working on and going into detail about design choices I make. I know
this post wasn't very technical and was a wall of text, but I'll try to keep posts like this to a minimum. If you have
any tips or things that I might be able to improve on, please put those in the comments or contacting me on Twitter.*