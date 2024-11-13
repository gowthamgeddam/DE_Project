import pandas as pd
import plotly.express as px
from conn import run_query
import streamlit as st
from logout import clear_session
from streamlit_option_menu import option_menu









def show_main_dashboard3():
        st.markdown(
            """
            <style>
                /* Container styling for each query */
                .query-container {
                    padding: 1rem;
                    margin: 1rem 0;
                    background-color: #f0f2f6; /* Light background for better contrast */
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Slight shadow for depth */
                }
                .header-text {
                    font-size: 1.2rem;
                    font-weight: bold;
                    color: #AEDBF0;
                    text-align: center;
                    margin-bottom: 1rem;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
        coln1, coln2 = st.columns([1, 1])

       
        ####################################################  Query5 ##############################################

        with coln1:
                # Initialize session state for pagination
                 if 'collab_offset' not in st.session_state:
                    st.session_state['collab_offset'] = 0

                # Number of records per page
                 records_per_page = 5

                # Query with pagination
                 def fetch_collaborations(offset, limit):
                    query = f"""
                        WITH DirectorActorCollab AS (
                            SELECT d.director_name, c.actor_name, COUNT(m.id) AS collab_count, MAX(f.revenue) AS highest_gross
                            FROM directed d
                            JOIN movie m ON d.id = m.id
                            JOIN movie_cast c ON m.id = c.id
                            JOIN finances f ON m.id = f.id
                            GROUP BY d.director_name, c.actor_name
                        )
                        SELECT director_name, actor_name, collab_count, highest_gross
                        FROM DirectorActorCollab
                        ORDER BY collab_count DESC
                        LIMIT {limit} OFFSET {offset};
                    """
                    return run_query(query)

                # Fetch data for the current page
                 data = fetch_collaborations(st.session_state['collab_offset'], records_per_page)
                 df = pd.DataFrame(data, columns=["Director", "Actor", "Collaboration Count", "Highest Gross"])
                 st.markdown('<div class="header-text">Collaboration Count and Highest Grossing Revenue for Top Director-Actor Pairs</div>', unsafe_allow_html=True)
                # Reshape the data for grouped bar chart
                 df_melted = df.melt(id_vars=["Director", "Actor"], 
                                    value_vars=["Collaboration Count", "Highest Gross"], 
                                    var_name="Metric", 
                                    value_name="Value")

                # Plot: Grouped Bar Chart
                 fig = px.bar(
                    df_melted, x="Actor", y="Value", color="Metric", barmode="group",
                    
                    labels={"Value": "Count / Revenue", "Actor": "Actor"}
                )
                 fig.update_layout(
                    plot_bgcolor="rgba(0,0,0,0)", 
                    xaxis=dict(showgrid=False),
                    yaxis_title="Value",
                    xaxis_title="Actor",
                )

                # Display the grouped bar chart
                 st.plotly_chart(fig, use_container_width=True)

                # Pagination controls
                 col1, col2, col3 = st.columns([1, 2, 1])
                 with col1:
                    if st.button("Previous Collaborations") and st.session_state['collab_offset'] >= records_per_page:
                        st.session_state['collab_offset'] -= records_per_page

                 with col3:
                    if st.button("Next Collaborations"):
                        st.session_state['collab_offset'] += records_per_page
                        
        ###############################################   end of Query5  ##############################################

        ###############################################    Query10  ##############################################
        

        ###############################################   end of Query10  ##############################################   
