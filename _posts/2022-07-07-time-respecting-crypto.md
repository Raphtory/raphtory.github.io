---
layout: post
title: "Tracking illicit cryptocurrency across time"
categories: [Use Case]
author: Ben Steer
---

## Where does all the money go? 

Ignoring the current down turn, [decentralised finance (DeFi)](https://www.forbes.com/advisor/investing/cryptocurrency/defi-decentralized-finance/) holds many exciting opportunities, from removing barriers to the global market for individuals in [less developed countries](https://www.voanews.com/a/africa_cryptocurrency-booming-among-kenyan-farmers/6208732.html), to aiding in the fight against [authoritarian dictatorships](https://bitcoinmagazine.com/culture/bitcoin-is-a-trojan-horse-for-freedom). Unfortunately, Crypto markets often attract criminals attempting to launder the proceeds of their illicit real-world activities or who are carrying out attacks directly on these markets. The impact for this is eye watering with money laundering costing the UK over [£100 billion a year](https://www.gartner.com/en/newsroom/press-releases/2021-03-16-gartner-identifies-top-10-data-and-analytics-technologies-trends-for-2021) and cryptocurrency crime in 2020 costing around [$10 billion](https://www.nationalcrimeagency.gov.uk/news/national-economic-crime-centre-leads-push-to-identify-money-laundering-activity). 

Secondly, while we have seen a massive boom in Crypto startups, with the onset of regulations into the market, many UK cryptocurrency firms still do not meet FCA anti-money laundering (AML) regulations and [almost 150 risk closure](https://www.reuters.com/world/uk/uk-regulator-says-cryptoasset-firms-not-meeting-anti-money-laundering-rules-2021-06-03/). Other jurisdictions are already beginning to introduce similar legislation, so this problem is only going to get worse. 

Many companies have been spawned to tackle this problem, building tools to track these activities and countering the measures criminals take to hide behind a web of seemly innocuous transactions. Notably in this space are [Chainalysis](https://www.chainalysis.com) and [Elliptic](https://www.elliptic.co) for compliance in standard cyptoassets and newer groups such [Flash bots](https://explore.flashbots.net) attempting to democratise trading activities.

However, techniques to hide the origin of money are continuously becoming more advanced, spreading the currencies over millions of transactions across thousands of wallets, to which current countermeasures are struggling to keep up. An example of this is the [$100 million stolen from Harmony](https://cointelegraph.com/news/harmony-hacker-sends-stolen-funds-to-tornado-cash-mixer) and quickly distributed via the [Tornado mixer](https://tornado.cash), leaving little hope of recovery.

This means after a certain amount of time, to an exchange or vendor accepting Crypto, the funds will appear legitimate and can be accepted. Once transferred into fiat the criminals can disappear and the business who had the displeasure of dealing with them is held accountable to the authorities when they eventually catch up.

![]({{site.baseurl}}/images/tainttracking/hacker.png)
*Example network of stolen money spreading from the initial source wallet through to exchanges and shops, allowing it to be converted into real-world goods.*


## Let's define the problem to solve
As can be seen from the above figure, sets of transactions (whether Crypto or Fiat) form a network where the individuals (or wallets) are the nodes, while transactions between two nodes form an edge. The problem to solve, therefore, is to start at the known `bad actors` and follow the flow of money, `tainting` every wallet we reach quick enough so that exchanges and vendors know not to accept money from them. 

If we do, unfortunately, discover an exchange/vendor along this path, we can contact them and inform them of who they were doing business with, so they can hand over any details to the authorities. This will end the tainting process for this individual money flow as assuming the vendor is legitimate we shouldn't taint their other customers!

In practice this is not so simple. Executing this naively (i.e. following all transactions) will lead us to exponentially more wallets with each `hop` we travel away from the initial `bad actors`; quickly becoming computationally intractable. This is made worse if the transactions loop back round to an earlier wallet, creating a cycle, as the algorithm can get permanently stuck looping round. 

The only standard solutions to this is to put on a `hop` limit (normally 6 to 20) or track the full path so far (checking if we have seen a wallet before). The first massively limits the depth to which we can follow the money and the latter makes the algorithm blow up even quicker!  

## What's the solution?
You may be surprised to hear, given the blog this is on, the solution is to use Raphtory! By adding a time dimension to our model there are many improvements we can make to the standard algorithm which make it run much faster and provide a more accurate result.

The general principle here is that instead of following all transactions made by a tainted wallet, we only follow those which occur after the `bad` transaction we arrived at. For example, given the graph below, the wallet in the middle received tainted funds on Tuesday at 5pm. If we propagated this forward along all transactions, all 4 downstream wallets would be affected. Instead, we only taint those interacting with the wallet after Tuesday at 5pm, meaning the exchange at the top and wallet at the bottom would be considered safe. 

![]({{site.baseurl}}/images/tainttracking/taint.png)
*An example transactional network where the wallet in the middle has received funds from a known bad actor. Tainted nodes are represented in `Red`, untainted in `White`.*

Scaling this up, if we reach a wallet with many thousands of transactions, but only a couple after the arrival time, we massively shrink the amount of wallets we infect, subduing the exponential explosion and increasing how far we can follow the money. This also provides a more accurate view of where this particular money is going, as per the [legal requirements of tracking illicit transactions](https://www.repository.cam.ac.uk/bitstream/handle/1810/287807/WEIS_2018_paper_38.pdf?sequence=1&isAllowed=y). In this instance utilising a diffusion process similar to First In First Out (`FIFO`).

Furthermore, as we are always moving forward in time we can no longer get stuck in cycles! Each time we reappear at the same wallet we can leave on fewer outbound transactions, this can only continue at most until we reach the present time as otherwise we would be considering future transactions :crystal_ball:. 

## Testing this out on the entire Bitcoin network 
This all sounds very exciting, but does it actually work in practice? To test this we set up a Raphtory instance on AWS (run on a `x2iedn.2xlarge` for those interested in specs) to ingest the full bitcoin network right up until the present day. We then run the above algorithm under different conditions to see the result. 

As a side note, **ingestion was completed in under 50 minutes** and once converted into Raphtory's internal format could be **loaded back off disk in under 1 minute!**

The first test conducted took 30 million randomly selected wallets and set them as `bad actors` at equally random times. The algorithm was then set running from these in parallel, **converging in just 7 minutes!** A query of this type would normally take several hours, if it finished at all. The deepest path found was **over 690 hops away**, much further than the standard 20!

Expanding on this we took a wallet owned by a large exchange which has existed since the very beginning of Bitcoin. This wallet has hundreds of thousands of transactions going back over 14 years. We run the algorithm, setting this as our `bad actor` from the beginning of time. This followed all of these transactions, **converging in just 400 seconds**, and returning paths over **a staggering 31,000 hops away**, right up until the present day!
 
 This effectively means that **any** stolen bitcoins can be **tracked forever** with the authorities hot on the heels of those committing the crime! 

## Interested in giving it a go yourself?
The basic version of this algorithm is [available](https://github.com/Raphtory/Raphtory/blob/master/core/src/main/scala/com/raphtory/algorithms/temporal/dynamic/GenericTaint.scala) for free as part of the [Raphtory Open Source Project](https://github.com/Raphtory/Raphtory). This can be run on any data you like. This is a binary tainting algorithm (you're either a bad guy or not), but can be easily modified for [other models of diffusion](https://www.repository.cam.ac.uk/bitstream/handle/1810/287807/WEIS_2018_paper_38.pdf?sequence=1&isAllowed=y). 

If this is your first step into the world of temporal graphs, consider checking out the [Introduction to Raphtory](https://www.raphtory.com/about) which will lead you into our [Getting started guide](https://docs.raphtory.com). If you run into any issues you can get assistance from the wonderful Raphtory community on [Slack](https://join.slack.com/t/raphtory/shared_invite/zt-xbebws9j-VgPIFRleJFJBwmpf81tvxA).

If you would like to run these algorithms at scale in a production environment, drop the team at [Pometry](https://www.pometry.com/contact/) a message, and they will be more than happy to help. 