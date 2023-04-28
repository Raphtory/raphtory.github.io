---
layout: coho
title:  "Using Raphtory to find fishy behaviour on Companies House 🎣"
categories:  [Analysis With Raphtory]
author: 'Rachel Chan'
excerpt: In this article we will show you how to use Raphtory to analyse Companies House data.
---
<br>
<br>
![]({{ site.baseurl }}/images/companieshouse/fish-image.png)

<br>
<br>
It takes a few minutes to register a new company on <a href="https://www.gov.uk/limited-company-formation/register-your-company" target="_blank">Companies House</a>. This has given rise to serial company formations and dissolutions by individuals. With so many companies being formed over time, it can be hard to track which individuals are linked to which companies. 

Raphtory is a powerful analytics engine for large-scale graph analysis. Using Raphtory, it takes a few seconds to turn Companies House data into insights on fishy behaviour going on with companies. In this blog, we will show you exactly how to do that.

## Data Collection

We are in luck as Companies House have provided a <a href="https://developer.company-information.service.gov.uk/overview" target="_blank">REST API</a>. At Pometry, we built several Companies House scrapers, utilising the API and giving us direct access to the data we want. Currently, we have 3 scrapers: the first being specifically for this blog post and example, the second is for grabbing Persons with Significant Control from company numbers and the last is for grabbing Directors from company numbers. All our scrapers output JSON data, ready to be loaded into a Raphtory graph for analysis. We have made this <a href="https://test.pypi.org/project/cohospider/" target="_blank">public via pip install</a> and explain how to use it below. 

## How to use the Companies House Scraper
### Getting your Companies House API key
Before scraping the Companies House website, you will need to create an account on the <a href="https://identity.company-information.service.gov.uk/user/register?request=eyJ0eXAiOiJKV0UiLCJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..k598Ksh5HW_W9cU7qz0IjQ.nRrBtC_ZKnw4i11POqeFUFxN-2Se8LGXZfhQlOviAZR7gTTIXJquoU81JzGiObTGjN9W1K-zR99AJmgNbf-OB28ErSI338UrAMD1uv1sCyWga_HGDroSqanv58zrsJ9Khq9tdv2vq3_o8rGDmg1bMtHifhKLMxAsdH4G9R0jR_YXRfeSIuJ9gsnwIttzF7rAp8W2HTxDI0dIDYzD6DchgGawElpUWXdgtx5WCcQmX17zlgYBzP9irJNv6xmQ5dwipKyAPLpe1dy5Apuk1UtIxNSfxFqURF2OIGbe3oum_49dtR8_y8_LkR0FhkhECS5lKZy4Am6mnwREpU78xkgd9ltIayfX4KvuRPKFii-gRdon7R0LTBUgYDasshLzMLdFWGNlmpgonH9NoB3wX8q_Dh2rShcjC6-jtGtcx2amCjLxR97yiWebxta7T0yuu5gJChtvyqRv8bkkQJYn9nq_3kBnZmasP6LPKcT9Ees3GkHGsWCVmeF24ZQzG77NnmqHd2n_LHP6wLIXdZodZhmVoKFUKA-EHnB5tRDcFFSneFx396Od02dBMZ0PKalvJ6F2PCEAH5nUO_6pnGJv3N9F-mMY8q6FPJ3qwKO1RUNfhEXosi2q9z3Rpq_MGft7FkQnV7x-hR9WD2ekJl2sNH0TYKwCEdtiy7B_bv9prnz74xaDsm7n10pPD18FIfUMT94hxDSarz3o4P0p0m6m07XYEo8t7BxlsxfLG0ImqrfQrYbC62n-1ZqVHJ84DKgPPMot_FwPqjwvv4fPcOcuw9lZZA.4YJgVfSsrNnmf5UOxf1qfQ" target="_blank">Companies House Developer Hub</a>. 
<br>
![]({{ site.baseurl }}/images/companieshouse/register-account.png)
<br>
After logging into your account, create an application where your API keys will be stored.
<br>
![]({{ site.baseurl }}/images/companieshouse/create-an-application.png)
<br>
Once created, go into your application and create a new REST API key. This key will be used to authenticate your scrape requests. 

![]({{ site.baseurl }}/images/companieshouse/create-new-key.png)
<br>
Make sure you select REST when creating your application.
![]({{ site.baseurl }}/images/companieshouse/create-new-key2.png)
<br>
Copy your API key which will be used to scrape Companies House website.
![]({{ site.baseurl }}/images/companieshouse/keys-for-application.png)

<br>
You are now ready to install the scraper and starting scraping the Companies House website.
<br>
<br>

### Installing and running our Companies House scraper
Install the scraper using pip.
<br>
<div class="highlight">
<code-black>
pip install -i https://test.pypi.org/simple/ cohospider
</code-black>
</div>
<br>
Go into a Python terminal and run the following code.
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

Our scraper will start to scrape the Companies House API, finding all of Barbara's company data. Once finished, all your data can be found in the `data/aqWJlHS4_rJSJ7rLgTK49iO4gAg` folder in your root directory. We can now start the analysis using Raphtory.

## Analysing the data with Raphtory

Install Raphtory via pip.
<br>
<div class="highlight">
<code-black>
pip install raphtory
</code-black>
</div>
<br>
Import all the dependencies needed for this example.

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

We use the in-built Python JSON library to parse the JSON files obtained via the crawler. Through this, we can create a Raphtory graph and add our values to the graph via the `add_edge` function.

<br>
Enter the directory path to your json files inside the path_to_json quotation marks, it should look something like: `~/Pometry/companies_house_scraper/tutorial/data/aqWJlHS4_rJSJ7rLgTK49iO4gAg`.

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

Create a Raphtory graph.

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
Iterate through all the json files (there are many files since the crawler works by crawling page by page) and add values to your Raphtory graph via `add_edge` function.

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
<span class="c1"># Try assigning values to variables. Note that we convert datetime format to epoch timestamps since Raphtory requires time to be in Epoch format.</span>
        <span class="k">try</span><span class="p">:</span>
            <span>ap_d</span> <span class="o">=</span> <span>datetime</span><span class="o">.</span><span>strptime</span><span class="p">(</span><span>json_text</span><span class="p">[</span><span class="s1">&#39;items&#39;</span><span class="p">][</span><span class="mi">0</span><span class="p">][</span><span class="s1">&#39;appointed_on&#39;</span><span class="p">],</span> <span class="s2">&quot;%Y-%m-</span><span class="si">%d</span><span class="s2">&quot;</span><span class="p">)</span>
            <span>appointed_on</span> <span class="o">=</span> <span>int</span><span class="p">(</span><span>datetime</span><span class="o">.</span><span>timestamp</span><span class="p">(</span><span>ap_d</span><span class="p">))</span>
            <span>re_d</span> <span class="o">=</span>  <span>datetime</span><span class="o">.</span><span>strptime</span><span class="p">(</span><span>json_text</span><span class="p">[</span><span class="s1">&#39;items&#39;</span><span class="p">][</span><span class="mi">0</span><span class="p">][</span><span class="s1">&#39;resigned_on&#39;</span><span class="p">],</span> <span class="s2">&quot;%Y-%m-</span><span class="si">%d</span><span class="s2">&quot;</span><span class="p">)</span>
            <span>resigned_on</span> <span class="o">=</span> <span>int</span><span class="p">(</span><span>datetime</span><span class="o">.</span><span>timestamp</span><span class="p">(</span><span>re_d</span><span class="p">))</span>
            <span>company_name</span> <span class="o">=</span> <span>json_text</span><span class="p">[</span><span class="s1">&#39;items&#39;</span><span class="p">][</span><span class="mi">0</span><span class="p">][</span><span class="s1">&#39;appointed_to&#39;</span><span class="p">][</span><span class="s1">&#39;company_name&#39;</span><span class="p">]</span>
            <span>director_name</span> <span class="o">=</span> <span>json_text</span><span class="p">[</span><span class="s1">&#39;items&#39;</span><span class="p">][</span><span class="mi">0</span><span class="p">][</span><span class="s1">&#39;name&#39;</span><span class="p">]</span>
<span class="c1"># Create an edge with time director was appointed to this company, source node is the director name and target node is the company name. The date the director resigned on is set as a property.</span>
            <span>g</span><span class="o">.</span><span>add_edge</span><span class="p">(</span><span>appointed_on</span><span class="p">,</span> <span>director_name</span><span class="p">,</span> <span>company_name</span><span class="p">,</span> <span class="p">{</span><span class="s1">&#39;resigned_on&#39;</span><span class="p">:</span> <span>resigned_on</span><span class="p">})</span>
<span class="c1"># Catch any missing values in the json files (could be because the director has not resigned at this company yet.)</span>
        <span class="k">except</span> <span>KeyError</span> <span class="k">as</span> <span>e</span><span class="p">:</span>
            <span>print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;key </span><span class="si">{</span><span>e</span><span class="si">}</span><span class="s2"> not found in json block&quot;</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div>


### Finding quick statistics about our data via graphs in Raphtory

With the Raphtory API, we can quickly find stats from our data such as the number of companies the director was assigned to, the earliest/latest date the director was assigned to a company and the earliest/latest date the director resigned from a company.
<br>
<br>
*Create a list of directors to see how many different names the director goes by*

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
*Using num_edges() function to find the number of companies formed by the director (director -- company edge)*

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
<pre>Number of companies director assigned to: 443
</pre>
</div>
</div>

</div>

</div>

</div>
<br>

*Using Python's datetime library to convert epoch back into dates to see what the earliest and latest date the director was assigned to a company.*

<div  class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span>print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Earliest date director was assigned to company: </span><span class="si">{</span><span>datetime</span><span class="o">.</span><span>fromtimestamp</span><span class="p">(</span><span>g</span><span class="o">.</span><span>earliest_time</span><span class="p">())</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
<span>print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Latest date director was assigned to company: </span><span class="si">{</span><span>datetime</span><span class="o">.</span><span>fromtimestamp</span><span class="p">(</span><span>g</span><span class="o">.</span><span>latest_time</span><span class="p">())</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
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
<pre>Earliest date director was assigned to company: 2006-09-01 00:00:00
Latest date director was assigned to company: 2016-02-09 00:00:00
</pre>
</div>
</div>

</div>

</div>

</div>
<br>

To obtain the date the director resigned from the company, we have stored this in a property. You can have an infinite number of properties on edges and vertices in Raphtory to store extra information.
<br>
<br>
Through creating a list of these times, we can see what the earliest and latest resignation that the director made.
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
<div class=" highlight hl-ipython3"><pre><span></span><span>list_resigned_on</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span>e</span> <span class="ow">in</span> <span>g</span><span class="o">.</span><span>edges</span><span class="p">():</span>
    <span>list_resigned_on</span><span class="o">.</span><span>append</span><span class="p">(</span><span>e</span><span class="o">.</span><span>property</span><span class="p">(</span><span class="s2">&quot;resigned_on&quot;</span><span class="p">))</span>
<span>list_resigned_on_max</span> <span class="o">=</span> <span>max</span><span class="p">(</span><span>list_resigned_on</span><span class="p">)</span>
<span>list_resigned_on_min</span> <span class="o">=</span> <span>min</span><span class="p">(</span><span>list_resigned_on</span><span class="p">)</span>
<span>print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Earliest company resignation date: </span><span class="si">{</span><span>datetime</span><span class="o">.</span><span>fromtimestamp</span><span class="p">(</span><span>list_resigned_on_min</span><span class="p">)</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
<span>print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Latest company resignation date: </span><span class="si">{</span><span>datetime</span><span class="o">.</span><span>fromtimestamp</span><span class="p">(</span><span>list_resigned_on_max</span><span class="p">)</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
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
<pre>Earliest company resignation date: 2008-10-01 00:00:00
Latest company resignation date: 2020-03-30 00:00:00
</pre>
</div>
</div>

</div>

</div>

</div>
<br>
### Finding information about a particular time window of our graph

We can pick a small view of our graph to filter down all the companies this director was assigned to from 2008 to 2015. We do this with the `g.window()` function which takes a start and end time.

<br>


After creating a view, we can see how many companies the director was appointed to by running the `.degree()` functions on our view.

<div  class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span>view</span> <span class="o">=</span> <span>g</span><span class="o">.</span><span>window</span><span class="p">(</span><span class="mi">1400000000</span><span class="p">,</span> <span class="mi">1450000000</span><span class="p">)</span>
<span>print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Number of companies assigned in this time window: </span><span class="si">{</span><span>view</span><span class="o">.</span><span>vertex</span><span class="p">(</span><span class="s1">&#39;Barbara KAHAN&#39;</span><span class="p">)</span><span class="o">.</span><span>degree</span><span class="p">()</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
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
<pre>Number of companies assigned in this time window: 104
</pre>
</div>
</div>

</div>

</div>

</div>

### Using Raphtory properties to refine our analysis

We filter the edges to only see the companies that this director is assigned to and then resigned to the same day.

<div  class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span>sus_companies</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span>edge</span> <span class="ow">in</span> <span>view</span><span class="o">.</span><span>vertex</span><span class="p">(</span><span class="s1">&#39;Barbara KAHAN&#39;</span><span class="p">)</span><span class="o">.</span><span>edges</span><span class="p">():</span>
    <span class="k">if</span> <span>edge</span><span class="o">.</span><span>property</span><span class="p">(</span><span class="s2">&quot;resigned_on&quot;</span><span class="p">)</span> <span class="o">==</span> <span>edge</span><span class="o">.</span><span>earliest_time</span><span class="p">():</span>
       <span>sus_companies</span><span class="o">.</span><span>append</span><span class="p">(</span><span>edge</span><span class="p">)</span>
<span>print</span><span class="p">(</span><span>sus_companies</span><span class="o">.</span><span class="fm">__len__</span><span class="p">())</span>
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
<pre>88
</pre>
</div>
</div>

</div>

</div>

</div>

### Creating perspectives in Raphtory to create a line plot over time

We can use Perspective which is a struct representing a time range from start to end. We use .rolling() with a window size of 10000000. This window moves forward by a step size (which is the window if you have not specified a step size).

<br>

Through these methods, we "roll" through all the windows/views, counting the number of companies the director was assigned to, and we end up with a line plot of how many companies this director is assigned to over time.
<br>
<br>

*Create a perspective with a rolling window of 10000000 moving forward with a step of 10000000.*

<div  class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span>p</span> <span class="o">=</span> <span>Perspective</span><span class="o">.</span><span>rolling</span><span class="p">(</span><span>window</span><span class="o">=</span><span class="mi">10000000</span><span class="p">)</span> 
<span>views</span> <span class="o">=</span> <span>g</span><span class="o">.</span><span>through</span><span class="p">(</span><span>p</span><span class="p">)</span> 
</pre></div>

     </div>
</div>
</div>
</div>

</div>
<br>
*For each view, count the number of edges and note the time.*

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
*Create the line plot visualisation with seaborn library.*

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

### Using windows to filter particular timepoints of interest
As seen in the line plot, there is a spike at year 2014. To investigate this further we look at a window of 01-01-2014 to 01-01-2015.

<div  class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span>filtered_view</span> <span class="o">=</span> <span>g</span><span class="o">.</span><span>window</span><span class="p">(</span><span class="mi">1388534400</span><span class="p">,</span> <span class="mi">1400070400</span><span class="p">)</span>
<span>p</span> <span class="o">=</span> <span>Perspective</span><span class="o">.</span><span>rolling</span><span class="p">(</span><span>window</span><span class="o">=</span><span class="mi">100000</span><span class="p">)</span> 
<span>filtered_views</span> <span class="o">=</span> <span>filtered_view</span><span class="o">.</span><span>through</span><span class="p">(</span><span>p</span><span class="p">)</span> 
<span>timestamps</span>   <span class="o">=</span> <span class="p">[]</span>
<span>edge_count</span>   <span class="o">=</span> <span class="p">[]</span>

<span class="k">for</span> <span>filtered_view</span> <span class="ow">in</span> <span>filtered_views</span><span class="p">:</span>
    <span>time</span> <span class="o">=</span> <span>datetime</span><span class="o">.</span><span>fromtimestamp</span><span class="p">(</span><span>filtered_view</span><span class="o">.</span><span>latest_time</span><span class="p">())</span>
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
<img src="data:image/png;base64,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qio0b95c6zAazOjxB8vI7TRy7ADjNwojt9PIsQdi9LYZPf5Qa9IJExEREVEwmtykbyIiIiK1mDARERERBcCEiYiIiCgAJkxEREREATBhIiIiIgqACRMRERFRAEyYiOiMM3v2bPTu3VvrMIjoDMI6TERkKIFWSb/xxhsxf/581NTUID09PUJREdGZjgkTERlKSUmJ/P+PP/4YjzzyCHbs2CFvS0hIQEpKihahEdEZjENyRGQomZmZ8k9KSgpMJpPHNvchuZtuugljxozBU089hYyMDKSmpuLRRx+F1WrFvffei7S0NOTm5mLhwoUuf+vQoUOYMGECWrRogfT0dIwePRr79++PbIOJSBeYMBFRk7B8+XIcPnwYq1atwvPPP4/Zs2fjqquuQosWLbBmzRpMmTIFU6ZMQVFREQDg1KlTGDx4MBITE7Fq1SqsXr0aiYmJuOKKK1BbW6txa4go0pgwEVGTkJaWhnnz5qFLly645ZZb0KVLF5w6dQoPPPAAOnfujJkzZyI2Nha//PILAOCjjz6C2WzGG2+8gZ49e6Jr16546623UFhYiBUrVmjbGCKKuGitAyAiioTu3bvDbHZ+R8zIyECPHj3k36OiopCeno7S0lIAwPr167F7924kJSW5PE91dTX27NkTmaCJSDeYMBFRkxATE+Pyu8lk8rrNbrcDAOx2O/r164f333/f47latWoVvkCJSJeYMBERedG3b198/PHHaN26NZKTk7UOh4g0xjlMREReXH/99WjZsiVGjx6Nn3/+Gfv27cPKlSsxdepUHDx4UOvwiCjCmDAREXnRrFkzrFq1Cm3atMHYsWPRtWtX3HLLLTh9+jR7nIiaIBauJCIiIgqAPUxEREREATBhIiIiIgqACRMRERFRAEyYiIiIiAJgwkREREQUABMmIiIiogCYMBEREREFwISJiIiIKAAmTEREREQBMGEiIiIiCoAJExEREVEA/x+V31aN4Xhg2gAAAABJRU5ErkJggg=="
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
<div class=" highlight hl-ipython3"><pre><span></span><span>filtered_view2</span> <span class="o">=</span> <span>g</span><span class="o">.</span><span>window</span><span class="p">(</span><span class="mi">1391212800</span><span class="p">,</span> <span class="mi">1392422400</span><span class="p">)</span>
<span>p</span> <span class="o">=</span> <span>Perspective</span><span class="o">.</span><span>rolling</span><span class="p">(</span><span>window</span><span class="o">=</span><span class="mi">10000</span><span class="p">)</span> 
<span>filtered_views2</span> <span class="o">=</span> <span>filtered_view2</span><span class="o">.</span><span>through</span><span class="p">(</span><span>p</span><span class="p">)</span> 
<span>timestamps</span>   <span class="o">=</span> <span class="p">[]</span>
<span>edge_count</span>   <span class="o">=</span> <span class="p">[]</span>

<span class="k">for</span> <span>filtered_view2</span> <span class="ow">in</span> <span>filtered_views2</span><span class="p">:</span>
    <span>time</span> <span class="o">=</span> <span>datetime</span><span class="o">.</span><span>fromtimestamp</span><span class="p">(</span><span>filtered_view2</span><span class="o">.</span><span>latest_time</span><span class="p">())</span>
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
<img src="data:image/png;base64,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aebMmXr44YfD+lxHjhzRDz/84Lm9fft2rV27VmlpaWrUqJGuvvpqrV69Wv/973/ldDqVl5cnSUpLS1NSUpIkafjw4WrcuLGys7MlSZMnT1b37t2VlZUlh8OhZ599VmvXrtX06dPD/VYBAFWUuzCy2UreJFbDIbCwi6X77rtPLVu21DPPPKO33npLktSmTRvNmjVL1157bVifa+XKlerVq5fn9rhx4yRJI0aM0KRJk/TRRx9Jks4991yf5y1cuFCXXHKJJCknJ0d2e2mD7NChQ7r11luVl5en1NRUderUSUuWLNH5558f7rcKAKiivFfDMcEbpxL2BO94EK0JYgCAiuH9Nbs09p11uijrTG3OdWj/kUJ9csdFapPBa35lFq3f36e1g/ehQ4f08ssv6/7779eBAwckleyvtHv37ogFBgBAtDhPTua222yyu+csMQyHAMIehlu/fr369u2r1NRU7dixQzfffLPS0tL0/vvv66efftLrr78ejTgBAIgYl5/VcIyzIJCwO0vjxo3TyJEjtXXrVp/VbwMGDNCSJUsiGhwAANHgXg3n01miWkIAYRdLK1as0J/+9Kdy1xs3buxZrQYAQEVWus+SPJ0lhuEQSNjFUvXq1f2enbZlyxbVr18/IkEBABBN3p0lVsPhVMIulgYPHqxHHnlERUVFkkqOKcnJydF9992nq666KuIBAgAQae4ukt1uY58lnFLYxdKTTz6pn3/+WQ0aNNDx48d18cUX66yzzlKdOnX0+OOPRyNGAAAiyuk+SNdrB28XxRICCHs1XEpKipYuXaovvvhCq1ev9hxU27dv32jEBwBAxLn8bErJBG8EEnax9Prrr2vYsGHq3bu3evfu7bleWFio2bNna/jw4RENEACASHPPT/JeDUdjCYGEPQx30003KT8/v9z1w4cP66abbopIUAAARJO/1XAMwyGQsIslY4xs7tlwXnbt2qXU1NSIBAUAQDR5D8PZ2ToApxDyMFynTp1ks9lks9nUp08fJSaWPtXpdGr79u267LLLohIkAACR5D7uxGazKcG9Go45Swgg5GJpyJAhkqS1a9eqf//+ql27tue+pKQkNW/enK0DAACVgmcYznvOEp0lBBBysTRx4kRJUvPmzTVs2DCfo04AAKhM/A7D0VlCAGGvhhsxYkQ04gAAwDJOr9Vw7n2WmLOEQMIulpxOp55++mn961//Uk5OjgoLC33uP3DgQMSCAwAgGlx+VsPRWEIgYa+Gmzx5sqZMmaJrr71W+fn5GjdunIYOHSq73a5JkyZFIUQAACLL5XXcCavhcCphF0tvvvmmZsyYofHjxysxMVHXX3+9Xn75ZT388MP66quvohEjAAAR5V4Nl8BqOIQg7GIpLy9PHTp0kCTVrl3bs0HlFVdcoblz50Y2OgAAoqB0GM7GppQ4pbCLpSZNmig3N1eSdNZZZ2nevHmSpBUrVig5OTmy0QEAEAXuITeb19YBdJYQSNjF0u9+9zt9/vnnkqQ77rhDDz30kLKysjR8+HCNGjUq4gECABBp7LOEcIS9Gu5vf/ub5+Orr75aTZo00bJly3TWWWfpyiuvjGhwAABEQ+k+S6Wr4ZjgjUDCLpbK6t69u7p37x6JWAAAsITT32o4aiUEEPYwnCT9v//3/9SjRw81atRIP/30kyRp6tSp+vDDDyMaHAAA0eBuInmvhjPMWUIAYRdLL7zwgsaNG6eBAwfq0KFDcjqdkqS6detq6tSpkY4PAICI814Nxz5LOJWwi6XnnntOM2bM0AMPPKCEhATP9a5du2rDhg0RDQ4AgGjwDMN5H3dCZwkBhF0sbd++XZ06dSp3PTk5WUePHo1IUAAARFPp2XBinyWcUtjFUosWLbR27dpy1z/55BO1bds2EjEBABBVpavhbLJ5DtKNZUSoyMJeDXf33XdrzJgxOnHihIwx+uabb/T2228rOztbL7/8cjRiBAAgorxXwyWcbBswDIdAwi6WbrrpJhUXF+uee+7RsWPHdMMNN6hx48Z65plndN1110UjRgAAIsrltSllAptS4hTCKpaKi4v15ptvatCgQbrlllu0f/9+uVwuNWjQIFrxAQAQce66yHufJRedJQQQ1pylxMRE/fnPf1ZBQYEk6cwzz6RQAgBUOu5huARWwyEEYU/w7tatm9asWRONWAAAsIT3PkushsOphD1n6bbbbtNdd92lXbt2qUuXLqpVq5bP/eecc07EggMAIBrcnSWbTV6bUsYyIlRkYRdLw4YNkyT99a9/9Vyz2Wwyxshms3l29AYAoKJyem0d4JngzTAcAgi7WNq+fXs04gAAwDLeq+FONpY47gQBhT1nqVmzZkHfwrFkyRINGjRIjRo1ks1m0wcffOBzvzFGkyZNUqNGjVSjRg1dcskl2rRp0yk/75w5c9S2bVslJyerbdu2ev/998OKCwBQtXnvs+QZhqOzhABCLpZWrVqlXr16yeFwlLsvPz9fvXr10rp168L64kePHlXHjh01bdo0v/f/4x//0JQpUzRt2jStWLFCDRs21KWXXqrDhw8H/JzLly/XsGHDdOONN2rdunW68cYbde211+rrr78OKzYAQNXlbiJ5r4YzFEsIIORi6amnnlLv3r2VkpJS7r7U1FRdeuml+uc//xnWFx8wYIAee+wxDR06tNx9xhhNnTpVDzzwgIYOHar27dvrtdde07Fjx/TWW28F/JxTp07VpZdeqgkTJujss8/WhAkT1KdPH02dOjXgcwoKCuRwOHzeAABVl/dquNIJ3hRL8C/kYunrr7/W4MGDA94/aNAgLVu2LCJBSSVzo/Ly8tSvXz/PteTkZF188cVBv87y5ct9niNJ/fv3D/qc7Oxspaamet4yMzN//TcAAKiwfI87YTUcggu5WNq9e7fq1KkT8P7atWsrNzc3IkFJUl5eniQpPT3d53p6errnvkDPC/c5EyZMUH5+vudt586dvyJyAEBF5ymWbGI1HE4p5NVw9evX15YtW9SiRQu/93/33Xc688wzIxaYm/s0aDf3FgWRfE5ycrKSk5NPP0gAQKXisxqOYTicQsidpb59++rxxx/3e58xRk888YT69u0bscAaNmwoSeU6Qvv27SvXOSr7vHCfAwCILz6r4dxbB9BZQgAhF0sPPvigNmzYoG7duulf//qX1q1bp/Xr1+udd95Rt27dtGHDBj3wwAMRC6xFixZq2LCh5s+f77lWWFioxYsX68ILLwz4vAsuuMDnOZI0b968oM8BAMQXz2o4jjtBCEIehmvVqpUWLFigkSNH6rrrrvMMaxlj1LZtW82fP19nnXVWWF/8yJEj+uGHHzy3t2/frrVr1yotLU1NmzbVnXfeqSeeeEJZWVnKysrSE088oZo1a+qGG27wPGf48OFq3LixsrOzJUl33HGHevbsqb///e8aPHiwPvzwQy1YsEBLly4NKzYAQNVVOmfJJruNYTgEF9YO3l27dtXGjRu1du1abd26VcYY/eY3v9G55557Wl985cqV6tWrl+f2uHHjJEkjRozQrFmzdM899+j48eO67bbbdPDgQXXr1k3z5s3zmWiek5Mju720QXbhhRdq9uzZevDBB/XQQw+pVatW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15xOp8nPz7c6NMt89913no+ff/55Y7PZzIwZM8zGjRvN3//+d9O0aVPzySefxDDC6Hv11VdNz549zRlnnGEGDBhg9u7d62m133fffaZevXpm69atMY7SWuvXrzdZWVlmypQpxhhjiouLYxxR9I0YMcK0a9fOFBQUGGOMycvLMw0bNjRz5swxjzzyiElPTzeHDh2KcZTRtXnzZp/bvCbG52virFmzovqaSLFUSTmdTs/Ht956q6f9XFxcbO6//37z6KOPmqKiohhGGH0FBQXmgw8+MF9++aXP9ZYtW5q77rorRlFZZ8aMGeaGG24wK1asMMb4/kzUrl3bTJs2LVahWcb7ezbGmLvuuss0bNjQ/PzzzzGKyFp79+41bdq0Menp6WbAgAGmVq1a5uabbzbGGHP06FFTv359s2TJkhhHGR1l/+3j8TWx7B8E8fia6P1vOnPmzKi9JiZGrhGGSNuyZYtmzZqlHTt2qHfv3urYsaPOP/98Sb6z+//v//5PNptNf/jDH3T++edr/vz5WrdunRITK/8/b7AcJCUladCgQbLbS0aTnU6nDh06pFatWqlLly6xDDuiyuagffv2uuCCC3TzzTerc+fOateunaSSYRljjH788Ue1aNFCbdu2jXHkkRPo58But8vlckkq+f5HjBihTz75RG+//bZuv/12GWOqzOo47xz06tVL5557rs4//3ytWLFCjz/+uGrUqKFhw4ZpxIgRkkqWUKempiojIyPGkUfO/v37deLECTVp0sTz/97N+3ZVfk30zkFCQoLPffHymuidg8TERDmdTiUkJOimm25S586ddfbZZ0uK8GviaZdZiKpNmzaZunXrmkGDBplBgwaZVq1amW7dupnnn3/e8xjvvyoKCgpMixYtTL169czatWtjEXLEhZKDsn8pPvzww6Z169Zmx44dVocbFYFy8NxzzwV8zoMPPmg6duxodu/ebWGk0RPKz4H7L0in02kGDx5sunTpEqtwo8JfDs4///ygfynfd999pmvXrmb//v0WRho9mzZtMmlpaWbUqFFmz549p3x8VX1NPFUOyq58q4qvif5yEGzYPRKviRRLFVBhYaG58cYbzR//+EfPtbVr15o777zTNGvWzDz99NOe6y6XyxQVFZnbbrvN2O12s2HDhhhEHHnh5MAYYz7++GNz1113mbp165o1a9ZYG2yUhJuD//znP2bs2LEmJSUlLnPgLpwXLVpkmjZt6jNnoTI7VQ6eeuopn8d/88035i9/+YupXbt2lfk5yM3NNd27dzc9evQw1atXNzfffHPQgqkqviaGm4Oq+JoYbg4i+ZpY+XuSVVBCQoK2bdumc88913OtY8eOuuOOO5SUlKT/+7//U0ZGhoYNGyabzaZ9+/ZJklasWKH27dvHKOrICicHLpdLa9as0TfffKMvv/wybnOwYsUKLVmyREuXLlWHDh1iF3gEhZMD9xDLOeeco5UrV6p+/foxijqyTpWDGTNmqHHjxho2bJgkyeFwyGazafny5VXi/4IxRhs2bFCTJk3097//XTt27FD//v0lSY888ojfYca9e/dKqjqvieHmwOVyafXq1VXqNfF0cvD1119H7jXxV5VaiDiXy2VcLpf585//bK655hpz4MABn/u/++47c/XVV5trr73WswLGGGOOHz9udahRE04OvPcPKfu4yux0c1CV9lcK9/9CVegilXW6PwdV6fXAmJKOwpIlSzz/xvPnzzeJiYnm5ptv9hla8Z7QG6858B6OqkqvicacXg4iNQxNsVRBzZ4929SoUcO8/PLL5X4JfPjhhyYxMdF8//33MYrOGuSAHBhDDowhB97cu1IvWLDA84tyz549pri42Dz33HNm/vz5MY4w+siB9TlgGK6CGjZsmNatW6cxY8aoZs2aGjp0qJKTkyVJWVlZat26dYwjjL5QcmCq6GZ7buSA/wsSOfBWrVo1OZ1O9enTR5999plnKOb48eP68MMPtXr16hhHGH3kwPocUCxVQIWFhUpKStITTzwhp9OpG2+8Udu3b1e/fv2UlZWlmTNn6sSJE56de6uiUHNwxhlnxDrUqCEH/F+QyIEkz9JwN/eWEb1799bcuXN12WWXKTU1VYsXL1ZWVlYMI40echDjHES0T4VfzT3WumvXLvP+++8bY4z5xz/+Ydq0aWPq1q1rOnbsaBo2bGhWr14dwyijixyQA2PIgTHkwJjSHOzevdu899575eZqjh071qSmppY73aAqIQexzwHFUowUFxf7/GMbU7r0eceOHaZu3brmoYce8tz33Xffmc8//9x8+umnZteuXZbGGi3kgBwYQw6MIQfGnDoHZ5xxhpk0aZLP/StWrDCZmZnm66+/tizOaCIHFTcHFEsxsHnzZvPHP/7R9OjRw4wePdrM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"
class="
"
>
</div>

</div>

</div>

</div>

</div>

### Dynamic visualisation of your graph in Raphtory

To visualise specific dates, we first create window of the time we want and use Raphtory's `.to_pyvis()` function to create a dynamic visualisation of the edges. In this way, we clearly see the director's company assignation and resignation behaviour.

The visualisation will appear in a file called `nx.html` which can be opened in a web browser.

<div  class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span>twelfth_of_feb</span> <span class="o">=</span> <span>g</span><span class="o">.</span><span>window</span><span class="p">(</span><span class="mi">1392163199</span><span class="p">,</span> <span class="mi">1392163201</span><span class="p">)</span>
<span>vis</span><span class="o">.</span><span>to_pyvis</span><span class="p">(</span><span>graph</span><span class="o">=</span><span>twelfth_of_feb</span><span class="p">,</span> <span>edge_color</span><span class="o">=</span><span class="s1">&#39;#F6E1D3&#39;</span><span class="p">,</span><span>shape</span><span class="o">=</span><span class="s2">&quot;image&quot;</span><span class="p">)</span>  
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

</div>
</div>

</div>

</div>

</div>
If you would like your graph in a list of vertices and edges, you can call methods such as `vertices()` and `edges()`.
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



![]({{ site.baseurl }}/images/companieshouse/barbara-kahan.png)

Temporally analysing data has been difficult in the past, however Raphtory makes it incredibly easy. Rather than looking at data statically, taking into account of time can unlock a lot of interesting insights that may be beneficial to your unique use cases. 

<br>
If you would like to run these algorithms at scale in a production environment, drop the team at <a href="https://www.pometry.com/contact/" target="_blank">Pometry</a> a message, and they will be more than happy to help.


<br>
<br>