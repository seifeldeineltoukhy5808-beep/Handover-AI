import streamlit as st

st.set_page_config(
    page_title="HandoverAI",
    page_icon="🏥")

st.title("🏥 HandoverAI")
st.write("Clinical handover assistant")

st.warning( "Prototype only. Use fictional data. "
    "All outputs require clinician review.")

notes = st.text_area(
    "Paste your shift notes:",
    height=200,
    placeholder="Enter fictional clinical notes..."
)

if st.button("Generate Handover"):
    if not notes.strip():
        st.error("Please enter some notes.")
    else:
        st.subheader("SBAR Handover")

        st.write("**Situation:**")
        st.write("Awaiting structured extraction")

        st.write("**Background:**")
        st.write("Awaiting structured extraction")

        st.write("**Assessment:**")
        st.write("Awaiting structured extraction")

        st.write("**Recommendation:**")
        st.write("Awaiting structured extraction")

        st.subheader("Original Notes")
        st.write(notes)