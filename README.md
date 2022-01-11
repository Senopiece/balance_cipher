# funny_rns
This is a simple project in which I will try to have some fun with balance encryption (forward "encryption" and backward "hacking") using [RNS](https://en.wikipedia.org/wiki/Residue_number_system).

# Basics
The main idea is to encrypt my current balance on the blockchain somehow, so only I, as the owner of the private key, can see this.
Hoping to create such a algo, that only a private key is required to view related account balance, but it seems impossible at the current point.

[version 1.0.0]
The basic principle is very simple. I am a verifier, and actually I dont need to know who is the sender, who is the receiver of the transaction, even more so about their balances. What I actually need to know is that sender sended the same amount of money that receiver received, but again I dont even care about the transfer amount.
So, using math i need to verify that:
```
B1 + B2 = B1_new + B2_new
B1_new > 0 (current problem is here)
B2_new > 0
```
So, how to encrypt it?
Firstly, let us consider a number system to which it is easy to translate, and from which it is difficult... the suitable choise here is RNS (let us now consider that RNS is highly hard to reverse (TODO: not as hard as I wanted it to be)), so we can hide balances using it's RNS representation (moreover RNS have some other well suitable properties here like impossible comparison, hard division (TODO: not as hard as I wanted it to be)).
But it is not the end, the problem here is that many balances can be repeated, so for example a frequently used balance 10, can be revealed easily, so we need to add some additional cipher. Keeping in mind that division is also a "hard" operation in RNS, we can modify this formula:
```
B1 = M1*RNS(actual balance)
B2 = M2*RNS(actual balance)
B1*M2 + B2*M1 = B1_new*M2 + B2_new*M1
B1_new > 0 (current problem is here)
B2_new > 0
```
where Mn can be denoted by the formula:
```
Mn = RNS(some private key specific secret)
```
So, this was the basics of the version 1.0.0, there still a lot of problems with not so strong decryption complexity and protocol nuances how to choose "some private key specific secret" etc...

# Basics2
I switched from rns to power and modulo arithmetic and modified the key concept, now it is persistent also for repeating balances. Also I have found interesting algebraic ring, it seems to be ultra hard to reverse, and now it only needs fast elemnts summation, element-scalar summation and element-scalar multiplication. According to the last remaining problem - underflow detection, I still have no idea on it.

# Alternatives and motivation
Yeah, I have heard about Zcash and zk-SNARKs and zk-STARK, it's a pretty technology, but that existence doesn't stop me from being thirsty to try to play with some another kind of encryption.

# Notes
Maybe I will come up with better method of encryption, rather then rns, or maybe with better idea of transfer verification, however, I'm planning to store here all the ideas about balance encryption on the blockchain, moreover as far as I can I'm planning to publish hacking methods of nearby created algos here, hoping to create many different encryption algorithms and break most of them.
