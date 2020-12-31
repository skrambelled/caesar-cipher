# Caesar cipher

This is Caesar Cipher implementation, which allows you to input some phrase and encrypt it by shifting each letter by some number.

```python
encrypt('hello world', 10)
```

means we'll shift each letter by 10 places, take a look at what that looks like in this key:

 | a | b |c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | z | t | u | v | w | x | y | z |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| q | r | s | t | u | v | w | x | y | z | a | b | c | d | e | f | j | h | i | j | k | l | m | n | o | p |

'hello world' => 'rovvy gybvn'

If you know by how many places a given message was encrypted, then you can `decrypt` using that same value:

```python
decrypt('rovvy gybvn', 10)
```

If you do now know by how many places something was encrypted, have no fear, we can crack the code!

```python
crack('rovvy gybvn')
```

This will run all 26 options (yes, we'll even run the original) and check to see how many of those words in each iteration are actually words[^1], then return the particalur iteration with the hishest percentage of real words.

You can also optionally pass a `threshold`, so that some percentage of words must be actual words. `threshhold` is set to .5 by default, so 50% of the words in the cracked phrase must be real words for the phrase to be considered.

```python
# set your threshold to 80%
crack('rovvy gybvn', threshhold=.8)
```

[^1]: Words are supplied by `nltk` package, and also includes names, like John or London.
