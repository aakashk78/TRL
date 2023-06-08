import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

#@st.cache_data
def load_data():
    data = pd.read_excel('Final Compendium.xlsx')
    return data

df = load_data()

trl_charac = pd.read_csv('TRL characteristics.csv')

tab1, tab2, tab3 = st.tabs(['Overview','Compendium of Technologies','Summary of TRL'])
#st.title('Techno-Commercial Assessment of TRL – 6 and above technologies developed in India, in academia, research labs and industry')

with tab1:
    st.markdown('<h1 style="text-align: center;">Techno-Commercial Assessment of TRL – 6 and above technologies developed in India</h1>',unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; font-size: 25px;">Electronics, Tele-communications and Manufacturing</h2>', unsafe_allow_html=True)
    #st.subheader('Electronics, Tele-communications and Manufacturing')

    st.header('Introduction')

    st.write('The Technology Readiness Level (TRL) is an effective tool for assessing the development and progress of technologies in many research areas. Since its inception, numerous government organizations, research institutions and industries worldwide have adopted TRLs. '
             'TRL provides a simple yet practical approach to understanding the maturity of available technologies, and their categorization is possible through these levels.')
    st.dataframe(trl_charac[['TECHNOLOGY READINESS LEVEL', 'CHARACTERISTIC']], use_container_width = True)
    st.write("Projects with low TRLs are associated with high risks due to uncertainty, the possibility of failure and the unavailability of necessary resources. Managers often need to identify appropriate technologies to achieve business goals. Thus, knowledge of TRLs for existing technologies is highly beneficial for reducing the project's overall risk by using well-adopted and widely tested alternatives. This can also be used effectively to understand the limitations of such alternatives and find ways to solve and overcome them for a particular use case.")
    col1,col2,col3 = st.columns([2,8,2])
    with col1:
        st.write('')
    with col2:
        st.image('./images/TRL.png')
    with col3:
        st.write('')

    st.write("This study aims to understand the status of technologies in leading academic institutions, research organizations and industries. A summary of the results achieved for the objectives proposed in this study is provided below.")

    st.subheader('Objectives')
    st.markdown('<h3 style="text-align: justify; font-size: 20px;">Objective 1: To conduct the case studies on success stories of the technologies(projects) which are in the TRL-6 and above in academia, research labs</h3>',unsafe_allow_html=True)

    st.write("A case study was conducted to understand the essential factors that help improve the TRL of technologies, thereby leading to successful commercialization. This study considers assistive technologies for people with disability being developed at the TTK Center for Rehabilitation Research and Device Development (R2D2) under Prof. Sujatha Srinivasan at IIT Madras. This study analyses the need for such technologies and the importance of customer-centric design and affordability to gain an edge over competitors in the market. It also highlights the importance of industry collaboration and innovation, vital for surpassing TRL6 and above, and how acquiring funds can be a challenge in developing novel technologies.")

    st.markdown('<h3 style="text-align: justify; font-size: 20px;">Objective 2: Barriers Hindering Commercialization of TRL 6 And Above Technologies</h3>',unsafe_allow_html=True)
    st.write("This study also focuses on the identification of barriers that hinder the commercialization of TRL6 and above technologies. This study aims to develop a Fuzzy Analytic Hierarchy Process (AHP) model for identifying the relative importance of the barriers. A fuzzy-AHP-based questionnaire was prepared for this study, and data was collected from the stakeholder's perspective wherein each criteria was compared based on the Saaty scale of 1 – 9 (1 – represents equal importance between the compared criteria, 9 – represents absolute relative importance). Based on the results of the analysis, the existence of an identical successfully commercialized project for a similar environment criterion has the highest weight compared to others. In contrast, indigenous barriers, system complexity, planning and review and validity of the assessment of TRL are considered to be the least essential barriers towards the commercialization of technologies")

    st.markdown('<h3 style="text-align: justify; font-size: 20px;">Objective 3: Artificial Intelligence-based approach for prediction of TRL</h3>',unsafe_allow_html=True)
    st.write("The current methodology involves a questionnaire-evaluation approach, followed by an expert to complete the assessment process. A significant disadvantage of this approach is its labour intensiveness for acquiring and processing data for numerous TRL indicators. This approach is also subjective and, thus, suffers from biases. Thus, there is scope for improvement in existing methodologies and novel approaches that mitigate subjectivity in TRLs. This work proposes a Natural Language Processing-based approach for classifying technologies depending on TRL from bibliometric data into Low, Medium and High TRL categories. Through this categorization, technologies in similar fields can be easily identified. Logistic Regression, Random Forest and Multinomial Naïve Bayes models were trained for the classification of data, and an accuracy of over 60% was achieved for these models.")

    st.markdown('<h3 style="text-align: justify; font-size: 20px;">Objective 4: Development of a database for TRL of projects in academia and research organizations. </h3>', unsafe_allow_html=True)
    st.write("This study consists of TRL data for over 850 funded projects across interdisciplinary research fields that are being developed in premier institutes across India. Of these, 706 projects are interdisciplinary, 122 are related to Electronics & Telecommunications, and 24 are related to Manufacturing. The variation of TRL in these projects over the years is also studied. ")

    st.markdown('<h3 style="text-align: justify; font-size: 20px;">Objective 5: Existing successful epitomes in Indian Institutes</h3>', unsafe_allow_html=True)
    st.write("Projects that have successfully achieved TRL6 and above were identified across various institutes. For the TRL data collected, 466 projects successfully reached TRL6 or above in 2020. To compare the variation in TRL, there were 206 projects above TRL6 in 2019. Older institutes lead significantly in the number of projects and the improvement in TRL of technologies based on the data collected. A summary of this data is provided in the submitted report. The database based on TRL data of these projects is currently being developed to help track the progress and maturity of technologies.")

    st.markdown('<h3 style="text-align: justify; font-size: 20px;">Objective 6: To develop policy recommendations </h3>', unsafe_allow_html=True)
    st.write("Policy recommendations are being developed based on the results of the analysis. It will help identify barriers hindering the commercialization of projects and also promote the collaboration of researchers working in similar and interdisciplinary fields of research to fast-track technology development. It is also helpful for funding agencies to organize data on ongoing / completed projects and assess outcomes.")



with tab2:
    st.header('Compendium of Technologies across institutions')
    st.write("The following compendium provides information of various technologies being developed across various instituions in India, alongwith their TRL and status of commercialization based on the Atal Ranking of Institutions on Innovation Achievements (ARIIA). This compendium consists of technologies from numerous interdisciplinary fields of research. The technologies are classified into three categories: Electronics & Telecommunications (ETC), Manufacturing (M), and Other based on their domain of application.")
    st.dataframe(df, use_container_width= True, height = 800)

with tab3:
    st.header('Summary of Technology Readiness Levels')

    def main():
        html_temp = """<div class='tableauPlaceholder' id='viz1686224709158' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;TR&#47;TRLSummary&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='TRLSummary&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;TR&#47;TRLSummary&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1686224709158');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else { vizElement.style.width='100%';vizElement.style.height='2027px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_temp)


    if __name__ == "__main__":
        main()