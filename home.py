from datetime import datetime
import streamlit as st

st.title("Personality, Behaviour Analysis and Authorship & Services")

col1, col2 = st.columns(2)

with col1:
  st.markdown('<h2><a href="persity" target="_self" style="text-decoration: none;">Personality & Behaviour Analysis</a></h2>', unsafe_allow_html=True)
  st.write("A simple tool to understand yourself")
  st.write("When someone asks you, who you are and you are left wondering, who you really are...")
  st.write("Check this out at:")
  st.page_link(
      "persity_app.py", label="Personality & Behaviour Analysis", icon="🧠"
  )
  st.write("For more information or a further dialog on introspection, you can reach out to us at Persity at [piravi.theauthor@gmail.com](mailto:piravi.theauthor@gmail.com)")

with col2:
  st.markdown('<h2><a href="authorship" target="_self" style="text-decoration: none;">Authorship & Services</a></h2>', unsafe_allow_html=True)

  st.write("A book to see where it all started")
  st.write("Check out this [The Autobiography of a Rock](https://store.pothi.com/book/piravi-autobiography-rock/) or [On Amazon](https://www.amazon.com/dp/B0HGFTF6RZ)")
  st.write("The art of introspection is really difficult. That is where [Persity](persity) comes in...")
  st.write("But there are other books too!")
  st.write("A cute little children's book [The Little Swan at Dawn](https://www.amazon.com/dp/B0HL6BWYFC) or on [Pothi for Indian readers](https://store.pothi.com/book/piravi-the-little-swan-dawn-1/)")
  st.write("And to top it all, I can offer to write a small children's book, like [The Little Swan at Dawn](https://www.amazon.com/dp/B0HL6BWYFC) tailored to your needs. You can have your own dedication, to make it a very special and personalised gift")
  st.write("This is not ghost writing but books written for children as a gift from someone who cares. You can have your name as the author too, if you like.") 
  st.write("For more information or a further dialog on personalised story telling ideas, you can reach out to [piravi.theauthor@gmail.com](mailto:piravi.theauthor@gmail.com)")
