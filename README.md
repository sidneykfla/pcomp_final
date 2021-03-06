# Physical Computing Final Project
DIG 333 - Physical Computing Final Project

## Materials
- [Raspberry Pi 3 Model B](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/)
- [68 Ω Resistors (5)](https://www.amazon.com/Projects-Resistors-Watt-Choose-Quantity/dp/B00CVZ3UTU?th=1)
- [82 Ω Resistors (5)](https://www.amazon.com/Projects-Resistors-Watt-Choose-Quantity/dp/B077G7RVQM) (NOTE: Ten 68 Ω resistors can easily be used instead of two sets of five. I chose two sets of five because I only had five of each.)
- [Female to Male Jumper Wires (19)](https://www.amazon.com/GenBasic-Female-Solderless-Breadboard-Prototyping/dp/B078P4PJKJ)
- [Red LEDs (10) and Blue LEDs (8)](https://www.amazon.com/AUKENIEN-Emitting-Assortment-Components-Electronics/dp/B0972D2BMH/ref=sr_1_1_sspa?keywords=red+led+5mm&qid=1652343834&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExSE9YRkc5UkxXQ0NZJmVuY3J5cHRlZElkPUEwNzY0MjE3MUtRWUhVRTBOTEgxTCZlbmNyeXB0ZWRBZElkPUEwMjQ3MDQ3NDNCN1RGRVhOSENMJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==)
- [Breadboard](https://www.amazon.com/BB400-Solderless-Plug-BreadBoard-tie-points/dp/B0040Z1ERO)

## Wiring Schematic
![Screen Shot 2022-05-12 at 3 58 26 AM](https://user-images.githubusercontent.com/68158566/168021313-7b5863fb-cab2-431e-becc-25067940746a.png)

| LED number | GPIO Pin |
|------------|----------|
|     1      |    2     |
|     2      |    3     |
|     3      |    4     |
|     4      |    5     |
|     5      |    6     |
|     6      |    7     |
|     7      |    8     |
|     8      |    9     |
|     9      |    10    |
|     10     |    11    |
|     11     |    12    |
|     12     |    25    |
|     13     |    14    |
|     14     |    15    |
|     15     |    16    |
|     16     |    17    |
|     17     |    23    |
|     18     |    24    |


## Demo
1. Clone repository
2. Run <b>python3 project_draft.py True</b> from the command line. Running the code using "True" starts the scheduling programs which make the hunger and thirst levels decrease over time.
3. Enter "feed" when asked <b> How do you want to interact with your rock? </b>.

```
          /---------\ 
        /             \ 
       /               \ 
      /      -   -      \ 
      |                 |
       \       ---     / 
        \             /
          ----------- 

Your rock cannot eat but somehow adjusts its nourishment levels accordingly.

Hunger level: 9
Thirst level: 2
```


Results:


https://user-images.githubusercontent.com/68158566/168020034-284acadc-6091-479a-ab5f-d14b041e207d.MOV



4. Enter "give water" when prompted with the same question.

```
          /---------\ 
        /             \ 
       /               \ 
      /      -   -      \ 
      |                 |
       \       ---     / 
        \             /
          ----------- 
Your rock...somehow drinks? It's not supposed to be able to do that.

Hunger level: 9
Thirst level: 5
```
Results:


https://user-images.githubusercontent.com/68158566/168020070-73e2dfae-b12e-45e1-8e56-d54c39b51786.MOV


5. Enter "play" when prompted.

```
          /---------\ 
        /             \ 
       /               \ 
      /      -   -      \ 
      |                 |
       \       ---     / 
        \             /
          ----------- 
Your rock sits there, unable to move but moderately happier.

Hunger level: 9
Thirst level: 5
```
Results:

https://user-images.githubusercontent.com/68158566/168020083-0450ca54-27a1-4e7f-884b-c91da91f9777.MOV

6. Press "w" to exit code.
