import streamlit as st
import io
from scraper import get_stock_data

st.title("📈 Stock Market Dashboard (Groww Data)")
st.write("Real-time stock price scraping using Selenium")

if st.button("Scrape Latest Data"):
    with st.spinner("Scraping..."):
        df = get_stock_data()
        st.success("Scraping complete!")
        st.dataframe(df)
        # Convert DataFrame to Excel in memory
        excel_buffer = io.BytesIO()
        df.to_excel(excel_buffer, index=False, engine='openpyxl')
        excel_buffer.seek(0)

# Display download button
        st.download_button(
            label="Download as Excel",
            data=excel_buffer,
            file_name="stocks.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

