
import pandas as pd

df = pd.DataFrame()
df.info(memory_usage='deep')



for dtype in ['float','int','object']:
    selected_dtype = gl.select_dtypes(include=[dtype])
    mean_usage_b = selected_dtype.memory_usage(deep=True).mean()
    mean_usage_mb = mean_usage_b / 1024 ** 2
    print("Average memory usage for {} columns: {:03.2f} MB".format(dtype,mean_usage_mb))

# Output
# Average memory usage for float columns: 1.29 MB
# Average memory usage for int columns: 1.12 MB
# Average memory usage for object columns: 9.53 MB