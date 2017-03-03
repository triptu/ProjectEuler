nums = 'one,two,three,four,five,six,seven,eight,nine'.split(',')
count = 0

for k in nums:
    count+=len(k)
store= count     # one to nine

count+=len('teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen')


nums2 = 'twentythirtyfortyfiftysixtyseventyeightyninety'
count+=len(nums2)*10
count+=store*8
store = count # 1 to 99

# Counted till 99
hun = len('hundred')
for k in nums:
    count+=len(k)*100 +hun*100+ len('and')*99 + store

count+=len('onethousand')
print count


