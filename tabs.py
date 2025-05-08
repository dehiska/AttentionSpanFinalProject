import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
import Graph1, Graph2, Graph3, Graph4, Graph5
url1 = 'data.csv'
df1 = pd.read_csv(url1)
url2 = 'screen_time.csv'
df2 = pd.read_csv(url2)


#df['tip_pct'] = df['tip'] / df['total_bill'] * 100
#st.title('Restaurant spending')

#fig1 = plt.figure()
#ax1 = fig1.add_subplot()
#ax1.set_xlabel('Bill ($)')
#ax1.set_title('Bill amount distribution')
#ax1.hist(df['total_bill'], bins = 20, color='red', alpha=0.5)


#Graph 2 Tab 2
fig2 = Graph2.makeGraph2()

#Graph 3 Tab 3
fig3 = Graph3.makeGraph3()

#Graph 4 Tab 4
fig4 = Graph4.makeGraph4()

#Graph 5 Tab 5
fig5_1 = Graph5.makeGraph5_1()
fig5_2 = Graph5.makeGraph5_2()



tab1, tab2, tab3, tab4, tab5 = st.tabs(["Screentime for School", "Age vs. Screentime", "Kids vs. Adults in Attention Span", "Who most distracted?", "Are productivity apps helpful?"])

with tab1:
    st.subheader('Which age group gets most distracted from notifications?')

    # Collect user input first
    purpose = st.radio('Select Purpose', ('Educational', 'Recreational', "Both"))
    time = st.radio("Select which days of the week", ("Weekdays", "Weekends", "Both"))

    # Then show submit button at the bottom
    if st.button("Submit"):
        if purpose == 'Educational' and time == 'Weekdays':
            st.pyplot(Graph1.makeGraph1_1())

        elif purpose == 'Educational' and time == 'Weekends':
            st.pyplot(Graph1.makeGraph1_2())

        elif purpose == 'Educational' and time == 'Both':
            st.pyplot(Graph1.makeGraph1_3())

        elif purpose == 'Recreational' and time == 'Weekdays':
            st.pyplot(Graph1.makeGraph1_4())

        elif purpose == 'Recreational' and time == 'Weekends':
            st.pyplot(Graph1.makeGraph1_5())

        elif purpose == 'Recreational' and time == 'Both':
            st.pyplot(Graph1.makeGraph1_6())

        elif purpose == 'Both' and time == 'Both':
            st.pyplot(Graph1.makeGraph1_7())

        elif purpose == 'Both' and time == 'Weekdays':
            st.pyplot(Graph1.makeGraph1_8())

        elif purpose == 'Both' and time == 'Weekends':
            st.pyplot(Graph1.makeGraph1_9())

                  

with tab2:
   st.pyplot(fig2)

with tab3:
   st.pyplot(fig3)


with tab4:
   st.pyplot(fig4)


with tab5:
   st.pyplot(fig5_1)
   st.pyplot(fig5_2)

