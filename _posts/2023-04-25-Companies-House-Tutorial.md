---
layout: coho
title:  "Using Raphtory to find fishy behaviour on Companies House 🎣"
categories:  [Analysis With Raphtory]
author: 'Rachel Chan'
excerpt: In this article we will show you how to use Raphtory to analyse Companies House data.
---

![]({{ site.baseurl }}/images/companieshouse/fishing-pom.png)
<br>

In the UK, requirements to register a new company are few. Practically anyone over the age of 16 years of age can own and manage a UK limited company. It only takes a few minutes to register a new company on <a href="https://www.gov.uk/limited-company-formation/register-your-company" target="_blank">Companies House</a>. This has brought about a rise in serial company formations and dissolutions by individuals. 
<br>
<br>
One example is a 92 year old woman named Barbara Kahan who has 22777 company appointments to her name, all of which are filed with an inconspicuous London address - 2 Woodberry Grove, London, N12 0DR. Little would one know that this leafy, suburban building was being used to register shell companies involved in fraud, money laundering and political corruption. 
<br>
<br>
With company formation agents advertising their services for as little as the price of two Mcdonald's Big Macs, the 3 hour company formation service has become an open door to criminal activity. Amidst the influx of new companies registering in the UK, it is hardly surprising that companies being formed for criminal purposes have gone unnoticed. More needs to be done to tackle this issue in the UK. 
<br>
<br>
![]({{ site.baseurl }}/images/companieshouse/detective-map.jpeg)
<br>
Fortunately, Raphtory can be used to capture the bad eggs amongst the hundreds and thousands of companies registering on UK land. Raphtory is a powerful analytics tool for large-scale graph analysis. With Raphtory, it takes a few seconds to turn Companies House data into insights on fishy behaviour going on with companies. 
<br>
<br>
In this blog, we will scrape information about all the companies that Barbara Kahan has been a director for and use Raphtory to analyse this data. Follow along with your own Python notebook of choice, as we unveil the dark secrets lying within UK's company registry.

## Follow along with our Jupyter Notebook

We have uploaded the full Jupyter notebook for this tutorial blog on our Github which you can find by clicking <a href="https://github.com/Pometry/Raphtory/blob/master/examples/py/companies_house/companies_house_example.ipynb" target="_blank">here</a>. Feel free to pull this example from Github or write up a fresh notebook in your local machine.

## How to collect Companies House Data

We are in luck as Companies House have provided a <a href="https://developer.company-information.service.gov.uk/overview" target="_blank">REST API</a>. At Pometry, we have built several crawlers that scrape the Companies House website, giving us direct access to the data we want. Currently, we have 3 crawlers: one made specifically to scrape Barbara Kahan's companies for this blog post and tutorial, another for grabbing Persons with Significant Control information and the last for grabbing Company Director information. All our crawlers output JSON data, ready to be loaded into a Raphtory graph for analysis. We have made this <a href="https://test.pypi.org/project/cohospider/" target="_blank">public via pip install</a> and explain how to use it below. 
<br>
<br>
![]({{ site.baseurl }}/images/companieshouse/pip-install-cohospider.png)

## How to use the Companies House crawler
### Getting your Companies House API key
Before scraping the Companies House website, you will need to create an account on the <a href="https://identity.company-information.service.gov.uk/user/register?request=eyJ0eXAiOiJKV0UiLCJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..k598Ksh5HW_W9cU7qz0IjQ.nRrBtC_ZKnw4i11POqeFUFxN-2Se8LGXZfhQlOviAZR7gTTIXJquoU81JzGiObTGjN9W1K-zR99AJmgNbf-OB28ErSI338UrAMD1uv1sCyWga_HGDroSqanv58zrsJ9Khq9tdv2vq3_o8rGDmg1bMtHifhKLMxAsdH4G9R0jR_YXRfeSIuJ9gsnwIttzF7rAp8W2HTxDI0dIDYzD6DchgGawElpUWXdgtx5WCcQmX17zlgYBzP9irJNv6xmQ5dwipKyAPLpe1dy5Apuk1UtIxNSfxFqURF2OIGbe3oum_49dtR8_y8_LkR0FhkhECS5lKZy4Am6mnwREpU78xkgd9ltIayfX4KvuRPKFii-gRdon7R0LTBUgYDasshLzMLdFWGNlmpgonH9NoB3wX8q_Dh2rShcjC6-jtGtcx2amCjLxR97yiWebxta7T0yuu5gJChtvyqRv8bkkQJYn9nq_3kBnZmasP6LPKcT9Ees3GkHGsWCVmeF24ZQzG77NnmqHd2n_LHP6wLIXdZodZhmVoKFUKA-EHnB5tRDcFFSneFx396Od02dBMZ0PKalvJ6F2PCEAH5nUO_6pnGJv3N9F-mMY8q6FPJ3qwKO1RUNfhEXosi2q9z3Rpq_MGft7FkQnV7x-hR9WD2ekJl2sNH0TYKwCEdtiy7B_bv9prnz74xaDsm7n10pPD18FIfUMT94hxDSarz3o4P0p0m6m07XYEo8t7BxlsxfLG0ImqrfQrYbC62n-1ZqVHJ84DKgPPMot_FwPqjwvv4fPcOcuw9lZZA.4YJgVfSsrNnmf5UOxf1qfQ" target="_blank">Companies House Developer Hub</a>:
<br>
<br>
![]({{ site.baseurl }}/images/companieshouse/register-account.png)

After logging into your account, create an application where your API keys will be stored:
<br>
<br>
![]({{ site.baseurl }}/images/companieshouse/create-an-application.png)

Once created, go into your application and create a new REST API key. This key will be used to authenticate your scrape requests:
<br>
<br>
![]({{ site.baseurl }}/images/companieshouse/create-new-key.png)
<br>
<br>
Make sure you select REST when creating your application:
<br>
<br>
![]({{ site.baseurl }}/images/companieshouse/create-new-key2.png)
<br>
<br>
Copy your API key which will be used to scrape Companies House website:
<br>
<br>
![]({{ site.baseurl }}/images/companieshouse/keys-for-application.png)
<br>
<br>
You are now ready to install the crawler and start scraping the Companies House website.
<br>
<br>

### Installing and running our Companies House crawler
![]({{ site.baseurl }}/images/companieshouse/animated-detective-searching-for-clues.gif)
*Install the crawler using pip*:
<br>
<br>
<div class="highlight">
<code-black>
pip install -i https://test.pypi.org/simple/ cohospider
</code-black>
</div>
<br>
*Go into a Python terminal and run the following code*:
<br>
<br>
<div class="highlight">
<code-black>
from spiders import BarbaraSpiderRun
</code-black>
</div>
<br>
<div class="highlight">
<code-black>
runner = BarbaraSpiderRun(key="YOUR API KEY HERE")
</code-black>
</div>
<br>
<div class="highlight">
<code-black>
runner.start()
</code-black>
</div>
<br>

Our crawler will start to scrape the Companies House API, finding all of Barbara's company data. Once finished, all your data can be found in the `data/aqWJlHS4_rJSJ7rLgTK49iO4gAg` folder in your root directory. We can now start the analysis using Raphtory.

## Analysing the data with Raphtory
![]({{ site.baseurl }}/images/companieshouse/analyse-data-python.jpeg)
*Install Raphtory via pip*:
<br>
<br>
<div class="highlight">
<code-black>
pip install raphtory
</code-black>
</div>
<br>
*Open a Python Terminal of your choice. We use Jupyter Notebook for this example. Import all the dependencies needed for this example*:
<br>
<br>
<div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">

<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>

<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">

<div class=" highlight hl-ipython3">
<pre>
<span></span><span class="kn">import</span> <span>os</span><span class="o">,</span> <span>json</span>
<span class="kn">import</span> <span>matplotlib.pyplot</span> <span class="k">as</span> <span>plt</span>
<span class="kn">from</span> <span>raphtory</span> <span class="kn">import</span> <span>Graph</span>
<span class="kn">from</span> <span>datetime</span> <span class="kn">import</span> <span>datetime</span>
<span class="kn">from</span> <span>raphtory</span> <span class="kn">import</span> <span>vis</span>
</pre>
</div>
</div>
</div>
</div>
</div>
</div>
<br>

We use the Python JSON library to parse the JSON files outputted from the crawler. Through this, we can create a Raphtory graph and add our values to the graph via the `add_edge()` function.

<br>
*Enter the directory path to your json files inside the `path_to_json` variable. It should look something like this: `~/companies_house_scraper/tutorial/data/aqWJlHS4_rJSJ7rLgTK49iO4gAg`*: 
<br>
<br>
<div  class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span>path_to_json</span> <span class="o">=</span> <span class="s1">&#39;&#39;</span>
<span>json_files</span> <span class="o">=</span> <span class="p">[</span><span>pos_json</span> <span class="k">for</span> <span>pos_json</span> <span class="ow">in</span> <span>os</span><span class="o">.</span><span>listdir</span><span class="p">(</span><span>path_to_json</span><span class="p">)</span> <span class="k">if</span> <span>pos_json</span><span class="o">.</span><span>endswith</span><span class="p">(</span><span class="s1">&#39;.json&#39;</span><span class="p">)]</span>
</pre></div>
</div>
</div>
</div>
</div>
<br>

<em>Create a Raphtory graph</em>:
<br>
<br>
<div  class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span>g</span> <span class="o">=</span> <span>Graph</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>
</div>

</div>
</div>
<br>
*Iterate through all the JSON files (there are many files since the crawler works by crawling page by page) and add values to your Raphtory graph via `add_edge()` function*:
<br>
<br>
<div  class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">for</span> <span>index</span><span class="p">,</span> <span>js</span> <span class="ow">in</span> <span>enumerate</span><span class="p">(</span><span>json_files</span><span class="p">):</span>
    <span class="k">with</span> <span>open</span><span class="p">(</span><span>os</span><span class="o">.</span><span>path</span><span class="o">.</span><span>join</span><span class="p">(</span><span>path_to_json</span><span class="p">,</span> <span>js</span><span class="p">))</span> <span class="k">as</span> <span>json_file</span><span class="p">:</span>
        <span>json_text</span> <span class="o">=</span> <span>json</span><span class="o">.</span><span>load</span><span class="p">(</span><span>json_file</span><span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">for</span> <span>item</span> <span class="ow">in</span> <span>json_text</span><span class="p">[</span><span class="s1">&#39;items&#39;</span><span class="p">]:</span>
                <span>appointed_on</span> <span class="o">=</span> <span>item</span><span class="p">[</span><span class="s1">&#39;appointed_on&#39;</span><span class="p">]</span>
                <span>resigned_on</span> <span class="o">=</span> <span>datetime</span><span class="o">.</span><span>datetime</span><span class="o">.</span><span>strptime</span><span class="p">(</span><span>item</span><span class="p">[</span><span class="s1">&#39;resigned_on&#39;</span><span class="p">],</span> <span class="s2">&quot;%Y-%m-</span><span class="si">%d</span><span class="s2">&quot;</span><span class="p">)</span>
                <span>resigned_on_string</span> <span class="o">=</span> <span>str</span><span class="p">(</span><span>resigned_on</span><span class="p">)</span>
                <span>epoch_resigned</span> <span class="o">=</span> <span>int</span><span class="p">(</span><span>datetime</span><span class="o">.</span><span>datetime</span><span class="o">.</span><span>timestamp</span><span class="p">(</span><span>resigned_on</span><span class="p">))</span> <span class="o">*</span> <span class="mi">1000</span>
                <span>company_name</span> <span class="o">=</span> <span>item</span><span class="p">[</span><span class="s1">&#39;appointed_to&#39;</span><span class="p">][</span><span class="s1">&#39;company_name&#39;</span><span class="p">]</span>
                <span>director_name</span> <span class="o">=</span> <span>item</span><span class="p">[</span><span class="s1">&#39;name&#39;</span><span class="p">]</span>

                <span>g</span><span class="o">.</span><span>add_edge</span><span class="p">(</span><span>appointed_on</span><span class="p">,</span> <span>director_name</span><span class="p">,</span> <span>company_name</span><span class="p">,</span> <span class="p">{</span><span class="s1">&#39;resigned_on&#39;</span><span class="p">:</span> <span>resigned_on_string</span><span class="p">,</span> <span class="s1">&#39;epoch_resigned&#39;</span><span class="p">:</span> <span>epoch_resigned</span><span class="p">})</span>

        <span class="k">except</span> <span>KeyError</span> <span class="k">as</span> <span>e</span><span class="p">:</span>
            <span>print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;key </span><span class="si">{</span><span>e</span><span class="si">}</span><span class="s2"> not found in json block&quot;</span><span class="p">)</span>
        <span class="k">except</span> <span>Exception</span> <span class="k">as</span> <span>e</span><span class="p">:</span>
            <span>print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span>e</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>
</div>

</div>

### Quick overview of Barbara's companies using Raphtory

With the Raphtory API, we can quickly find statistics from our data about Barbara's company ownership history.
<br>
<br>
![]({{ site.baseurl }}/images/companieshouse/boardroom.jpeg)
*Create a list of director names to see how many different names the director goes by:*
<br>
<br>
<div  class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span>list_of_src</span><span class="o">=</span> <span class="p">[]</span>

<span class="k">for</span> <span>e</span> <span class="ow">in</span> <span>g</span><span class="o">.</span><span>edges</span><span class="p">():</span>
   <span>list_of_src</span><span class="o">.</span><span>append</span><span class="p">(</span><span>e</span><span class="o">.</span><span>src</span><span class="p">()</span><span class="o">.</span><span>name</span><span class="p">())</span>

<span>print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;List of director names: </span><span class="si">{</span><span>set</span><span class="p">(</span><span>list_of_src</span><span class="p">)</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
    
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>List of director names: {&#39;Barbara Z KAHAN&#39;, &#39;Barbara KAHAN&#39;}
</pre>
</div>
</div>

</div>

</div>

</div>
<br>
*Finding the number of companies formed by the director:*
<br>
<br>
<div  class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span>print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Number of companies director assigned to: </span><span class="si">{</span><span>g</span><span class="o">.</span><span>num_edges</span><span class="p">()</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>Number of companies director assigned to: 22305
</pre>
</div>
</div>

</div>

</div>

</div>
<br>

*Seeing the earliest and latest company formations this director has made:*
<br>
<br>
<div  class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span>earliest_date</span> <span class="o">=</span> <span>datetime</span><span class="o">.</span><span>datetime</span><span class="o">.</span><span>fromtimestamp</span><span class="p">(</span><span>g</span><span class="o">.</span><span>earliest_time</span><span class="p">()</span><span class="o">/</span><span class="mi">1000</span><span class="p">)</span>
<span>latest_date</span> <span class="o">=</span> <span>datetime</span><span class="o">.</span><span>datetime</span><span class="o">.</span><span>fromtimestamp</span><span class="p">(</span><span>g</span><span class="o">.</span><span>latest_time</span><span class="p">()</span><span class="o">/</span><span class="mi">1000</span><span class="p">)</span>

<span>print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Earliest date director was assigned to company: </span><span class="si">{</span><span>earliest_date</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
<span>print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Latest date director was assigned to company: </span><span class="si">{</span><span>latest_date</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>Earliest date director was assigned to company: 2002-01-14 00:00:00
Latest date director was assigned to company: 2016-02-16 00:00:00
</pre>
</div>
</div>

</div>

</div>

</div>
<br>

There are a plethora of methods in the Raphtory API that give you an overview about your graph data. These are just a few to demonstrate how easy it is to access this information with Raphtory.

### Using Raphtory properties to filter suspicious companies

The date that the director resigned from the company can be accessed via the edge <b>property</b>. This is the API for adding properties to edges in Raphtory:
<br>
<br>
<code-black>
g.add_edge(time, source, target, {'property_name': property_value})
</code-black>
<br>
<br>
It is possible to have an <b>infinite number</b> of properties on edges and vertices in Raphtory to store extra information. However, we have kept it simple for this example. Properties in Raphtory have enabled us to store the resignation date in two formats - date time format and epoch timestamp format.
<br>
<br>

![]({{ site.baseurl }}/images/companieshouse/Closed-out-of-business.jpeg)

<br>

It would be unusual if a Company Formation Agent helped their client set up a company and stayed on as director, as opposed to immediately handing the director title to the client. This can be indication of a criminal using the company formation agent as a front for their dishonest activities.

<br>
![]({{ site.baseurl }}/images/companieshouse/offshore-companies.png)
<br>
<br>
<div  class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span>sus_companies</span> <span class="o">=</span> <span class="p">[]</span>

<span class="k">for</span> <span>edge</span> <span class="ow">in</span> <span>g</span><span class="o">.</span><span>vertex</span><span class="p">(</span><span class="s1">&#39;Barbara KAHAN&#39;</span><span class="p">)</span><span class="o">.</span><span>edges</span><span class="p">():</span>
    <span class="k">if</span> <span class="p">(</span><span>edge</span><span class="o">.</span><span>property</span><span class="p">(</span><span class="s2">&quot;epoch_resigned&quot;</span><span class="p">)</span> <span class="o">-</span> <span>edge</span><span class="o">.</span><span>earliest_time</span><span class="p">())</span> <span class="o">&gt;</span> <span class="mi">31557600000</span><span class="p">:</span>
       <span>sus_companies</span><span class="o">.</span><span>append</span><span class="p">(</span><span>edge</span><span class="p">)</span>
       
<span>print</span><span class="p">(</span><span>sus_companies</span><span class="o">.</span><span>__len__</span><span class="p">())</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>859
</pre>
</div>
</div>

</div>

</div>

</div>
<br>

As you can see from the above code snippet, Barbara had stayed on at 859 companies for longer than one year. Let's delve deeper into when these companies were created and exactly who these companies belonged to.

### Create a line plot visualisation over time with Raphtory

![]({{ site.baseurl }}/images/companieshouse/rolling_line_chart.gif)

We can use a function in Raphtory called `.rolling()` with a window size of 10000000000 milliseconds (around 4 months). This enables us to "roll" through all the windows/views, counting the number of companies the director was assigned to over time.
<br>
<br>

*Roll through the graph with a window of 10000000000 milliseconds:*

<div  class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre>
<span>views</span> <span class="o">=</span> <span>g</span><span class="o">.</span><span>rolling</span><span class="p">(</span><span>10000000000</span><span class="p">)</span> 
</pre></div>

     </div>
</div>
</div>
</div>

</div>
<br>
*For each view, count the number of edges:*

<div  class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span>timestamps</span>   <span class="o">=</span> <span class="p">[]</span>
<span>edge_count</span>   <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span>view</span> <span class="ow">in</span> <span>views</span><span class="p">:</span>
    <span>time</span> <span class="o">=</span> <span>datetime</span><span class="o">.</span><span>fromtimestamp</span><span class="p">(</span><span>view</span><span class="o">.</span><span>latest_time</span><span class="p">())</span>
    <span>timestamps</span><span class="o">.</span><span>append</span><span class="p">(</span><span>time</span><span class="p">)</span>
    <span>edge_count</span><span class="o">.</span><span>append</span><span class="p">(</span><span>view</span><span class="o">.</span><span>num_edges</span><span class="p">())</span>            
</pre></div>

     </div>
</div>
</div>
</div>

</div>
<br>
*Create the line plot visualisation with the Seaborn library:*

<div  class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span>sns</span><span class="o">.</span><span>set_context</span><span class="p">()</span>
<span>ax</span> <span class="o">=</span> <span>plt</span><span class="o">.</span><span>gca</span><span class="p">()</span>
<span>plt</span><span class="o">.</span><span>xticks</span><span class="p">(</span><span>rotation</span><span class="o">=</span><span class="mi">45</span><span class="p">)</span>
<span>ax</span><span class="o">.</span><span>set_xlabel</span><span class="p">(</span><span class="s2">&quot;Time&quot;</span><span class="p">)</span>
<span>ax</span><span class="o">.</span><span>set_ylabel</span><span class="p">(</span><span class="s2">&quot;Companies Created&quot;</span><span class="p">)</span>
<span>sns</span><span class="o">.</span><span>lineplot</span><span class="p">(</span><span>x</span> <span class="o">=</span> <span>timestamps</span><span class="p">,</span> <span>y</span> <span class="o">=</span> <span>edge_count</span><span class="p">,</span><span>ax</span><span class="o">=</span><span>ax</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[&nbsp;]:</div>




<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
<pre>&lt;Axes: xlabel=&#39;Time&#39;, ylabel=&#39;Companies Created&#39;&gt;</pre>
</div>

</div>
<div class="jp-OutputArea-child">
    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>




<div class="jp-RenderedImage jp-OutputArea-output ">
<img src="data:image/png;base64,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"
class="
"
>
</div>

</div>

</div>

</div>

</div>

Now that we can see several spikes in our graph, especially between 2012 and 2016, we can further investigate this window of time.

### Using windows to filter particular timepoints of interest

One of the spikes in the line plot above is at year 2014. To investigate this further we use the `.window()` function which takes a start and end time. We will look at a window of 01-01-2014 to 01-01-2015.

<div  class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span>filtered_view</span> <span class="o">=</span> <span>g</span><span class="o">.</span><span>window</span><span class="p">(</span><span class="mi">1388534400000</span><span class="p">,</span> <span class="mi">1400070400000</span><span class="p">)</span>
<span>filtered_views</span> <span class="o">=</span> <span>filtered_view</span><span class="o">.</span><span>rolling</span><span class="p">(</span><span class="mi">100000000</span><span class="p">)</span>
<span>timestamps</span>   <span class="o">=</span> <span class="p">[]</span>
<span>edge_count</span>   <span class="o">=</span> <span class="p">[]</span>

<span class="k">for</span> <span>filtered_view</span> <span class="ow">in</span> <span>filtered_views</span><span class="p">:</span>
    <span>time</span> <span class="o">=</span> <span>datetime</span><span class="o">.</span><span>datetime</span><span class="o">.</span><span>fromtimestamp</span><span class="p">(</span><span>filtered_view</span><span class="o">.</span><span>latest_time</span><span class="p">()</span><span class="o">/</span><span class="mi">1000</span><span class="p">)</span>
    <span>timestamps</span><span class="o">.</span><span>append</span><span class="p">(</span><span>time</span><span class="p">)</span>
    <span>edge_count</span><span class="o">.</span><span>append</span><span class="p">(</span><span>filtered_view</span><span class="o">.</span><span>num_edges</span><span class="p">())</span>            

<span>sns</span><span class="o">.</span><span>set_context</span><span class="p">()</span>
<span>ax</span> <span class="o">=</span> <span>plt</span><span class="o">.</span><span>gca</span><span class="p">()</span>
<span>plt</span><span class="o">.</span><span>xticks</span><span class="p">(</span><span>rotation</span><span class="o">=</span><span class="mi">45</span><span class="p">)</span>
<span>ax</span><span class="o">.</span><span>set_xlabel</span><span class="p">(</span><span class="s2">&quot;Time&quot;</span><span class="p">)</span>
<span>ax</span><span class="o">.</span><span>set_ylabel</span><span class="p">(</span><span class="s2">&quot;Companies Created&quot;</span><span class="p">)</span>
<span>sns</span><span class="o">.</span><span>lineplot</span><span class="p">(</span><span>x</span> <span class="o">=</span> <span>timestamps</span><span class="p">,</span> <span>y</span> <span class="o">=</span> <span>edge_count</span><span class="p">,</span><span>ax</span><span class="o">=</span><span>ax</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[&nbsp;]:</div>




<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
<pre>&lt;Axes: xlabel=&#39;Time&#39;, ylabel=&#39;Companies Created&#39;&gt;</pre>
</div>

</div>
<div class="jp-OutputArea-child">
    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>




<div class="jp-RenderedImage jp-OutputArea-output ">
<img src="data:image/png;base64,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"
class="
"
>
</div>

</div>

</div>

</div>

</div>

There seems to be a spike between 2014-02-01 to 2014-02-15. We create a window for this spike to investigate further.

<div  class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span>filtered_view2</span> <span class="o">=</span> <span>g</span><span class="o">.</span><span>window</span><span class="p">(</span><span class="mi">1391212800000</span><span class="p">,</span> <span class="mi">1392422400000</span><span class="p">)</span>
<span>filtered_views2</span> <span class="o">=</span> <span>filtered_view2</span><span class="o">.</span><span>rolling</span><span class="p">(</span><span>window</span><span class="o">=</span><span class="mi">10000000</span><span class="p">)</span> 
<span>timestamps</span>   <span class="o">=</span> <span class="p">[]</span>
<span>edge_count</span>   <span class="o">=</span> <span class="p">[]</span>

<span class="k">for</span> <span>filtered_view2</span> <span class="ow">in</span> <span>filtered_views2</span><span class="p">:</span>
    <span>time</span> <span class="o">=</span> <span>datetime</span><span class="o">.</span><span>datetime</span><span class="o">.</span><span>fromtimestamp</span><span class="p">(</span><span>filtered_view2</span><span class="o">.</span><span>latest_time</span><span class="p">()</span><span class="o">/</span><span class="mi">1000</span><span class="p">)</span>
    <span>timestamps</span><span class="o">.</span><span>append</span><span class="p">(</span><span>time</span><span class="p">)</span>
    <span>edge_count</span><span class="o">.</span><span>append</span><span class="p">(</span><span>filtered_view2</span><span class="o">.</span><span>num_edges</span><span class="p">())</span>            

<span>sns</span><span class="o">.</span><span>set_context</span><span class="p">()</span>
<span>ax</span> <span class="o">=</span> <span>plt</span><span class="o">.</span><span>gca</span><span class="p">()</span>
<span>plt</span><span class="o">.</span><span>xticks</span><span class="p">(</span><span>rotation</span><span class="o">=</span><span class="mi">45</span><span class="p">)</span>
<span>ax</span><span class="o">.</span><span>set_xlabel</span><span class="p">(</span><span class="s2">&quot;Time&quot;</span><span class="p">)</span>
<span>ax</span><span class="o">.</span><span>set_ylabel</span><span class="p">(</span><span class="s2">&quot;Companies Created&quot;</span><span class="p">)</span>
<span>sns</span><span class="o">.</span><span>lineplot</span><span class="p">(</span><span>x</span> <span class="o">=</span> <span>timestamps</span><span class="p">,</span> <span>y</span> <span class="o">=</span> <span>edge_count</span><span class="p">,</span><span>ax</span><span class="o">=</span><span>ax</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[&nbsp;]:</div>




<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
<pre>&lt;Axes: xlabel=&#39;Time&#39;, ylabel=&#39;Companies Created&#39;&gt;</pre>
</div>

</div>
<div class="jp-OutputArea-child">
    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>




<div class="jp-RenderedImage jp-OutputArea-output ">
<img src="data:image/png;base64,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"
class="
"
>
</div>

</div>

</div>

</div>

</div>
There is a big spike on 2014-02-11 and 2014-02-12. Now that we have specific time points, we can find out the names of the companies in these spikes by visualising the edges of the graph at these time points.

### Dynamic visualisation of your graph in Raphtory

To visualise specific dates, we first create a window which includes the time point we want. Below, we have created a window that only includes the date 2014-02-12. We then filter for edges where the company formation agent (Barbara) has stayed as director at the company for longer than a year. Lastly, we use Raphtory's `.to_pyvis()` function to create a dynamic visualisation of the edges. In this way, we can clearly see the companies where the company formation agent has stayed as director for longer than a year.

<br>
<div  class="jp-Cell jp-CodeCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span>sus_companies</span> <span class="o">=</span> <span class="p">[]</span>
<span>twelfth_of_feb</span> <span class="o">=</span> <span>g</span><span class="o">.</span><span>window</span><span class="p">(</span><span class="mi">1391212800000</span><span class="p">,</span> <span class="mi">1392422400000</span><span class="p">)</span>
<span class="k">for</span> <span>edge</span> <span class="ow">in</span> <span>twelfth_of_feb</span><span class="o">.</span><span>vertex</span><span class="p">(</span><span class="s1">&#39;Barbara KAHAN&#39;</span><span class="p">)</span><span class="o">.</span><span>edges</span><span class="p">():</span>
    <span class="k">if</span> <span class="p">(</span><span>edge</span><span class="o">.</span><span>property</span><span class="p">(</span><span class="s2">&quot;epoch_resigned&quot;</span><span class="p">)</span> <span class="o">-</span> <span>edge</span><span class="o">.</span><span>earliest_time</span><span class="p">())</span> <span class="o">&gt;</span> <span class="mi">157784630000</span><span class="p">:</span>
       <span>sus_companies</span><span class="o">.</span><span>append</span><span class="p">(</span><span>edge</span><span class="p">)</span>
<span>g2</span> <span class="o">=</span> <span>Graph</span><span class="p">()</span>
<span class="k">for</span> <span>edge</span> <span class="ow">in</span> <span>sus_companies</span><span class="p">:</span>
    <span>g2</span><span class="o">.</span><span>add_edge</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span>edge</span><span class="o">.</span><span>src</span><span class="p">()</span><span class="o">.</span><span>name</span><span class="p">(),</span> <span>edge</span><span class="o">.</span><span>dst</span><span class="p">()</span><span class="o">.</span><span>name</span><span class="p">())</span>
<span>print</span><span class="p">(</span><span>sus_companies</span><span class="o">.</span><span>__len__</span><span class="p">())</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>263
</pre>
</div>
</div>

</div>

</div>

</div>

<div  class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span>vis</span><span class="o">.</span><span>to_pyvis</span><span class="p">(</span><span>graph</span><span class="o">=</span><span>g2</span><span class="p">,</span> <span>edge_color</span><span class="o">=</span><span class="s1">&#39;#F6E1D3&#39;</span><span class="p">,</span><span>shape</span><span class="o">=</span><span class="s2">&quot;image&quot;</span><span class="p">)</span>  
</pre></div>

     </div>
</div>
</div>
</div>
</div>
The visualisation will appear in a file called `nx.html` which can be opened in a web browser.
<br>
<br>

*A screenshot of the dynamic visualisation*
![]({{ site.baseurl }}/images/companieshouse/barbara_kahan.png)
<br>
If you would like your graph in a list of vertices and edges, you can call methods such as `.vertices()` and `.edges()`.
<div  class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span>twelfth_of_feb</span><span class="o">.</span><span>vertices</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[&nbsp;]:</div>




<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
<pre>Vertices(Vertex(name=Barbara KAHAN, properties={_id : Barbara KAHAN}), Vertex(name=JYNUX SYSTEMS LIMITED, properties={_id : JYNUX SYSTEMS LIMITED}), Vertex(name=SIRTRECH LIMITED, properties={_id : SIRTRECH LIMITED}), Vertex(name=HOTSOUND LIMITED, properties={_id : HOTSOUND LIMITED}), Vertex(name=HAXMED LIMITED, properties={_id : HAXMED LIMITED}), Vertex(name=NITESYS LIMITED, properties={_id : NITESYS LIMITED}), Vertex(name=HYPERMANAGE LIMITED, properties={_id : HYPERMANAGE LIMITED}), Vertex(name=LYNXMECH LIMITED, properties={_id : LYNXMECH LIMITED}), Vertex(name=SISTEMON LIMITED, properties={_id : SISTEMON LIMITED}), Vertex(name=GINDOLA TRADERS LIMITED, properties={_id : GINDOLA TRADERS LIMITED}), ...)</pre>
</div>

</div>

</div>

</div>

</div><div  class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span>twelfth_of_feb</span><span class="o">.</span><span>edges</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
    
<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[&nbsp;]:</div>


<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
<pre>Edges(Edge(source=Barbara KAHAN, target=JYNUX SYSTEMS LIMITED, earliest_time=1392163200, latest_time=1392163200, properties={resigned_on : 1499122800}), Edge(source=Barbara KAHAN, target=SIRTRECH LIMITED, earliest_time=1392163200, latest_time=1392163200, properties={resigned_on : 1423785600}), Edge(source=Barbara KAHAN, target=HOTSOUND LIMITED, earliest_time=1392163200, latest_time=1392163200, properties={resigned_on : 1525215600}), Edge(source=Barbara KAHAN, target=HAXMED LIMITED, earliest_time=1392163200, latest_time=1392163200, properties={resigned_on : 1411686000}), Edge(source=Barbara KAHAN, target=NITESYS LIMITED, earliest_time=1392163200, latest_time=1392163200, properties={resigned_on : 1585522800}), Edge(source=Barbara KAHAN, target=HYPERMANAGE LIMITED, earliest_time=1392163200, latest_time=1392163200, properties={resigned_on : 1457308800}), Edge(source=Barbara KAHAN, target=LYNXMECH LIMITED, earliest_time=1392163200, latest_time=1392163200, properties={resigned_on : 1457308800}), Edge(source=Barbara KAHAN, target=SISTEMON LIMITED, earliest_time=1392163200, latest_time=1392163200, properties={resigned_on : 1445817600}), Edge(source=Barbara KAHAN, target=GINDOLA TRADERS LIMITED, earliest_time=1392163200, latest_time=1392163200, properties={resigned_on : 1565132400}), Edge(source=Barbara KAHAN, target=GINDENE LIMITED, earliest_time=1392163200, latest_time=1392163200, properties={resigned_on : 1410908400}), ...)</pre>
</div>

</div>

</div>

</div>

</div>
<br>
<br>

In just a few minutes, we have transformed billions of company data into interesting insights on potential fishy behaviour. 
<br>
<br>
Temporally analysing data has been difficult in the past, however Raphtory makes it incredibly easy. Rather than looking at data in a static manner, taking into account of time can give us better understanding on our data that may be beneficial to your unique use cases. 
<br>
<br>
If you would like to run further analysis and algorithms at scale in a production environment, drop the team at <a href="https://www.pometry.com/contact/" target="_blank">Pometry</a> a message, and they will be more than happy to help.


<br>
<br>