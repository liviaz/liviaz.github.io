---
layout: post
title: Predicting embryo viability
permalink: predicting-viability
---

# Project: predicting embryo viability

The goal of this project was to develop a predictor of embryo viability with better performance compared to the current clinical gold standard. You can read more about the motivation behind this project and the clinical need in _in vitro_ fertilization (IVF) [here](../clinical-need.html).

On this page I will go into detail about how I gathered parameters for my model and how I validated them in a laboratory and clinical setting. This material is drawn from [my recently published paper](http://www.nature.com/ncomms/2016/160224/ncomms10809/full/ncomms10809.html) and also from my class project for CS 229 at Stanford (Machine Learning).


### What is currently done?

**Gold standard:** In IVF clinics today, embryos are typically chosen for transfer based on a morphological assessment. This assessment includes information about the number of cells in the embryo (embryos which develop more slowly are less viable), and some qualitative parameter(s) about the appearance of those cells (embryos which are fragmented or asymmetrical are also less viable). For a transfer at the day 5 blastocyst stage, examples of good and poor morphology are shown below.

<div style="width:400px; margin:auto; margin-top: 20px; text-align: center; display:block; vertical-align:center;" markdown="1">
![morphology grading](../images/embryo-morphology-2.svg)
</div>

**How well can morphology predict viability?** One [study](http://www.sciencedirect.com/science/article/pii/S0015028206044530) of over 2000 IVF cycles evaluated the ability of the day 5 morphological grade to predict clinical pregnancy. It reported an area under the ROC curve of approximately 0.66, which is better than choosing embryos for transfer at random but not really high enough to be considered a "good" predictor. 

At a sensitivity value of 68% (which is where they set their threshold), the positive predictive value was only 44%. This means that only 44% of _good morphology_ embryos transferred actually resulted in a pregnancy -- not a stellar success rate. However, only 31% of _all_ embryos transferred resulted in a pregnancy, so morphology did have some value in identifying viable embryos. 

Still, I thought we can do better, so I decided to gather other kinds of parameters to construct a better predictor of viability.

### Searching for a better predictor of viability

My criteria for choosing parameters to measure were guided by their potential for clinical application. This means I was looking for data that I could gather noninvasively and without significant disruption to the existing clinical workflow. I also wanted to focus on parameters which could be measured objectively. There is a lot of variability in human-assigned morphological scores which probably contributes to the poor predictive value of morphological assessment. In the end, I settled on two kinds of parameters which are described below.

**Biomechanical parameters:** I developed a biomechanical model of an embryo and built a device to measure its viscous and elastic parameters. The measurement works by applying a controlled pressure to the edge of an embryo and observing its response to the pressure over time. As seen below, embryos which appear similar can have dramatically different responses to the same applied pressure.

<div style="width:400px; margin:auto; margin-top: 20px; text-align: center; " markdown="1">
![morphology grading](../images/embryo-pressure.svg)
</div>

How can we quantify these variations in response? 

Show measurement/model
Talk about fitting model to data
Talk about model selection


**Time lapse imaging parameters:** These parameters can be measured using commercially available equipment found in IVF clinics, and correspond to the length of time between various cell divisions and other events in development.

Go into a little bit of detail on what is currently measured and how "optimal" region is determined.
Talk about what other parameters we measured and how we can improve on simple thresholding.




***Include schematic of prediction based on multiple types of parameters***
*** Include some equations with MathJax? ***



### Finding the optimal combination






### Conclusions






