---
layout: post
title:  "NHS and the Chocolate Ne-PPE-tism Factory"
categories:  [Analysis With Raphtory]
author: 'Rachel Chan'
excerpt: In this article we will explore how we used Raphtory to investigate companies in the UK that received an NHS contract during the pandemic and their Persons with Significant Control.
---

On 23rd of March 2020, Boris Johnson announced the first coronavirus lockdown in the UK, ordering people to stay at home. As Covid-19 cases started to rise in the UK, hospital admissions for COVID-19 also started to rise. A substantial amount of personal protective equipment (PPE) needed to be ordered by the government to protect healthcare workers. However, it was already too little too late. The demand for PPE all over the world skyrocketed, leading to limited supplies and a huge price inflation.

To deal with the increased competition for PPE, the government invited industry to come forward as suppliers of PPE for our country. In addition to opening up contracts for fresh suppliers, they introduced the "High Priority Lane" whereby suppliers could pass on offers directly to MPs, ministers, and senior officials, who in turn directed these offers to a dedicated location, skipping the long list of suppliers offering the government their services to provide PPE. In early 2022, this VIP fast track system was ruled as <a href="https://rookirwinsweeney.co.uk/high-court-rules-that-government-acted-illegally-by-operating-a-vip-lane-when-awarding-ppe-contracts-in-a-judicial-review-brought-by-our-clients-good-law-project-and-everydoctor/" target="_blank">unlawful by the High Court</a>. 

At Pometry, we had a look into the <a href="https://www.tussell.com/insights/covid" target="_blank">list of companies</a> that were awarded a contract from the government in response to COVID-19. We used Raphtory to find the beneficial owners of these companies, along with their percentage of shares in the company, unveiling the people behind billions and billions of taxpayer's money. Read on to find out how some of these companies benefitted from the VIP lane and wasted hundreds and millions of taxpayers money.

## What is a Person With Significant Control?

A <a href="https://www.gov.uk/guidance/people-with-significant-control-pscs" target="_blank">person with significant control (PSC)</a> is someone who owns or controls a company, sometimes known as a "Beneficial Owner". In the UK, it is required by law to declare your companies PSC when opening up a company.

## PSC's and their percentage of ownership

Every PSC must include the level of their shares and voting rights, within the following categories:

* over 25% up to (and including) 50%.
* more than 50% and less than 75%.
* 75% or more.

With a list of all the suppliers that were awarded NHS contracts and their registered UK company numbers, we were able to scrape PSC information from each company using the <a href="https://developer-specs.company-information.service.gov.uk/companies-house-public-data-api/reference/persons-with-significant-control/list" target="_blank">Companies House Public API</a>.

## Company Formation Agents
In our previous <a href="https://www.raphtory.com/A-Series-of-Unfortunate-Directors/" target="_blank">blog</a>, we investigated Company Formation Agents that were registering and closing many companies within the same day. Some of these companies were found to be linked to money laundering and political corruption scandals. 

With the same subset of data, we scraped PSC information from these companies, creating a vertex for PSC and a vertex for company. We attached the PSC's percentage of ownership as the weight of an edge linking PSC to Company. After filtering for PSC's owning more than 100 companies, we plotted scatter plots of PSC's registering new companies over time, in addition to a plot of PSC's closing companies over time. The hue of the points on the plots show the PSC's level of share ownership of the company, the darker the dot, the higher the share ownership percentage.

<em>Unlike for company directors, Companies House does not store unique ID's for PSC's, so we created an ID using the PSC name, along with their date of birth. This explains why PSC's that are a Private Limited Company have "-00" attached to the end of their names.</em>

![]({{ site.baseurl }}/images/nhscontracts/registering.png)

![]({{ site.baseurl }}/images/nhscontracts/closing.png)

In the second graph, PSCs such as Fd Secretarial Ltd and Woodberry Secretarial Limited are closing many companies where they hold 75% or more shares in short periods of time. Moreover, Sdg Secretaries Limited and Sdg Registrars Limited of the first graph, along with Fd Secretarial Ltd and Woodberry Secretarial Limited of the second graph, are all part of the same company formation agent structure.

![]({{ site.baseurl }}/images/nhscontracts/dodgypscs.png)

In our previous blog, we detailed the Finchley Road company formation agents structure. One of the companies within the convoluted structure was <a href="https://www.a1companies.com/" target="_blank">A1 Company Services</a>. In 2017, Andrew Simon Davis took over A1 Company Services and became the Person with Significant Control. Prior to Andrew Davis' ownership, A1 Company Services was located at Finchley Road and helped criminals set up companies that were later disqualified for <a href="https://www.raphtory.com/A-Series-of-Unfortunate-Directors/" target="_blank">tax evasion, money laundering and political corruption scandals</a>. Many of Capital Nominees Limited companies were also found in the Panama Papers.

Andrew Davis was the CEO of Stanley Davis Group and was quoted in a <a href="https://www.hamhigh.co.uk/news/formation-agents-back-companies-house-overhaul-3638510" target="_blank">news article</a>: 
> "We have neither a legal nor a moral responsibility for the activities of the companies that we form."

However, he mentioned that where anti-money laundering or terrorist financing is suspected, A1 *and sister companies* carry out due diligence, reporting concerns to the National Crime Agency (NCA).

> *"Unfortunately,"* he said, *"their systems are not terribly satisfactory. The reports do not get acknowledged and just seem to disappear into a black hole.*
> 
> *"When we identify, for example, a fake passport, we report this to the NCA, to Action Fraud, to police and to the Passport Office. These reports are never acknowledged."*

After 20 years of working in the company formation industry, he sold the family business in 2020 and is now training to become a school teacher, with aspirations to "contribute and give back to society in a truly meaningful way."

## Company Formation Agents and the NHS
One of the directors of Company Nominees Limited, David Malcolm Kaye, is the CEO of <a href="https://thehackingtrust.com/" target="_blank">The Hacking Trust</a>, a property and business investor, specialising in companies with residential and commercial properties. 

In early 2021, the first Covid vaccines were being rolled out in the UK to those that were most vulnerable. Around this time, the Hacking Trust offered <a href="https://www.bbc.co.uk/news/uk-england-55593210" target="_blank">GP surgeries in Bristol and Worthing £5000 for unused coronavirus doses</a>. Furthermore, David Kaye had opened a company on Companies House under the name <a href="https://find-and-update.company-information.service.gov.uk/company/13113657" target="_blank">Wuhan Recovery 1 Ltd</a>. The nature of business was filed as "Buying and selling of own real estate". The company said they required around 20 doses of the vaccine.

The NHS said they received many such emails and clarified that hundreds of NHS teams across the country were "working hard to deliver vaccines quickly to those who would benefit most", adding that "NHS staff will never ask for, or accept cash for vaccines." The Department of Health and Social Care said vaccinations were available from the NHS "for free" and "cannot be sold privately in the UK".

At the start of the pandemic, healthcare workers across the country were risking their own and their families lives as they lacked basic PPE. With an increase in global demand for PPE, the government resorted to splurging huge amounts of money - fast tracking huge sums of money to company owners tied to MPs, just to provide PPE that did not meet the standard. £4 billion worth of PPE was reported as unused and 24% of NHS contracts are being <a href="https://committees.parliament.uk/committee/127/public-accounts-committee/news/171306/4-billion-of-unusable-ppe-bought-in-first-year-of-pandemic-will-be-burnt-to-generate-power/" target="_blank">investigated</a>. At Pometry, we used Raphtory to uncover the people behind these NHS contracts, looking at the date on which they were appointed as a person with significant control and their share of the company.

## The Chocolate NePPEtism Factory

We took each company number in the <a href="https://www.tussell.com/insights/covid" target="_blank">Tussell NHS Covid Contract data</a> and scraped the corresponding Persons With Significant Control (PSC) for these companies from the Companies House API, along with their date of birth, date of PSC appointment and more. We ran an algorithm in Raphtory that links companies that were awarded an NHS contract with their respective PSCs, showing the share of ownership and the time they were appointed as a PSC in that company. In addition to that, we linked all the PSCs in the same company together, creating a PSC network graph.

After a run of our data in Raphtory, a temporal network graph was created in less than a minute, with clearly labelled nodes displaying companies and people, along with the time at which these edges were created and the percentage of ownership that these people hold. This enabled us to quickly identify the people behind the companies awarded government money during the pandemic and their activity.

In one of the sub-graphs, we found several PSCs registered with the same surname- "Walker", all of which were linked to a company that was awarded money to provide PPE to the NHS. <a href="https://find-and-update.company-information.service.gov.uk/company/NI617785/persons-with-significant-control" target="_blank">Clandeboye Agencies Ltd</a> is the name of the company that received the contract. They are registered on Companies House as dealing with the "wholesale of sugar, chocolate and sugar confectionary". In total, Clandeboye were awarded £108m in PPE contracts and was also part of the government's VIP lane for companies with political connections.

Our output in Raphtory showed that Clady Group Ltd took control of 75% and more of Clandeboye Agencies Ltd on 15th of March 2022. On the Companies House website, <a href="https://find-and-update.company-information.service.gov.uk/company/NI683839/persons-with-significant-control" target="_blank">Clady Group Ltd</a> appointed 8 persons with significant control on the 3rd of April 2022, all of which registered with the surname "Walker", with the youngest being born in 2001. From the period of May to July of 2020, Clandeboye Agencies shipped millions of items such as thumb-looped gowns and aprons from a factory in Cambodia to an NHS warehouse in England. 

Months later, it was revealed in <a href="https://www.bbc.co.uk/iplayer/episode/m0012ljx/spotlight-covid-contracts-hunting-for-ppe" target="_blank">BBC NI's Spotlight programme</a> that boxes from the same shipment had not been used by the NHS, and a box of PPE worth £1000 was being sold online for just £5, rather than ending up in NHS warehouses to be distributed to hospitals across the country.

![]({{ site.baseurl }}/images/nhscontracts/ppebox.jpeg)

*Source: https://www.bbc.co.uk/news/uk-northern-ireland-59651994*

![]({{ site.baseurl }}/images/nhscontracts/clandeboye.png)

*Sub-graph showing the PSC to company relationships in Clandeboye Agencies Ltd*

![]({{ site.baseurl }}/images/nhscontracts/ownershipchain.png)
By mapping out the companies with their PSCs and their percentage of ownership in Raphtory, you can start to see where the money from NHS contracts is funneling down to. e.g. Patrick Byrne owns more than 50% of Pursuit Marketing Limited, but also owns more than 75% of Pursuit People Limited. The same pattern is seen in the other PSCs of these two companies.
![]({{ site.baseurl }}/images/nhscontracts/ownershipchain2.png)
Furthermore, complex network graphs become more clear when mapped out in Raphtory.
![]({{ site.baseurl }}/images/nhscontracts/complexownership.png)

Below is an interactive graph plotted with Pyvis showing company to PSC edges, with information on ownership and the date the PSC was notified on. You can zoom in and out, hover over edges and move nodes around.

<div>
{% include nhsPSCGraph.html %}
</div>

## Conclusions and Future Works

The Companies House API, together with the NHS contract data, has yet again provided us with fruitful insights into company activity and the people behind these companies. With Raphtory, we were able to identify who were the ultimate beneficiaries of the companies given government during the pandemic. 

In this article, we had a look at government spending in the NHS, especially during the pandemic. We are currently in the process of finding use cases with Raphtory in the health sector. Give us a follow on Linkedin or Twitter to keep up to date with our latest updates and blog articles.


# Interested in giving it a go yourself?

The basic version of this algorithm is available for free as part of the Raphtory Open Source Project. This can be run on any data you like as long as it fits the bipartite model described above.

If this is your first step into the world of temporal graphs, consider checking out the Introduction to Raphtory which will lead you into our Getting started guide. If you run into any issues you can get assistance from the wonderful Raphtory community on Slack.

If you would like to run these algorithms at scale in a production environment, drop the team at Pometry a message, and they will be more than happy to help.

