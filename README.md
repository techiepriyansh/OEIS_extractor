# OEIS_extractor
To extract the useful pieces of information from the Online Encyclopedia on Integer Sequences for offline use.

# Usage
Open up your terminal and execute:

<code>python OEIS_saver.py sequence_index_to_start_from sequence_index_to_terminate_at</code>

This will download sequences from A_sequence_index_to_start_from to A_sequence_index_to_terminate_at in a file named OEIS_text.txt

# Customization
The code is pretty self explanatory and well commented which makes it very easier to exploit.

However you might wanna inspect the layout/format of the original website itself to get a better feel of what you are doing.

Can be easily extended to other websites also.

# Optimization
There is a very slight chance of optimizing the code to any better but nonetheless there is very high chance of boosting up the speed of getting requests. As you might notice that the file which is generated is very less in size but even then, it takes a lot of time to generate it(relatively). This is because we are not continuously hung up on a single request. We are dealing with multiple requests which ends up spending time, multiple times, in sending the request and receiving the response. Hence, you can use Online Python IDEs such as <a href="repl.it">Repl.it</a> and then run the scripts. What now happens is that your requests are now being handled by the IDE's server which ends up doing the work really fast.


