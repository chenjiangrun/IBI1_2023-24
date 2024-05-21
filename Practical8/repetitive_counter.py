sequence = "ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA"
a=0
for i in range(0,34):
    if sequence[i:i+6]=="GTGTGT":
        a=a+1
    if sequence[i:i+6]=="GTCTGT":
        a=a+1
    i=i+3
print(a)

