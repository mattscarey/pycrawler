<h1>PyCrawler</h1>
<h3>A customizable, all-purpose, reliable random web crawler</h3>

This is the vanilla version that starts at www.iub.edu and crawls randomly from there. 

The crawler starts by grabbing all links from a page and filtering them out using the <code>sanatize</code> function. Custom parameters can be inserted into the function by editeing the <code>specialCases</code> function. The crawler then picks a link at random from the links list and updates the "pool" set with all the links. The pool is used for cases where the links array is empty and the crawler needs to backtrack. The crawler then repeats these steps while keeping a list of visited links to make sure there are no repeat visits. </p>

<p>So far I have had my own version (wikipedia crawler branch) visit well over half a million unique websites (and still counting!) without stopping. The vanilla crawler is fairly simple and is easy to customize for your own needs.</p>

<h3>Warning</h3>
<p>The timeout functionality of the crawler only works on UNIX systems due to the fact that it imports "signal". In the repo I have commented out the timeout.py import as well as the code decorator in <code>getText</code> just in case.</p>

