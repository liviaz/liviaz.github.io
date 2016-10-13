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

### Biomechanical parameters

I developed and built a device to measure an embryo's biomechanical properties by applying a controlled pressure to it through a micropipette and observing its response. As seen below, embryos which appear morphologically similar can have dramatically different responses to the same applied pressure.

<div style="width:400px; margin:auto; margin-top: 20px; text-align: center; " markdown="1">
![morphology grading](../images/embryo-pressure.svg)
</div>

The data gathered for each embryo is its aspiration depth into the micropipette over time. For the two embryos in the images above, the data collected could look something like the image below, where one goes much farther into the pipette.

<div class="50pct-img" style="width:400px; margin:auto; margin-top: 20px; text-align: center; " markdown="1">
![morphology grading](../images/embryo-pressure-example.svg)
</div>

**Model generation:** How can we quantify these variations in response? Based on the literature in cell mechanics, a bulk viscoelastic model is generally a good choice. Cells have been shown to have both liquid-like (viscous) and solid-like (elastic) mechanical behavior, which varies based on cell type, disease state, and other factors. Elastic behavior in mechanical models is typically represented by springs, while viscous behavior is represented by dashpots as shown below.

<div class="post-image" style="width:400px; margin:auto; margin-top: 20px; text-align: center; " markdown="1">
![morphology grading](../images/spring-dashpot.svg)
</div>

By combining these elements in various arrangements in parallel and/or in series, one can build an infinite number of viscoelastic models which could describe cell behavior. A few models are shown below, starting with 2-element models (on the left) and including an example of a possible 5-element model (on the right).

<div class="post-image" style="width:80%; margin:auto; margin-top: 20px; text-align: center; " markdown="1">
![morphology grading](../images/different-models.svg)
</div>

There are many possible types of models but I only tested these 5 because they are commonly used in the literature and because deriving the solution becomes increasingly difficult (and numerical computation becomes drastically slower) as more elements are added. 

**Model selection:** So ... which of these models best describes the behavior of an embryo in response to a step pressure input? One common strategy is to fit each model to a set of recorded data and calculate the mean square error (MSE) within that data set. This has the pitfall that the most complex model will always have the lowest in-sample error and can lead to overfitting. Therefore, it is best to fit the model to a set of training data first and calculate its error on an independent set of testing data to estimate its true generalization error. This concept is illustrated in the image below which is adapted from [Wikipedia](https://en.wikipedia.org/wiki/Overfitting#/media/File:Overfitting_svg.svg).
 
<div class="post-image" style="width:50%; margin:auto; margin-top: 20px; text-align: center; " markdown="1">
![morphology grading](../images/overfitting.svg)
</div>

For each embryo, I only had one set of data points which described its response to pressure. Because applying pressure to an embryo can change its mechanical properties, I couldn't just measure an embryo again to obtain an independent set of testing data. To compensate for this I used cross-validation within the data from a single measurement and computed an "out-of-sample" testing error by combining model predictions across testing partitions. A sample of each model's fit to data from one embryo is shown below.

<div class="post-image" style="width:80%; margin:auto; margin-top: 20px; text-align: center; " markdown="1">
![morphology grading](../images/model-selection.svg)
</div>

Qualitatively, the 4-parameter modified SLS and the 5-parameter Wiechert models appear to fit the data well, and so we can guess that the 4-parameter modified SLS is the best model because it has the lower complexity of the two. A plot of the training (in-sample) and testing (generalization / out-of-sample) errors are shown below for all models. For each model, the testing error was averaged over data from 197 mouse embryos. 

<div class="post-image" style="width:80%; margin:auto; margin-top: 20px; text-align: center; " markdown="1">
![morphology grading](../images/model-selection-plot.svg)
</div>

Here our previous intuition is confirmed, and it again appears that the 4-parameter modified SLS has the lowest testing error and thus is the best model to describe the mechanical behavior of a 1-cell embryo. Because this is still a bulk model, it is important to note that the 4 parameters do not correspond to individual structures within the embryo, but rather describe its behavior as if it were a homogeneous material. 

### Predicting viability  

_Now that we have defined these 4 parameters and can measure them, can we use them to predict viability?_

The experimental design I used to answer this question is shown below, where ideally a measurement at day 1 after fertilization could be used to predict development to a later time point. In this case, development to the day 5-6 blastocyst stage is used as a proxy for viability, where embryos reaching this milestone are labeled "viable," and the rest are labeled "nonviable." Of course, not all embryos which develop to the day 5-6 blastocyst stage will go on to become a live birth, so this is not a perfectly reliable indicator of viability. 

<div class="post-image" style="width:80%; margin:auto; margin-top: 20px; text-align: center; " markdown="1">
![morphology grading](../images/experimental-design.svg)
</div>

I gathered data on 89 human research embryos and 235 more human embryos as part of a pilot clinical study at day 1 after fertilization. Although 

2D scatter plot of parameters




Bar plot 




Classification and SVM decision boundary




Feature selection




Comparison to morphology and ROC curves






### Conclusions


**Time lapse imaging parameters:** I also gathered some imaging parameters to see how their performance in viability prediction compares to that of mechanical parameters. These imaging parameters can be measured using commercially available equipment found in IVF clinics, and correspond to the length of time between various cell divisions and other events in development. 

The scientific premise behind these parameters is generally that embryos which develop too slowly or too quickly are abnormal in some way and not likely to be viable. A couple of papers from [2010](http://www.nature.com/nbt/journal/v28/n10/abs/nbt.1686.html) and [2011](http://humrep.oxfordjournals.org/content/26/10/2658.short) describe some specific timing intervals which may be particularly predictive of viability.


Go into a little bit of detail on what is currently measured and how "optimal" region is determined.
Talk about what other parameters we measured and how we can improve on simple thresholding.



