<h1>Wikipedia PyCrawler</h1>

<p>This is my personal version of the PyCrawler. The crawler only crawls Wikipedia pages and while it crawls it gathers up all the text data on a page. When the crawler is finished (or the "write" command is sent) the processed text data is printed to a file that can be read by CorrelationFileReader.py</p>

<p>The data processor, TextData, tracks all the words it finds and logs all the words that are found directly adjacent to a given word. For example if you query "united" the word "states" will score high as a words that is commonly seen with "united". Some very intertesting results can be found and if the crawler visits many sites, hundreds of thousands of words can be queried.</p>

<p>Another interesting feature of this crawler is the Command.py program. I currently run the crawler on a UNIX server as a background process. While this comes with some obvious advantages (it will run "forever"), there is no way to see what my crawler is doing and there is no way to stop it without killing it. With the Command program I can send the crawler commands, namely: "status", "status-all", "write", and "stop". These commands are written to the command.txt file that is checked by the crawler between each website. If the crawler sees a command, it executes whatever is needed and writes a response into response.txt which the Command program reads and prints to the console. This creates an easy way to peek into the state of the crawler as well as performing functions in a safe and predictable way.</p>

<p>When data is written it is saved in a format that is readable to the CorrelationFileReader. This program, lets call it CFR, loads the file's data into memory (warning: this can eat a lot of memory) so that when a query is sent to CFR it can return results in a timely manner.</p>

<h3>Warning</h3>
<p>The timeout functionality of the crawler only works on UNIX systems due to the fact that it imports "signal". In the repo I have commented out the timeout.py import as well as the code decorator in <code>getText</code> just in case.</p>

