# #!/usr/bin/env python
# import sys

# current_category = None
# count = 0

# for line in sys.stdin:
#     category, sales = line.strip().split('\t')
    
#     if current_category == category:
#         count += 1
#     else:
#         if current_category:
#             print(f"{current_category}\t{count}")
#         current_category = category
#         count = 1

# if current_category:
#     print(f"{current_category}\t{count}")

#!/usr/bin/env python
# import sys

# current_category = None
# count = 0

# for line in sys.stdin:
#     category, sales = line.strip().split('\t')
    
#     if current_category == category:
#         count += 1
#     else:
#         if current_category and count > 114:
#             print(f"{current_category}\t{count}")
#         current_category = category
#         count = 1

# if current_category and count > 114:
#     print(f"{current_category}\t{count}")

#!/usr/bin/env python
import sys

current_category = None
total_sales = 0
count = 0

for line in sys.stdin:
    category, sales = line.strip().split('\t')
    
    if current_category == category:
        total_sales += float(sales)
        count += 1
    else:
        if current_category:
            average = total_sales / count
            print(f"{current_category}\t{average:.2f}")
        current_category = category
        total_sales = float(sales)
        count = 1

if current_category:
    average = total_sales / count
    print(f"{current_category}\t{average:.2f}")