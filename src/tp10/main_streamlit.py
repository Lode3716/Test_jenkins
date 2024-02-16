"""
   
 auth : l.devigne

"""
import streamlit as st
import pandas as pd
from UserDAO import UserDao

def main():
    st.set_page_config(layout="wide")
    st.button("Reset", type="primary")
    if st.button('Say hello'):
        st.write('Why hello there')
    else:
        st.write('Goodbye')

    with UserDao("users_db.db") as dao:
        users = list(dao.findAll())

    df = pd.DataFrame(users)
    # st.table(users)
    #
    edited_df = st.data_editor(df)
    #
    edited_df.loc[edited_df["email"].idxmax()]["gender"]



if __name__ == '__main__':
    main()
