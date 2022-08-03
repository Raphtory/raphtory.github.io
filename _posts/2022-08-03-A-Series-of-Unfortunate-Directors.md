---
layout: post
title:  "A Series of Unfortunate Directors"
categories:  [Analysis With Raphtory]
author: 'Rachel Chan'
excerpt: In this article we will explore how we used Raphtory to identify fishy behaviour on Companies House.
---

![](https://i.imgur.com/0Le2IAj.jpg)

*29 Harley Street, London.*

Amongst some of the top private medical clinics, in the heart of London, lies 29 Harley Street. It has been the headquarters for more than 3000 companies. This beautiful Georgian building is the front office for companies around the world seeking an address on a prestigious street in London. However, behind the ornate balconies and the grand double-door entrance, this address has been used by criminals to carry out a <a href="https://archives.fbi.gov/archives/sanfrancisco/press-releases/2011/defendants-in-multi-million-dollar-investment-fraud-scheme-sentenced-to-prison" target="_blank">multi-million-dollar investment fraud scheme</a> and to <a href="https://www.dailymail.co.uk/news/article-3439235/Long-haired-fraudster-posed-Pope-s-banker-fleece-Dutch-shipping-firm-73million-jailed-14-years.html" target="_blank">launder stolen money from Allseas, a Dutch shipping company</a>. At Pometry, we used **Raphtory** to expose other entities utilising UK addresses to hide their criminal activity. Read on to find out more...

## What is Companies House? :briefcase: :house: 

Companies House is an institution that stores information on all private limited companies in the United Kingdom. Setting up a company used to be time-consuming and cumbersome, but ever since Companies House introduced online applications, there are now over 4.5m companies registered. It takes a few minutes to fill in an online application, and upon a payment of £12, your company will be registered within 24 hours.

## Company Formation Agents :briefcase: :sunglasses:

Company formation agents started emerging and taking advantage of this new online system. A formation agent is a company that creates other companies on behalf of clients all over the world. Not only do agents reduce the administrative work required to set up a company, it is surprisingly cheap, appealing to many businesses that want to start trading quickly. Some turn to agents for legitimate business reasons, whilst others use these agents to set up dummy corporations to hide their financial dealings.

### Shell or Shelf? :shell: :books: 

Formation agents can help clients create a ***shell company*** or offer an existing ***shelf company***. 

A shell company is created to hold funds and manage another entity's financial transactions. For example, a new startup may use a shell company to store the money they have raised before it officially launches. 

A shelf company is an out-of-the-box company that is available to purchase. The advantage of a shelf company is that they have years of documents, giving the impression of longevity of a company.

### Dodgy Directors and their high turnover of companies :dash:

At Pometry, we used **Raphtory** to investigate [Companies House data](https://developer.company-information.service.gov.uk/), finding patterns of illegal behaviour amongst registered companies in the UK. 

For a subset of 12749 companies collected from the <a href="https://developer-specs.company-information.service.gov.uk/streaming-api/reference/company-information/stream" target="_blank">Companies House Streaming API</a>, we built a Python scraper and left it running overnight to find the <a href="https://developer-specs.company-information.service.gov.uk/companies-house-public-data-api/reference/officers/list" target="_blank">list of officers</a> associated to these companies, and <a href="https://developer-specs.company-information.service.gov.uk/companies-house-public-data-api/reference/officer-appointments/list" target="_blank">all the companies they have been or are currently appointed to</a>.

In **Raphtory**, we ran an Edge List algorithm on the Companies House data we had scraped, linking Company Officers to their current and past companies. These so-called "Company Officers" can also be companies that own other companies, giving way to complex company structures. After filtering down Company Officers that had over 50,000 companies (all of which had been dissolved) we found that these Company Officers were in fact Company Formation Agents. A shocking pattern was found when investigating the dates that these companies were created and dissolved.

### Company Formation Agents or Fraud Formation Agents? :rotating_light:  

The companies that were linked to these formation agents in our data were being opened and closed in a short space of time, some agents were even opening and closing most of their companies on the same day.

One of the company formation agents we found in our analysis was "Nominee Secretary Ltd", a shell company owned by Corporate Nominees Ltd, which in turn was owned by Legal Nominees, centred at the heart of Formation House's complex structure of companies. It is not illegal to own or control anonymous companies. However, it allows individuals to evade tax, launder money and hide assets behind these anonymous companies.

<img src="https://i.imgur.com/HHGrrHj.jpg" alt="Formation House Structure" width="800" height="600" />

<em>Histogram plot for "Nominee Secretary Ltd", this plot shows the duration of time that the companies were active before they were dissolved.</em>
<img src="https://i.imgur.com/0FiPAEH.png" alt="Histogram plot for 'Nominee Secretary Ltd'" width="400" height="300" />

As shown in the graph above, most companies owned by Nominees Secretary Ltd did not last long before they were dissolved.

A project called [#29Leaks](https://www.occrp.org/en/29leaks/), spearheaded by multiple reporters, found that Formations House was involved in several high profile scams, where UK authorities failed to take action. Individuals that were found by police were prosecuted and given a lengthy prison sentence - however many individuals are still on the run.

---

In addition to Formation House, two other Company Formation Agents with similar company activities in our analysis were found to be linked to several cases of fraud, including a <a href="https://www.hamhigh.co.uk/news/finchley-road-company-factory-tenants-speak-out-ahead-of-register-3638200" target="_blank">telecoms scam backed by the Mafia</a>. The agents went by the names - Temple Secretaries Limited and Company Directors Limited. Not only were these agents registered at the same address, 788-790 Finchley Road, they were both directors at the same companies, opening and closing companies on the same dates. (See histogram plots below).

<em>Histogram plots for "Temple Secretaries Limited" and "Company Directors Limited" respectively, the plots show the duration of time that the companies were active before they were dissolved.</em>

<img src="https://i.imgur.com/AY0kGZp.png" alt="Histogram plot for 'Temple Secretaries Limited'" width="400" height="300" />

<img src="https://i.imgur.com/u0TwFyN.png" alt="Histogram plot for 'Company Directors Limited'" width="400" height="300" />

Most of the companies owned by these agents were opened and closed within the same day. Firms registered at this Finchley Road address were eventually found to be linked to <a href="https://www.hamhigh.co.uk/news/finchley-road-company-factory-tenants-speak-out-ahead-of-register-3638200" target="_blank">international scandals of money laundering and political corruption</a>.

<em>The complex company structure of Finchley Road's formation agents that could explain the similar company activities of Temple Secretaries Limited and Company Directors Limited.</em>
<img src="https://i.imgur.com/USGDCb8.jpg" alt="The complex company structure of Finchley Road's formation agents" width="800" height="600" />

To this day, there are still active companies registered under Temple Secretaries Ltd and Company Directors Ltd at this derelict Finchley Road office. 

<em>The neglected interior of 788-790 Finchley Road, once a bustling front for hundreds and thousands of companies. (Source: Archant) </em>
<img src="https://i.imgur.com/6wpbJA5.jpg" alt="The neglected interior of 788-790 Finchley Road" width="600" height="500" />

## Conclusion and Future Work
By the end of March 2022, the number of companies on the Companies House register was <a href="https://www.gov.uk/government/statistics/companies-register-activities-statistical-release-2021-to-2022/companies-register-activities-2021-to-2022" target="_blank">over 4.8m with over 750k new companies</a>. The ease of setting up a company on Companies House and the lack of checks on the platform has given a way for criminals to hide dirty money behind anonymous companies. 

With **Raphtory**, we were able to sift through Companies House data and find these suspicious individuals just by mapping Company Officers to their Companies. Our platform has the sophistication to do more complex algorithms, exposing convuluted company structures just like the ones discussed above, and  identifying individuals that are pocketing most of the companies money  (Ultimate Beneficial Owners).

If you would like to learn more about Raphtory, drop the <a href="https://www.pometry.com/contact/" target="_blank">Pometry</a> team a message and they will be more than happy to help. 


# Interested in giving it a go yourself?
The basic version of this algorithm is <a href="https://github.com/Raphtory/Raphtory/blob/master/core/src/main/scala/com/raphtory/algorithms/generic/EdgeList.scala" target="_blank">available</a> for free as part of the <a href="https://github.com/Raphtory/Raphtory" target="_blank">Raphtory Open Source Project</a>. This can be run on any data you like as long as it fits a bipartite model.

If this is your first step into the world of temporal graphs, consider checking out the <a href="https://www.raphtory.com/about" target="_blank">Introduction to Raphtory</a> which will lead you into our <a href="https://docs.raphtory.com" target="_blank">Getting Started guide</a>. If you run into any issues you can get assistance from the wonderful Raphtory community on <a href="https://join.slack.com/t/raphtory/shared_invite/zt-xbebws9j-VgPIFRleJFJBwmpf81tvxA" target="_blank">Slack</a>.
If you would like to run these algorithms at scale in a production environment, drop the team at <a href="https://www.pometry.com/contact/" target="_blank">Pometry</a> a message, and they will be more than happy to help.
