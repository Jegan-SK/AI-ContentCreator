import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# --------------------------------------------------
# Configuration
# --------------------------------------------------

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("GEMINI_API_KEY is not configured. Please add it to your .env file.")
    st.stop()

client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-3.5-flash"


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Content Creator Suite",
    page_icon="✍️",
    layout="wide"
)


# --------------------------------------------------
# Custom Styling
# --------------------------------------------------

st.markdown(
    """
    <style>
        .main-title {
            font-size: 42px;
            font-weight: 700;
            text-align: center;
            margin-bottom: 5px;
        }

        .subtitle {
            text-align: center;
            color: #777;
            font-size: 18px;
            margin-bottom: 30px;
        }

        .content-box {
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #ddd;
            background-color: #fafafa;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    '<div class="main-title">✍️ AI Content Creator Suite</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Create professional content for social media, email, blogs and presentations using AI.'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# Sidebar Settings
# --------------------------------------------------

with st.sidebar:
    st.header("⚙️ Content Settings")

    content_type = st.selectbox(
        "Choose content type",
        [
            "LinkedIn Post",
            "Instagram Caption",
            "Twitter/X Post",
            "Email Draft",
            "Blog Outline",
            "Presentation Content"
        ]
    )

    tone = st.selectbox(
        "Choose tone",
        [
            "Professional",
            "Casual"
        ]
    )

    emoji_mode = st.toggle(
        "😊 Emoji Mode",
        value=True
    )

    st.divider()

    st.markdown("### ✨ Supported Content")
    st.markdown(
        """
        - 💼 LinkedIn Posts
        - 📸 Instagram Captions
        - 🐦 Twitter/X Posts
        - 📧 Email Drafts
        - 📝 Blog Outlines
        - 📊 Presentation Content
        """
    )


# --------------------------------------------------
# Input Section
# --------------------------------------------------

st.subheader("📝 Enter Your Topic")

topic = st.text_area(
    "What would you like to create content about?",
    placeholder=(
        "Example: Artificial Intelligence in Education\n\n"
        "You can also provide additional details, target audience, "
        "key points, or requirements."
    ),
    height=160
)


# --------------------------------------------------
# Prompt Generator
# --------------------------------------------------

def build_prompt(content_type, topic, tone, emoji_mode):

    emoji_instruction = (
        "Use relevant emojis naturally where appropriate."
        if emoji_mode
        else "Do not use emojis."
    )

    tone_instruction = (
        "Use a professional, polished and business-appropriate tone."
        if tone == "Professional"
        else "Use a friendly, natural and conversational tone."
    )

    prompts = {

        "LinkedIn Post": f"""
You are an expert LinkedIn content writer.

Create a high-quality LinkedIn post based on the following topic:

{topic}

Requirements:
- Make the opening sentence attention-grabbing.
- Keep the content useful and engaging.
- Use short paragraphs for readability.
- Include relevant insights or takeaways.
- Add a suitable call-to-action at the end.
- Avoid unnecessary filler.
- Do not include a title such as "LinkedIn Post".
- {tone_instruction}
- {emoji_instruction}

Return only the final LinkedIn post.
""",

        "Instagram Caption": f"""
You are an expert social media content creator.

Create an engaging Instagram caption based on:

{topic}

Requirements:
- Start with an interesting hook.
- Keep it concise and engaging.
- Make it suitable for Instagram.
- Include a call-to-action.
- Add relevant hashtags at the end.
- Do not write "Instagram Caption" as a heading.
- {tone_instruction}
- {emoji_instruction}

Return only the final caption.
""",

        "Twitter/X Post": f"""
You are an expert Twitter/X content writer.

Create a concise and engaging Twitter/X post based on:

{topic}

Requirements:
- Make the message clear and impactful.
- Keep it concise enough for a standard Twitter/X post.
- Focus on one strong idea.
- Avoid unnecessary explanation.
- {tone_instruction}
- {emoji_instruction}

Return only the final Twitter/X post.
""",

        "Email Draft": f"""
You are an expert professional email writer.

Create a complete email based on:

{topic}

Requirements:
- Include an appropriate subject line.
- Include a professional greeting.
- Clearly communicate the main message.
- Include an appropriate closing.
- Keep the email concise and natural.
- Do not invent specific names or personal details.
- {tone_instruction}
- {emoji_instruction}

Return only the completed email.
""",

        "Blog Outline": f"""
You are an expert blog content strategist.

Create a detailed blog outline based on:

{topic}

Requirements:
- Create a compelling blog title.
- Include an introduction section.
- Create logical main sections.
- Add useful subsections where appropriate.
- Include key points that should be discussed under each section.
- Include a conclusion.
- Make the structure suitable for a complete blog article.
- {tone_instruction}
- {emoji_instruction}

Return only the blog outline.
""",

        "Presentation Content": f"""
You are an expert presentation content creator.

Create presentation content based on:

{topic}

Requirements:
- Create a suitable presentation title.
- Organize the content into clear slides.
- Give each slide a concise title.
- Provide useful bullet points for every slide.
- Maintain a logical flow from introduction to conclusion.
- Keep slide content concise enough for presentation use.
- Include a conclusion or final takeaway.
- {tone_instruction}
- {emoji_instruction}

Return only the presentation content.
"""
    }

    return prompts[content_type]


# --------------------------------------------------
# Generate Content
# --------------------------------------------------

if st.button("✨ Generate Content", type="primary", use_container_width=True):

    if not topic.strip():
        st.warning("Please enter a topic before generating content.")
        st.stop()

    prompt = build_prompt(
        content_type,
        topic,
        tone,
        emoji_mode
    )

    with st.spinner("Generating your content..."):

        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )

            generated_content = response.text

            if not generated_content:
                st.error("The AI returned an empty response.")
                st.stop()

            # Store content in session state
            st.session_state["generated_content"] = generated_content
            st.session_state["content_type"] = content_type

        except Exception as e:
            st.error(
                "Something went wrong while generating the content."
            )
            st.exception(e)


# --------------------------------------------------
# Output Section
# --------------------------------------------------

if "generated_content" in st.session_state:

    st.divider()

    st.subheader(
        f"✨ Generated {st.session_state['content_type']}"
    )

    generated_content = st.session_state["generated_content"]

    st.text_area(
        "Your Content",
        value=generated_content,
        height=400
    )

    # Character count
    character_count = len(generated_content)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Character Count",
            character_count
        )

    with col2:
        word_count = len(generated_content.split())

        st.metric(
            "Word Count",
            word_count
        )

    # Download button
    st.download_button(
        label="⬇️ Download Content",
        data=generated_content,
        file_name="generated_content.txt",
        mime="text/plain",
        use_container_width=True
    )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "AI Content Creator Suite • Powered by Gemini & Streamlit"
)