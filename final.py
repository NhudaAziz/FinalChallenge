import pandas as pd 
import plotly.express as px  
import streamlit as st  

st.set_page_config(page_title="Sales Analysis", page_icon=":keyboard:", layout="wide")

# ---- READ EXCEL ----
# @st.cache
def get_data_from_excel():
    df = pd.read_excel(
        io="sales.xlsx",
        engine="openpyxl",
        sheet_name="Sales",
        skiprows=3,
        usecols="B:R",
        nrows=1000,
    )
    # Add 'hour' column to dataframe
    df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df

df = get_data_from_excel()

# ---- SIDEBAR ----
st.sidebar.header("Choose Filter:")
city = st.sidebar.multiselect(
    "Select the City:",
    options=df["City"].unique(),
    default=df["City"].unique()
)

customer_type = st.sidebar.multiselect(
    "Select the Customer Type:",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique(),
)

gender = st.sidebar.multiselect(
    "Select the Gender:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

df_selection = df.query(
    "City == @city & Customer_type ==@customer_type & Gender == @gender"
)

# ---- MAINPAGE ----
st.title("Supermarket Sales Analysis")
st.markdown("##")

total_sales = int(df_selection["Total"].sum())
average_sale_by_transaction = round(df_selection["Total"].mean(), 2)

left_column, right_column = st.columns(2)
with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"$ {total_sales:,}")
with right_column:
    st.subheader("Average Sales Per Transaction:")
    st.subheader(f"$ {average_sale_by_transaction}")

st.markdown("""---""")

# SALES BY PRODUCT LINE [BAR CHART]
sales_by_product_line = (
    df_selection.groupby(by=["Product line"]).sum()[["Total"]].sort_values(by="Total")
)
fig_product_sales = px.line(
    sales_by_product_line,
    x="Total",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Sales by Product Line</b>",
    color_discrete_sequence=["#db08e9"] * len(sales_by_product_line),
    template="plotly_white",
)
fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# SALES BY HOUR [BAR CHART]
sales_by_hour = df_selection.groupby(by=["hour"]).sum()[["Total"]]
fig_hourly_sales = px.scatter(
    sales_by_hour,
    x=sales_by_hour.index,
    y="Total",
    title="<b>Sales by hour</b>",
    color_discrete_sequence=["#04fbf0"] * len(sales_by_hour),
#     color="City"
    template="plotly_white",
    trendline="ols", 
    trendline_scope="overall"
)
fig_hourly_sales.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

# fig_hourly_sales
# fig_product_sales

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
right_column.plotly_chart(fig_product_sales, use_container_width=True)

# SALES BY QUANTITY PRODUCT [BAR CHART]
sales_by_pay_line = (
    df_selection.groupby(by=["Payment"]).sum()[["Total"]].sort_values(by="Total")
)
fig_pay_sales = px.bar(
    sales_by_pay_line,
    x="Total",
    y=sales_by_pay_line.index,
    orientation="h",
    title="<b>Sales by Payment Type</b>",
    color_discrete_sequence=["#ff4242"] * len(sales_by_pay_line),
#     color="Gender"
    template="plotly_white",
)
fig_pay_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# GROSS INCOME
sales_gross = df_selection.groupby(by=["gross income"]).sum()[["Total"]]
fig_gross_sales = px.scatter(
    sales_gross,
    x=sales_gross.index,
    y="Total",
    title="<b>Sales vs Gross Income</b>",
    color_discrete_sequence=["#fbff07"] * len(sales_gross),
#     color="City"
    template="plotly_white",
)
fig_gross_sales.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_pay_sales, use_container_width=True)
right_column.plotly_chart(fig_gross_sales, use_container_width=True)
