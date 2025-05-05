import pandas as pd
import streamlit as st 


def top_locations(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    grouped = violations_df.groupby("location", as_index=False)["amount"].sum()
    result = grouped[grouped["amount"] >= threshold].sort_values(by="amount", ascending=False)
    return result


def top_locations_mappable(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    top = top_locations(violations_df, threshold)
    coords = violations_df.drop_duplicates("location")[["location", "lat", "lon"]]
    merged = pd.merge(top, coords, on="location", how="left")
    return merged[["location", "lat", "lon", "amount"]]



def tickets_in_top_locations(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    top = top_locations(violations_df, threshold)
    return violations_df[violations_df["location"].isin(top["location"])]



if __name__ == '__main__':
    '''
    Main ETL job. 
    '''
    st.title("Running Parking Ticket ETL")
    st.write("Loading CSV...")

    df = pd.read_csv("./cache/final_cuse_parking_violations.csv")
    st.write("Data loaded!")

    top = top_locations(df)
    top.to_csv("./cache/top_locations.csv", index=False)
    st.write("Saved top_locations.csv")

    map_data = top_locations_mappable(df)
    map_data.to_csv("./cache/top_locations_mappable.csv", index=False)
    st.write("Saved top_locations_mappable.csv")

    filtered = tickets_in_top_locations(df)
    filtered.to_csv("./cache/tickets_in_top_locations.csv", index=False)
    st.write("Saved tickets_in_top_locations.csv")

    st.success("ETL Complete ✅")