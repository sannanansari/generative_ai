import streamlit as st
from datetime import datetime
#from yt_summerization import generate_yt_summerization, generate_linkedin_post


import streamlit as st
from datetime import datetime

# ================== Mock Backend Functions ==================
def generate_linkedin_post(youtube_url, style, tone, hashtags_num, add_hashtags, call_to_action, max_words):
    """Simulates LinkedIn post generation. Replace with real model call."""
    return {
        "hook": "🚀 Learn faster with AI!",
        "body": "In this video, we explored how to use transformers for NLP tasks...",
        "cta": "👉 Watch the full video now!" if call_to_action == "Yes" else None,
        "hashtags": ["#AI", "#MachineLearning", "#Productivity"] if add_hashtags == "Yes" else []
    }

def generate_summary(youtube_url):
    """Simulates YouTube transcript summarization. Replace with real model call."""
    return "This video explains how transformers power modern NLP tasks, covering attention, embeddings, and real-world use cases."

# ================== Streamlit App ==================
st.set_page_config(page_title="AI Content Generator", layout="wide")

st.title("📝 AI Content Generator")

# Create Tabs
tab1, tab2 = st.tabs(["💼 LinkedIn Post Generator", "📄 Summary Generator"])

# ---------------- TAB 1: LinkedIn Post Generator ----------------
with tab1:
    st.header("Generate LinkedIn Post")

    col1, col2 = st.columns([1.2, 2])

    # LEFT: Input form
    with col1:
        st.subheader("🔹 Input Section")

        with st.form("post_form"):
            youtube_url = st.text_input("Enter YouTube URL for Post")
            style = st.selectbox("Select Style", ["-- Select Style --", "Educational", "Politics"])
            tone = st.selectbox("Select Tone", ["-- Select Tone --", "Professional", "Polite", "Friendly"])
            hashtags_num = st.number_input("Number of Hashtags", min_value=1, max_value=10, step=1)
            add_hashtags = st.radio("Add Hashtags?", ["Yes", "No"], horizontal=True)
            call_to_action = st.radio("Add Call to Action?", ["Yes", "No"], horizontal=True)
            max_words = st.number_input("Max Word Count", min_value=50, max_value=1000, value=300, step=50)

            generate_post_btn = st.form_submit_button(
                "Generate Post",
                use_container_width=True
            )

        # ✅ Validation after submit
        if generate_post_btn:
            if not youtube_url.strip() or style == "-- Select Style --" or tone == "-- Select Tone --":
                st.error("⚠️ Please fill all required fields before generating the post.")
            else:
                with st.spinner("Generating LinkedIn post..."):
                    st.session_state.linkedin_post = generate_linkedin_post(
                        youtube_url, style, tone, hashtags_num, add_hashtags, call_to_action, max_words
                    )

    # RIGHT: Output Preview
    with col2:
        st.subheader("📢 Generated LinkedIn Post")

        if "linkedin_post" in st.session_state and st.session_state.linkedin_post:
            response = st.session_state.linkedin_post
            # hashtags_text = " ".join(response["hashtags"]) if response["hashtags"] else ""
            # cta_text = response["cta"] if response["cta"] else ""
            if response:
                st.markdown("#### Hook")
                st.info(response["hook"])

                st.markdown("#### Body")
                st.write(response["body"])

                if response["cta"]:
                    st.markdown("#### Call To Action")
                    st.success(response["cta"])

                if response["hashtags"]:
                    st.markdown("#### Hashtags")
                    st.write(" ".join(response["hashtags"]))

            # linkedin_post = f"""
            # {response['hook']}

            # {response['body']}

            # {cta_text}

            # {hashtags_text}
            # """
        else:
            st.info("ℹ️ Fill the form on the left and click **Generate Post** to see the preview here.")

# ---------------- TAB 2: Summary Generator ----------------
with tab2:
    st.header("Generate Summary")

    with st.form("summary_form"):
        youtube_url_summary = st.text_input("Enter YouTube URL for Summary")
        summary_btn = st.form_submit_button("Generate Summary")

    if summary_btn:
        if not youtube_url_summary.strip():
            st.error("❌ Please enter a YouTube URL.")
        else:
            st.session_state.summary = generate_summary(youtube_url_summary)

    if "summary" in st.session_state and st.session_state.summary:
        st.subheader("📝 Generated Summary")
        st.text_area("Summary", st.session_state.summary, height=200)







# st.set_page_config(page_title="YouTube → LinkedIn AI App", layout="wide")

# st.title("🎥 YouTube to LinkedIn Post Generator")

# # Tabs for scalable layout
# tab1, tab2 = st.tabs(["💼 Post Generator", "📄 Summarizer"])


# # ================== TAB 2: Post Generator ==================
# with tab1:
#     st.header("Generate LinkedIn Post")

#     with st.form("post_form"):
#         youtube_url = st.text_input("Enter YouTube URL for Post")
#         style = st.selectbox("Select Style", ["Educational", "Politics"])
#         tone = st.selectbox("Select Tone", ["Professional", "Polite", "Friendly"])
#         #hashtags_num = st.number_input("Number of Hashtags", min_value=1, max_value=10, step=1)
#         add_emojis = st.radio("Add Emojis?", ["Yes", "No"], horizontal=True)
#         add_hashtags = st.radio("Add Hashtags?", ["Yes", "No"], horizontal=True)
#         call_to_action = st.radio("Add Call to Action?", ["Yes", "No"], horizontal=True)
#         max_words = st.number_input("Max Word Count", min_value=50, max_value=1000, value=300, step=50)

#         request_data = {
#             "youtube_url":youtube_url,
#             "style": style,
#             "tone":tone,
#             "add_hashtags": add_hashtags,
#             "call_to_action": call_to_action,
#             "max_words": max_words,
#             "add_emojis": add_emojis,
#         }
#         print(request_data)
#         generate_btn = st.form_submit_button("Generate Post")

#         if generate_btn:
#             if not youtube_url.strip() or not style or not tone:
#                 st.error("❌ All inputs are mandatory. Please fill all fields.")
#             else:
#                 post_response = generate_linkedin_post(request_data)
#                 print("UI data-----{post_response}")
#                 hashtags_text = " ".join(post_response["hashtags"]) if post_response["hashtags"] else ""
#                 cta_text = post_response["call_to_action"] if post_response["call_to_action"] else ""

#                 # Assemble LinkedIn post
#                 linkedin_post_data = f"""
#                 {post_response['hook']}

#                 {post_response['body']}

#                 {cta_text}

#                 {hashtags_text}
#                 """

#                 # LinkedIn-style card UI
#                 st.success("✅ LinkedIn Post generated successfully!")
#                 with st.container():
#                     st.markdown(
#                         f"""<div style="
#                             border:1px solid #ddd;
#                             border-radius:10px;
#                             padding:15px;
#                             background-color:white;
#                             box-shadow:2px 2px 8px rgba(0,0,0,0.1);
#                             ">
#                             <div style="display:flex; align-items:center;">
#                                 <img src="https://static.vecteezy.com/system/resources/previews/000/439/863/original/vector-users-icon.jpg" 
#                                     width="40" style="border-radius:50%; margin-right:10px;">
#                                 <div>
#                                     <strong>Generated Post</strong><br>
#                                     <span style="color:gray; font-size:12px;">AI Assistant • {datetime.now().strftime("%b %d, %Y")}</span>
#                                 </div>
#                             </div>
#                             <div style="margin-top:15px; font-size:15px; line-height:1.5;">
#                                 {linkedin_post_data}
#                             </div>
#                             <hr>
#                             <div style="display:flex; justify-content:space-around; color:gray; font-size:14px;">
#                                 👍 Like &nbsp;&nbsp; 💬 Comment &nbsp;&nbsp; 🔄 Share &nbsp;&nbsp; ✉ Send
#                             </div>
#                         </div>
#                         """,
#                         unsafe_allow_html=True
#                     )

# # ================== TAB 1: Summarizer ==================
# with tab2:
#     st.header("Summarize YouTube Content")

#     with st.form("summary_form"):
#         youtube_url = st.text_input("Enter YouTube URL")
#         summary_type = st.radio(
#             "Choose summary type",
#             ["Short Summary", "Bullet Summary", "Detailed Summary"]
#         )
#         summarize_btn = st.form_submit_button("Summarize")

#         if summarize_btn:
#             if not youtube_url.strip():
#                 st.error("❌ Please provide a YouTube link.")
#             else:
#                 summary = generate_yt_summerization(youtube_url, summary_type)
#                 st.success("✅ Summary generated successfully!")
#                 st.text_area("Summary Output", summary, height=200)
