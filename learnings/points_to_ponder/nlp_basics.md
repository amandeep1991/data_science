# Spelling Mistakes: 
>* Fuzzy Matching: 
>>* **Hamming Distance**
>>>* just overlap and see not matching characters. Limitation - doesn't work very well for different length words and for same length as well few false positive are there

```python
def hamming(target, source):
    """Given two strings, return hamming distance"""
    target = target.upper()
    source = source.upper()
    dist = [1 for x,y in zip(target, source) if x!=y]
    return len(dist)
    
target = 'currajong'
source = 'kurrajong'
    
```

>>* **Improved Hamming Distance**:


```python
def hamming(target, source):
    """Given two strings, return hamming distance"""
    target = target.upper()
    source = source.upper()
    dist = [1 for x,y in zip(target, source) if x!=y]
    return len(dist) + max(0, len(source)-len(target)) # whyn't len(target)-len(source) as we want to match North Korea (source) with Korea (target)
    
target = 'currajong'
source = 'kurrajong'
    
```


>>* **Soundex Algorithm**: Not very useful, as most of the words it says sounds similar. Python implementation - jellyfish


>>* **Metaphone**: 
>>>* Improvement on soundex algorithm (drop duplicate adjacent letters except c) - 17 rules like this. 
>>>* Python implementation - jellyfish
>>>* Doesn't work with 'Melbourne North' or 'Melbourne South' if matching with 'Melbourne'. Improve it like hamming d/s.


>>* **Levenshtein Distance**:
>>>* Like hamming distance, but here we would treat 1 for insert, deletion, substitutions etc.
>>>* Python Implementation is difflib (higher the ratio is more similar are words)
>>>* A lot slower but can be improve it

```python
ratio = difflib.SequenceMatcher(None, word1, place_name).ratio()

``` 

>>* Easter Egg: (Fastest operation)
>>>* Matching the sequence.
>>>* Input - rrjng => search for regex r.*r.*j.*n.*g.*

>* Conclusion:
>>* There is no single best algorithm
>>* Always a trade-off between accuracy & speed
>>* Understanding an algo will allow you to improve the algorithm