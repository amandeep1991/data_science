# Topics to be covered
>* Durabiliy of writes (how you know that data is persist on disk)
>* Replication of data (for availability), 
>* Sharding (distribute data across multiple servers)

## Write Concern
>* There are two parameters which we should be aware about:
>>* w (=1 by default) -> Time taken by memory to reply the application
>>* j (=false or 0 by default) -> should the application wait for journel to write on the disk.

![06.01.WriteConcern.jpg](img/06.01.WriteConcern.jpg)

>* Combination of different values of w & j:

|W|j|Comments|
|-|-|--------|
|1|false|**default**<br>fast<br>small window of vulnarability|
|1|true|slow<br>greater level of safety|
|0|not acknowledge||


## Network Error
>* Some times due to network error, we might not get the acknowledgement whether our command has executed or not:
>* In this case, there could be two possibilities:
>>* While sending the msg, it got some network issue --> **NO CHANGE TO DB**
>>* Acknowledgement from the server never reached to the application --> **DB UPDATED** (may be - unless special scenarios happended like constraint exception comes it etc.)

![06.02.NetworkErrorsjpg.JPG](img/06.02.NetworkErrorsjpg.JPG)

>* Issues with the command:
>>* Now we can use the same insert query multiple times if it has same id --> **GOOD**
>>* Updates will cause the issue especially for those whose with idempotent operators like **inc** --> **BAD**
