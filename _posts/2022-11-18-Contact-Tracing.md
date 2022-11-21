---
layout: post
title:  "How to avoid a Pingdemic with Temporal Graph Analytics"
categories:  [Analysis With Raphtory]
author: 'Rachel Chan'
excerpt: In this article we will explore how we used Raphtory to build an accurate contact tracing infection model.
---
![]({{ site.baseurl }}/images/contacttracing/selfisolate.jpeg)

After 2 years of sticking cotton buds up our noses, dialing into zoom calls in our pyjamas and social distanced walks, it is safe to say that COVID-19 changed our lifestyles in many different ways. Despite the continual bouts of fatigue caused by an increase in screen time, technology was utilised in new and fresh ways to reduce the spread of disease. An example of this is digital contact tracing, which was used all over the world as a strategy for slowing the spread of COVID-19. 

Contact tracing apps were typically used to track potential contacts with the virus. Before the COVID vaccine was introduced, such apps were helpful in guiding decisions on whether to see a loved one that was shielding. However, the soaring number of COVID cases in the UK caused a "pingdemic". In July 2021, a total of 520,194 alerts were sent to app users in one week. Users were "pinged" by the app to self isolate if they had spent 15 minutes within two metres of someone that had tested positive for COVID. Many businesses struggled to stay afloat as the sea of pings led hundreds and thousands of staff members to self isolate for ten days. 

Whilst the "pingdemic" phenonemon lowered the spread of COVID, more analysis could have been done on the app's contact tracing data to improve self isolation notifications. Carrying out infection model algorithms over timestamped contact tracing data could have been highly beneficial, sending notifications only to contacts made during the virus' transmission period.

In this blog, we will prove how modelling contact data over time as a temporal graph can shed light to more insights and whether an individual truly needs to self isolate. We took a <a target="_blank" href='http://www.sociopatterns.org/datasets/primary-school-temporal-network-data/'>temporal network dataset</a> of contacts between children and teachers in a primary school and ingested this into Raphtory. Raphtory creates a temporal graph with nodes representing children and teachers, and edges containing information on the individuals in contact and the time at which the contact took place. We then ran algorithms over this graph. 

The first algorithm we ran was the Discrete SI Model, the simplest form of all disease models. Individuals come into this model with no immunity (susceptible). Once infected, individuals stay infected and infectious throughout their entire life. This algorithm calculates which generation individuals in a population will be infected after the first infectious kid (seed) makes its first contact.

<br>
*Results from Discrete SI Model*

![]({{ site.baseurl }}/images/contacttracing/discretedataframe.png)
<br>
The second algorithm we ran was the Discrete SI Model with an added step of looking through the edge history. This develops on the first algorithm by looking into the history of contacts each individual has made. In this way, repeated contacts with the same people will not be skipped and still count towards the infection count.

<br>
*Results from Discrete SI Model with the addition of looking at edge history, notice the additional contacts have increased the number of individuals infected*
<br>
![]({{ site.baseurl }}/images/contacttracing/interactionsdataframe.png)
<br>
![]({{ site.baseurl }}/images/contacttracing/SI.png)

The last algorithm factors in time, hence we can go beyond the simple SI model by adding the time an individual recovers from a disease and the time at which an individual cannot infect anyone. For example, if a kid was infectious 2 weeks before contact was made, it is unlikely that the kid can spread the disease as they will have recovered by then. 

<br>
*Results from the Temporal SI model, notice that the output has filtered to a more accurate representation of infections, including time at which individual was infected*
<br>
![]({{ site.baseurl }}/images/contacttracing/temporaldataframe.png)

![]({{ site.baseurl }}/images/contacttracing/temporal.png)
<br>
*Results from the Temporal SI algorithm visualised with <a href="https://www.pathpy.net/" target="_blank">PathPy</a>. Use the Play button or slider to see nodes being infected over time*

<div>
{% include temporal_graph.html %}
</div>