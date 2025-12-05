import validators
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

#streamlit app
st.set_page_config(page_title="Langchain: Summarize Text From YT and Website",page_icon="🦜")
st.title("🦜 Langchain: Summarize Text From YT and Website")
st.subheader('Summarize URL')

##Get the groq api key and url (YT or website) to be summarized
with st.sidebar:
    groq_api_key=st.text_input("GROQ API KEY",value="",type="password")

generic_url=st.text_input("URL",label_visibility="collapsed")

chunk_prompt=ChatPromptTemplate.from_template("""
Summarize the following text clearly and concisely in 3 bullet points.
Text:
{text}
""")

final_prompt=ChatPromptTemplate.from_template("""
Combine all the chunk summaries below into a final polished summary.
The final summary must:

- Be 350 to 400 words
- Be organized into clear bullet points + small subsections if needed
- Remove repetitions
- Capture only the essential ideas

Chunk summaries:
{chunks}                               
""")

if st.button("Summarize the content from YT or Website"):
    ## validate all the inputs
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information")
    elif not validators.url(generic_url):
        st.error("Please Enter a valid URL")
    else:
        try:
            with st.spinner("Loading and Summarizing..."):
                ##loading the YT or website data
                if "youtube.com" in generic_url or "youtube.be" in generic_url:
                    loader=YoutubeLoader.from_youtube_url(generic_url,add_video_info=False)
                else:
                    loader=UnstructuredURLLoader(urls=[generic_url],ssl_verify=False,
                                                 headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"})
                data=loader.load()
                #remove empty documents
                data=[d for d in data if d.page_content.strip()]

                if not data:
                    st.error("Unable to extract content from this URL.")
                    st.stop()

                splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
                chunks=splitter.split_documents(data)
                
                llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama-3.1-8b-instant")

                ##chain for summarization
                chain=chunk_prompt|llm|StrOutputParser()
                chunk_summaries=[]

                for c in chunks:
                    text = c.page_content.strip()
                    if not text:
                        continue
                    try:
                        chunk_summaries.append(chain.invoke({"text": text}))
                    except Exception as e:
                        print("Chunk error:", e)
                        continue

                if not chunk_summaries:
                    st.error("Failed to summarize content.")
                    st.stop()

                final_chain=final_prompt|llm|StrOutputParser()    
                final_summary=final_chain.invoke({"chunks":"\n\n".join(chunk_summaries)})
                st.success(final_summary)

        except Exception as e:
            st.exception(f"Exception:{e}")