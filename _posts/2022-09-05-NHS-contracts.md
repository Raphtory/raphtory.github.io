---
layout: post
title:  "NHS and the Chocolate Ne-PPE-tism Factory"
categories:  [Analysis With Raphtory]
author: 'Rachel Chan'
excerpt: In this article we will explore how we used Raphtory to investigate companies in the UK that received an NHS contract during the pandemic and their Persons with Significant Control.
---

![]({{ site.baseurl }}/images/nhscontracts/binbagppe.jpeg)
*The unfortunate consequence of the government's PPE buying strategy.*


On 23rd of March 2020, Boris Johnson announced the first coronavirus lockdown in the UK, ordering people to stay at home. As Covid-19 cases started to rise in the UK, hospital admissions for Covid-19 also started to rise. A substantial amount of personal protective equipment (PPE) needed to be ordered by the government to protect healthcare workers. However, it was already too little too late. The demand for PPE all over the world skyrocketed, leading to limited supplies and a huge price inflation.

To deal with the increased competition for PPE, the government invited new industry to come forward as PPE suppliers for our country. Many companies jumped onto this opportunity, creating a long list of suppliers waiting to be approved by the government. The government managed the high influx of offers by introducing a "High Priority Lane". If a supplier had connections with an MP, minister, or senior official, they were able to skip the line and were awarded a PPE contract straight away. However, several suppliers in the High Priority lane provided PPE that was not up to the required standard. Further still, many of these million pound contracts were awarded before <a href="https://www.theguardian.com/world/2021/dec/06/at-least-46-vip-lane-ppe-deals-awarded-before-formal-due-diligence-in-place" target="_blank">formal due diligence was put in place</a>. In early 2022, this VIP fast track system was ruled as <a href="https://rookirwinsweeney.co.uk/high-court-rules-that-government-acted-illegally-by-operating-a-vip-lane-when-awarding-ppe-contracts-in-a-judicial-review-brought-by-our-clients-good-law-project-and-everydoctor/" target="_blank">unlawful by the High Court</a>. 


![]({{ site.baseurl }}/images/nhscontracts/PPE-boxes.jpeg)
*Source: https://nursingnotes.co.uk/news/frontline-doctors-nurses-given-repurposed-bin-bags-as-official-ppe/*


At Pometry, we investigated all the <a href="https://www.tussell.com/insights/covid" target="_blank">companies</a> awarded an NHS contract during the pandemic. For each company registered on Companies House, we used Raphtory to identify all the beneficial owners and their percentage of shares in the company. Read on to find out how we used Raphtory to reveal companies with nepotistic structures, NHS money being funneled into the wrong pockets and the government's preferential treatment to friends and donors doing far more harm than good.

## What is a Person With Significant Control?

Before we delve into our findings, it is worth explaining what a person with significant control is.

A <a href="https://www.gov.uk/guidance/people-with-significant-control-pscs" target="_blank">person with significant control (PSC)</a> is someone who owns or controls a company, sometimes known as a "Beneficial Owner". In the UK, it is required by law to declare your companies PSC when opening up a company.

## PSC's and their percentage of ownership

Every PSC must include the level of their shares and voting rights, within the following categories:

* over 25% up to (and including) 50%.
* more than 50% and less than 75%.
* 75% or more.

With a list of all the suppliers that were awarded NHS contracts and their registered UK company numbers, we were able to scrape PSC information from each company using the <a href="https://developer-specs.company-information.service.gov.uk/companies-house-public-data-api/reference/persons-with-significant-control/list" target="_blank">Companies House Public API</a>, unveiling dodgy company structures that were given the responsibility of millions of pounds of taxpayer's money.

## The Chocolate NePPEtism Factory

Raphtory became our golden ticket into finding the exact people behind these million pound NHS contracts and their share of ownership within these contracts.

We took each company number in the <a href="https://www.tussell.com/insights/covid" target="_blank">Tussell NHS Covid Contract data</a> and scraped every Person With Significant Control (PSC) in these companies from the Companies House API. We ran an algorithm in Raphtory that linked companies to their PSCs with edges showing the share of ownership and the time they were appointed as a PSC in that company. On top of that, we linked all the PSCs in the same company together, creating a PSC network graph.

After a run of our data in Raphtory, a temporal network graph was created in less than a minute, with nodes displaying companies and people, along with the time at which these edges were created and the percentage of ownership that these people hold. This enabled us to quickly identify the people behind the companies awarded government money during the pandemic and their activity.

*Below is an interactive visualisation of the Raphtory output. It shows the company to PSC edges, with information on ownership and the date the PSC was notified on. We have filtered for companies with two or more PSCs for a cleaner visualisation. You can zoom in and out, hover over edges and move nodes around. The thickness of edges shows the weight of ownership.*

<div>
{% include nhsPSCGraph.html %}
</div>

In one of the sub-graphs, we found several PSCs registered under the surname "Walker", all of which are beneficiary owners of a company awarded NHS money to provide PPE. <a href="https://find-and-update.company-information.service.gov.uk/company/NI617785/persons-with-significant-control" target="_blank">Clandeboye Agencies Ltd</a> is the name of the company that received the contract, registered to deal with the "wholesale of sugar, chocolate and sugar confectionary". In total, Clandeboye was awarded £108m in PPE contracts and was also part of the government's VIP lane for companies with political connections.

The business activities of <a href="https://find-and-update.company-information.service.gov.uk/company/NI683839/persons-with-significant-control" target="_blank">Clady Group Ltd</a>, which took control of 75% or more of Clandeboye Agencies Ltd on 15th of March 2022, are disconcerting to say the least. On the Companies House website, Clady Group Ltd appointed 8 persons with significant control on the 3rd of April 2022, all of which registered with the surname "Walker", with the youngest being born in 2001. 

![]({{ site.baseurl }}/images/nhscontracts/clady-group-ownership.png)
![]({{ site.baseurl }}/images/nhscontracts/walkers.png)

From the period of May to July of 2020, Clandeboye Agencies shipped millions of items such as thumb-looped gowns and aprons from a factory in Cambodia to an NHS warehouse in England. Months later, it was revealed in <a href="https://www.bbc.co.uk/iplayer/episode/m0012ljx/spotlight-covid-contracts-hunting-for-ppe" target="_blank">BBC NI's Spotlight programme</a> that boxes from the same shipment had not been used by the NHS, and a box of PPE worth £1000 was being sold online for just £5. £1000 of taxpayer's money being turned into a measly £5 note, all for the provisions of the Walker family. 

![]({{ site.baseurl }}/images/nhscontracts/ppebox.jpeg)

*Source: https://www.bbc.co.uk/news/uk-northern-ireland-59651994*

Despite having no experience of making PPE supplies and the government receiving <a href="https://www.irishnews.com/news/northernirelandnews/2020/08/12/news/formal-legal-proceedings-begin-over-multi-million-pound-ppe-award-to-co-antrim-sweet-manufacturer-2032511/" target="_blank">over 24000 offers</a> from prospective suppliers of PPE, the sweets and chocolate manufacturer was directly handed a multimillion contract to provide PPE without any checks.

Another VIP worthy of mention is Fourds Limited, a <a href="https://www.blocblinds.co.uk/" target="_blank">blinds production business</a>. Awarded a <a href="https://ted.europa.eu/udl?uri=TED:NOTICE:338130-2020:TEXT:EN:HTML&src=0" target="_blank">£43.5 million contract</a> to provide PPE - a contract value 15 times larger than its net assets in 2019. 

Despite the economic hardships that the pandemic brought on many, Mr Ide and Cormac Diamond, the beneficial owners of Fourds Limited, had made a whopping <a href="https://www.belfasttelegraph.co.uk/business/ulsterbusiness/top-100/bloc-blinds-group-expands-into-us-as-sale-soar-to-1019m-41915552.html" target="_blank">£101.9m turnover for the year ending April 2021</a>. In our output, we found that Ide and Cormac Diamond ceased control of Fourds Limited in 2021, which is now significantly controlled by an overseas shell company with an Isle of Man PO Box address.

![]({{ site.baseurl }}/images/nhscontracts/fourds-limited.png)

By mapping out companies with their PSCs and their percentage of ownership in Raphtory, you can start to see where money from NHS contracts funnels down to. e.g. Patrick Byrne owns more than 50% of Pursuit Marketing Limited, but also owns more than 75% of Pursuit People Limited. The same pattern is seen in the other PSCs of these two companies. 

![]({{ site.baseurl }}/images/nhscontracts/ownershipchain.png)

![]({{ site.baseurl }}/images/nhscontracts/ownershipchain2.png)
Complex network graphs, such as the one below, become much easier to digest when mapped out in Raphtory.
![]({{ site.baseurl }}/images/nhscontracts/complexownership.png)

## Conclusions and Future Works

The Companies House API, together with the NHS contract data, has yet again provided us with fruitful insights into company activity and the people behind these companies. With Raphtory, we were able to identify the ultimate beneficiaries of companies given NHS contracts during the pandemic. This information led us to find questionable companies being awarded multimillion contracts without formal due diligence, and millions of taxpayer's money being funnelled down a family tree, all the way to a 20 year old.

This article uncovered government spending in the NHS during the pandemic. We are currently in the process of finding further use cases with Raphtory in the health sector. Give us a follow on Linkedin or Twitter to keep up to date with our latest updates and blog articles. 

# Interested in giving it a go yourself?

The basic version of this algorithm is available for free as part of the Raphtory Open Source Project. This can be run on any data you like as long as it fits the bipartite model described above.

If this is your first step into the world of temporal graphs, consider checking out the Introduction to Raphtory which will lead you into our Getting started guide. If you run into any issues you can get assistance from the wonderful Raphtory community on Slack.

If you would like to run these algorithms at scale in a production environment, drop the team at Pometry a message, and they will be more than happy to help.

