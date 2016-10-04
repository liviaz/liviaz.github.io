---
layout: post
title: Predicting embryo viability
permalink: predicting-viability
---

# Project: predicting embryo viability

In this post I will briefly introduce the clinical need (and the motivation behind this project). Then I will go into more detail about the approach I used to tackle the problem of predicting embryo viability and show some results. The material on this page is drawn from [my recently published paper](http://www.nature.com/ncomms/2016/160224/ncomms10809/full/ncomms10809.html) and also from my class project for CS 229 at Stanford (Machine Learning).

### Clinical need

The focus of my research was to improve outcomes of *in vitro* fertilization (IVF), with the end goal of improving pregnancy rates and reducing the incidence of negative outcomes such as miscarriage, pregnancy complications and preterm birth. These negative outcomes often happen for one of two reasons: 

1. __no viable embryos__ are transferred and the patient does not become pregnant or miscarries
2. __two or more viable embryos__ are transferred and the patient has twins or triplets, which have a very high risk of complications and preterm birth

To avoid these poor outcomes, physicians would ideally want to transfer **exactly one viable embryo** to their patient so that they have a singleton pregnancy. Unfortunately it is currently very difficult to figure out which embryos are viable and which are not. Typically the embryos which look "good" are presumed to be viable, but this approach has very poor positive predictive value (that is, even among embryos which look "good" only about 50-60% are actually viable). A real clinical example is shown below: all of the embryos shown appear to have good morphology, but only one actually resulted in a pregnancy upon transfer.

<div style="width:300px; text-align:center; margin:auto;" markdown="1">
![morphologically similar embryos](../images/SampleEmbryos.png)
</div>

*So it seems that we need a more accurate predictor of viability to help physicians make better decisions about which embryos to transfer.*

### What else can we measure besides morphology?

In my quest to find a better predictor viability, I settled on two types of parameters to measure. I chose these because they can be measured noninvasively with minimal disturbance to the embryo.

1. Time lapse imaging parameters (basically, the length of time between cell divisions and other events in development)
2. Biomechanical parameters (I thought the embryo's stiffness and viscosity could be indicative of viability)

The imaging parameters can be measured by 


***Include schematic of prediction based on multiple types of parameters***
*** Include some equations with MathJax ***



### Finding the optimal combination






### Conclusions






