# Hexdump
----
Imitates the Unix 'hexdump' command line utility. Takes a file as input and prints the byte representation of the file in the same format as Unix hexdump.

## Directory Structure
---
```
├───.idea
├───images    # contains images to dump with hexdump
├───src       # contains 'hexdump.py' file
└───test      # contains the test text files
```

## Running hexdump
----
Run from root project directory on sample text files with:   
`python src/hexdump.py test/test3.txt`      

or run on images in image directory:   
`python src/hexdump.py images/truck-tracks.jpg`


## Sample Output
----
```
> python src/hexdump.py images/truck-tracks.jpg
00000000  ff d8 ff e0 00 10 4a 46  49 46 00 01 01 01 00 e6  |......JFIF......|
00000010  00 e6 00 00 ff db 00 43  00 28 1c 1e 23 1e 19 28  |.......C.(..#..(|
00000020  23 21 23 2d 2b 28 30 3c  64 41 3c 37 37 3c 7b 58  |#!#-+(0<dA<77<{X|
00000030  5d 49 64 91 80 99 96 8f  80 8c 8a a0 b4 e6 c3 a0  |]Id.............|
00000040  aa da ad 8a 8c c8 ff cb  da ee f5 ff ff ff 9b c1  |................|
00000050  ff ff ff fa ff e6 fd ff  f8 ff db 00 43 01 2b 2d  |............C.+-|
00000060  2d 3c 35 3c 76 41 41 76  f8 a5 8c a5 f8 f8 f8 f8  |-<5<vAAv........|
00000070  f8 f8 f8 f8 f8 f8 f8 f8  f8 f8 f8 f8 f8 f8 f8 f8  |................|
00000080  f8 f8 f8 f8 f8 f8 f8 f8  f8 f8 f8 f8 f8 f8 f8 f8  |................|
00000090  f8 f8 f8 f8 f8 f8 f8 f8  f8 f8 f8 f8 f8 f8 ff c2  |................|
000000a0  00 11 08 04 80 06 00 03  01 11 00 02 11 01 03 11  |................|
000000b0  01 ff c4 00 18 00 00 03  01 01 00 00 00 00 00 00  |................|
000000c0  00 00 00 00 00 00 00 01  02 03 04 ff c4 00 16 01  |................|
000000d0  01 01 01 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
000000e0  00 01 02 ff da 00 0c 03  01 00 02 10 03 10 00 00  |................|
000000f0  01 a8 42 18 0c 40 02 01  53 86 20 19 23 50 10 01  |..B..@..S. .#P..|
00000100  2b 44 35 48 14 a2 35 10  56 82 b1 12 94 03 50 43  |+D5H..5.V.....PC|
00000110  40 14 04 14 1a 20 10 c0  62 50 a1 09 1a 80 24 62  |@.... ..bP....$b|
00000120  20 63 10 c4 30 18 08 09  18 08 45 08 40 33 33 51  | c..0.....E.@33Q|
00000130  08 66 65 80 c9 a7 0c 43  26 91 50 50 48 86 5c 14  |.fe....C&.PPH.\.|
00000140  0a 0a 64 96 21 15 05 22  a1 16 02 00 18 80 06 03  |..d.!.."........|
00000150  20 a1 8c 06 00 20 05 43  41 44 01 44 15 00 00 86  | .... .CAD.D....|
00000160  89 41 08 62 00 19 23 10  0d 12 c9 04 58 a1 d2 85  |.A.b..#.....X...|
00000170  4e 01 53 08 e9 00 10 00  c4 31 00 08 6a 91 80 80  |N.S......1..j...|
00000180  00 6a 20 a0 86 80 02 a2  91 28 8d 41 81 08 2d 23  |.j ......(.A..-#|
00000190  01 02 88 d4 40 62 10 28  8d 52 25 00 62 2c 48 95  |....@b.(.R%.b,H.|
    .                         .                         .   
    .                         .                         .
    .                         .                         .
0002c890  8f e5 4c 25 a3 2e 99 b2  ba d3 94 06 d8 e4 16 1d  |..L%............|
0002c8a0  d9 64 05 dc 52 09 bd 13  62 63 28 f2 53 45 9e 1f  |.d..R...bc(.SE..|
0002c8b0  91 42 dc e2 58 e7 7d a8  38 0a 5d 80 60 32 36 74  |.B..X.}.8.].`26t|
0002c8c0  f9 5f 23 ea 55 ac b3 4d  53 ff 00 62 36 8a 1b 5f  |._#.U..MS..b6.._|
0002c8d0  20 55 8f 69 00 18 7c 1f  b0 75 6d 8a dd 45 6d d5  | U.i..|..um..Em.|
0002c8e0  a7 3c 61 20 de 3f ea 21  5a ea d8 fd 8a 2a df 48  |.<a .?.!Z....*.H|
0002c8f0  cf 07 4f d9 89 f3 47 f8  bf 26 b9 28 0a 44 b8 81  |..O...G..&.(.D..|
0002c900  f1 73 f1 8d a9 8d 69 3a  58 7d 20 fc 68 ec b5 6f  |.s....i:X} .h..o|
0002c910  b2 8c 7a c7 c5 ed 64 da  b2 53 73 f7 21 6a 46 71  |..z...d..Ss.!jFq|
0002c920  97 6f fd 0f 65 54 77 16  e6 3a 06 f6 03 af b2 c5  |.o..eTw..:......|
0002c930  e8 47 49 65 9e 9f b2 90  eb ec ee c6 92 0d a8 74  |.GIe...........t|
0002c940  f2 71 bb cf cf b0 5b 65  35 16 29 6d f6 5a aa c4  |.q....[e5.)m.Z..|
0002c950  bb 18 2e 73 e4 1a d7 a4  40 5d 9f 7d fc 89 b2 1a  |...s....@].}....|
0002c960  3a 7c 83 86 5c ff d9                              |:|..\..|
0002c967

  ```
