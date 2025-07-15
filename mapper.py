# #!/usr/bin/env python
# import sys

# for line in sys.stdin:
#     data = line.strip().split('\t')
#     if len(data) == 6:
#         date, time, item, category, sales, payment = data
#         print(f"{category}\t{sales}")

#!/usr/bin/env python
import sys

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 6:
        raise ValueError(f"Expected 6 fields, got {len(data)}: {line.strip()}")
    date, time, item, category, sales, payment = data
    print(f"{category}\t{sales}")