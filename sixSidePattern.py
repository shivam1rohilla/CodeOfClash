"""
The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01 Test 1
Input
Expected output
1
 _ 
/ \
\_/
02 Test 2
Input
Expected output
2
 _   _ 
/ \_/ \
\_/ \_/
  \_/
03 Test 3
Input
Expected output
3
 _   _   _ 
/ \_/ \_/ \
\_/ \_/ \_/
  \_/ \_/
    \_/
04 Test 4
Input
Expected output
4
 _   _   _   _ 
/ \_/ \_/ \_/ \
\_/ \_/ \_/ \_/
  \_/ \_/ \_/
    \_/ \_/
      \_/
"""

n=int(input())
print(*[" _ "]*n)
print(*["/ \\"]*n,sep="_")
print(*["\\_/"]*n)
for i in range(1,n):
    print(*[" "]*i+["\\_/"]*(n-i))
