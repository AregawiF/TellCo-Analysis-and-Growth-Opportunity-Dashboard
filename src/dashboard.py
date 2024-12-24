import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

@st.cache_data
def load_data():
    # Replace with your dataset path
    data = pd.read_csv("./src/data/aggregated_user_experience.csv")
    return data

# Visualization functions
def user_overview_analysis(data):
    st.title("User Overview Analysis")

    # Distribution of Avg_TCP_Retransmission
    st.subheader("Distribution of Avg_TCP_Retransmission")
    fig, ax = plt.subplots()
    sns.histplot(data['Avg_TCP_Retransmission'], bins=10, ax=ax, kde=True, color='blue')
    st.pyplot(fig)

    # Distribution of Avg_RTT
    st.subheader("Distribution of Avg_RTT")
    fig, ax = plt.subplots()
    sns.histplot(data['Avg_RTT'], bins=10, ax=ax, kde=True, color='green')
    st.pyplot(fig)

    # Distribution of Avg_Throughput
    st.subheader("Distribution of Avg_Throughput")
    fig, ax = plt.subplots()
    sns.histplot(data['Avg_Throughput'], bins=10, ax=ax, kde=True, color='purple')
    st.pyplot(fig)

    # Most Common Handset
    st.subheader("Most Common Handset")
    handset_counts = data['Most_Common_Handset'].value_counts().head(10)
    st.bar_chart(handset_counts)


def user_engagement_analysis(data):
    st.title("User Engagement Analysis")
    st.write("How users interact with the platform.")

    # Display dataset columns
    st.subheader("Dataset Columns")

    # Analyze Avg_TCP_Retransmission
    st.subheader("Average TCP Retransmission Analysis")
    fig_tcp = px.histogram(
        data,
        x="Avg_TCP_Retransmission",
        nbins=20,
        title="Distribution of Average TCP Retransmission",
        labels={"Avg_TCP_Retransmission": "Average TCP Retransmission"},
    )
    st.plotly_chart(fig_tcp)

    # Analyze Avg_RTT
    st.subheader("Average RTT Analysis")
    fig_rtt = px.histogram(
        data,
        x="Avg_RTT",
        nbins=20,
        title="Distribution of Average RTT",
        labels={"Avg_RTT": "Average RTT (ms)"},
    )
    st.plotly_chart(fig_rtt)

    # Analyze Avg_Throughput
    st.subheader("Average Throughput Analysis")
    fig_throughput = px.histogram(
        data,
        x="Avg_Throughput",
        nbins=20,
        title="Distribution of Average Throughput",
        labels={"Avg_Throughput": "Average Throughput (Mbps)"},
    )
    st.plotly_chart(fig_throughput)

    # Analyze Most Common Handset
    st.subheader("Most Common Handsets")
    handset_counts = data["Most_Common_Handset"].value_counts().head(10)
    fig_handset = px.bar(
        handset_counts,
        x=handset_counts.index,
        y=handset_counts.values,
        title="Top 10 Most Common Handsets",
        labels={"x": "Handset Model", "y": "Count"},
    )
    st.plotly_chart(fig_handset)



def experience_analysis(data):
    st.title("Experience Analysis")
    st.write("Insights on user experience metrics.")

    # Check if necessary columns are available
    if 'Avg_TCP_Retransmission' in data.columns and 'Avg_Throughput' in data.columns:
        # Plot Avg_TCP_Retransmission vs. Avg_Throughput
        st.subheader("TCP Retransmission vs. Throughput")
        fig, ax = plt.subplots()
        sns.scatterplot(
            x='Avg_TCP_Retransmission',
            y='Avg_Throughput',
            data=data,
            ax=ax,
            hue=data['Most_Common_Handset'] if 'Most_Common_Handset' in data.columns else None,
            palette='coolwarm'
        )
        ax.set_title("Relationship Between TCP Retransmission and Throughput")
        ax.set_xlabel("Average TCP Retransmission")
        ax.set_ylabel("Average Throughput (Mbps)")
        st.pyplot(fig)
    else:
        st.error("Required columns ('Avg_TCP_Retransmission', 'Avg_Throughput') are missing from the dataset.")

    # Analyze RTT (Round Trip Time)
    if 'Avg_RTT' in data.columns:
        st.subheader("Distribution of Average RTT")
        fig_rtt, ax_rtt = plt.subplots()
        sns.histplot(data['Avg_RTT'], bins=20, ax=ax_rtt, kde=True, color='blue')
        ax_rtt.set_title("Distribution of Average RTT")
        ax_rtt.set_xlabel("Average RTT (ms)")
        st.pyplot(fig_rtt)
    else:
        st.error("The column 'Avg_RTT' is missing from the dataset.")

    # Summary of experience
    if 'Avg_Throughput' in data.columns:
        avg_throughput = data['Avg_Throughput'].mean()
        st.subheader("Summary of User Experience Metrics")
        st.metric(label="Average Throughput (Mbps)", value=f"{avg_throughput:.2f}")
    else:
        st.error("The column 'Avg_Throughput' is missing from the dataset.")


def satisfaction_analysis(data):
    st.title("Satisfaction Analysis")
    st.write("Insights on user satisfaction metrics.")

    # Check if SatisfactionRating exists
    if 'SatisfactionRating' in data.columns:
        st.subheader("Satisfaction Ratings Distribution")
        fig = px.pie(data, names='SatisfactionRating', title="Satisfaction Ratings Distribution")
        st.plotly_chart(fig)
    else:
        # Use alternative metrics for analysis
        st.subheader("Alternative Satisfaction Metric: Average Throughput")
        if 'Avg_Throughput' in data.columns:
            fig = px.histogram(data, x='Avg_Throughput', nbins=20, title="Distribution of Average Throughput")
            st.plotly_chart(fig)
        else:
            st.error("No suitable columns found for satisfaction analysis. Please ensure the dataset contains relevant metrics.")


# Main Streamlit app
def main():
    st.sidebar.title("Navigation")
    pages = {
        "User Overview Analysis": user_overview_analysis,
        "User Engagement Analysis": user_engagement_analysis,
        "Experience Analysis": experience_analysis,
        "Satisfaction Analysis": satisfaction_analysis,
    }

    # Sidebar selection
    page = st.sidebar.radio("Go to:", list(pages.keys()))

    # Load the data
    data = load_data()

    # Render the selected page
    pages[page](data)

if __name__ == "__main__":
    main()
