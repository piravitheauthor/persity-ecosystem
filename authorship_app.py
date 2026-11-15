from datetime import datetime
import streamlit as st

# --- STREAMLIT WEB APP INTERFACE ---

st.title("Authorship and Services")

st.header("The Autobiography of a Rock")
st.subheader("A Fable of Time, Human Fate and Ancient Wisdom")

st.write("Avaliable on [Amazon](https://www.amazon.com/dp/B0HGFTF6RZ) internationally and on [Pothi](https://store.pothi.com/book/piravi-autobiography-rock/) in India")

st.image(
    "BookCover.jpg",
    caption="The Autobiography of a Rock",
    link="https://www.amazon.com/dp/B0HGFTF6RZ",
    width=250
)

st.header("The Little Swan at Dawn")
st.subheader("A heartwarming story about patience, perseverance, and the magic of a brand-new day")

st.write("Avaliable on [Amazon](https://www.amazon.com/dp/B0HL6BWYFC) internationally and on [Pothi](https://store.pothi.com/book/piravi-the-little-swan-dawn-1/) in India")

st.image(
    "SwanAtDawn.png",
    caption="The Little Swan at Dawn",
    link="https://www.amazon.com/dp/B0HL6BWYFC",
    width=250
)



st.subheader("Services and personalised gift idea")
st.write("Now imagine a book like the The Little Swan at Dawn. Present it to your favourite nieces or nephews or grandchildren, with a dedication page, specifically made for them")
st.write("I got this idea after I saw the book, The Little Swan at Dawn, selling so well on [Amazon](https://www.amazon.com/dp/B0HL6BWYFC). I wish I could thank all the people who bought it. And I have no idea how they came to know of this, as I hardly told anyone about it. I wanted to share the joy by starting this small inexpensive service to make it as memorable for others, as it was for me.")
st.write("Create a special story tailored for the little one at home, and give it as a return gift at their birthday parties. It is a memorable personalised keepsake, that will last forever (or at least a very very long time)")

st.write(
    "Write to us at [piravi.theauthor@gmail.com](mailto:piravi.theauthor@gmail.com) to learn more on what we can offer"
)
