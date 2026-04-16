import streamlit as st

st.header('URL Safety Checker')

link_in = st.text_input('Paste link here:')

if st.button("check"):
    if link_in == "":
        st.write('Please enter a link')
    else:
        s = 0 
        stuff = []

        if "@" in link_in:
            s += 1
            stuff.append('Has @')
            
        if len(link_in) > 30:
            s += 1
            stuff.append('Too long')
            
        if not link_in.startswith("https"):
            s += 1
            stuff.append("No https")

        low_link = link_in.lower()
        if 'login' in low_link or 'bank' in low_link:
            s += 1
            stuff.append('Weird keywords')

        if link_in.count('.') > 3:
            s += 1
            stuff.append('Lots of dots')

        if s == 0:
            st.success("Safe")
        elif s <= 2:
            st.warning("Kinda risky")
        else:
            st.error("Scam")

        st.write('Total risk:', s)

        if len(stuff) > 0:
            st.markdown('**Issues:**')
            for item in stuff:
                st.text('- ' + item)