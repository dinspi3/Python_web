import pandas as pd

# Python dict object
student_dict = {'Name': ['Joe', 'Nat'], 'Age': [20, 21], 'Marks': [85.10, 77.80]}
print(student_dict)

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print(student_df)