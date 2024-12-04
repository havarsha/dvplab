import pandas as pd
import plotly.express as px
dollar_conv = pd.read_csv('CUR_DLR_INR.csv')
fig=px.line(dollar_conv, x='DATE', y='RATE', title="1KI23CS175-varshaha")
fig.show()