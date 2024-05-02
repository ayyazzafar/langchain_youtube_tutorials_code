from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains import LLMChain 


# setup the opneai api key
openai_api_key = "sk-proj-asfasfdasfdasf"

#define the prompts
twitter_prompt = PromptTemplate(
    input_variables=["text"],
    template="""Please create an engaging Twitter thread based on the following text, breaking it down into multiple tweets of no more than 280 characters each, while maintaining the core message and including relevant hashtags:

{text}"""

) 


facebook_prompt = PromptTemplate(
    input_variables=["text"],
    template="""
    Create an attention-grabbing Facebook post based on the following text. Include a brief introduction, key points, and a call-to-action. Aim for a post length of around 100-200 words:

{text}
""")


linkedin_prompt = PromptTemplate(
    input_variables=["text"],
    template="""
    Using the following text, generate an informative and professional LinkedIn article. Structure the article with an engaging title, introduction, subheadings, bullet points, and a conclusion. The article should be between 500-800 words:

{text}
""")

youtube_prompt = PromptTemplate(
    input_variables=["text"],
    template="""Please create a YouTube video script based on the following text. Include an introduction, main content divided into logical sections, and a conclusion with a call-to-action. Use a conversational tone and aim for a script length of approximately 1000 words:

{text}"""
)


instagram_prompt = PromptTemplate(
    input_variables=["text"],
    template="""Generate an engaging Instagram caption based on the following text. Keep the caption concise (under 150 characters) and include relevant emojis and hashtags to increase visibility and engagement:

{text}"""
)

# Initialize the OpenAI language model
llm = OpenAI(openai_api_key=openai_api_key)

# Create LLMChains for each prompt
twitter_chain = LLMChain(llm=llm, prompt=twitter_prompt)
facebook_chain = LLMChain(llm=llm, prompt=facebook_prompt)
linkedin_chain = LLMChain(llm=llm, prompt=linkedin_prompt)
youtube_chain = LLMChain(llm=llm, prompt=youtube_prompt)
instagram_chain = LLMChain(llm=llm, prompt=instagram_prompt)


# Function to generate content based on input text and platform
def generate_content(text, platform):
    if platform == "twitter":
        return twitter_chain.invoke(text)
    elif platform == "facebook":
        return facebook_chain.invoke(text)
    elif platform == "linkedin":
        return linkedin_chain.invoke(text)
    elif platform == "youtube":
        return youtube_chain.invoke(text)
    elif platform == "instagram":
        return instagram_chain.invoke(text)
    else:
        raise ValueError(f"Unsupported platform: {platform}")


input_text=""""
Today, we’re thrilled to announce that enterprises can purchase LangSmith in the Azure Marketplace as an Azure Kubernetes Application. LangSmith is a unified DevOps platform for developing, collaborating, testing, and monitoring LLM applications, whether you’re building with LangChain or not. LangSmith has quickly become the platform of choice to help enterprises get their LLM-apps from prototype to production, and LangSmith customers such as Moody’s, Elastic, Rakuten, and BCG rely on the platform to build high quality genAI applications that scale.

“As a leader in innovation and technology, Moody’s prioritizes thorough testing and evaluation of our Generative AI-powered tools. In order to create applications that are reliable for the enterprise and our customers, LangSmith helps maintain engineering rigor throughout the development and testing phases, allowing us to stress test our LLM-powered applications well before we release them. This gives us confidence as we continue harnessing Generative AI in our mission to decode risk and unlock opportunity.” – Han-chung Lee, Director of Machine Learning at Moody’s.

We’re excited to lean into our collaboration with Microsoft by giving our joint customers an easier procurement option via Azure Marketplace, with a data security posture that satisfies even the most demanding infosec and compliance teams.

To learn more about LangSmith and the benefits that come with the Azure Marketplace, continue reading or get in touch today. 

Benefits of LangSmith
Through LangSmith’s debugging, testing, monitoring, and prompt management modules, enterprise customers benefit from:

Increased visibility of user interactions with their production LLM-applications: LangSmith gives engineering teams trace-level detail on what their end users are asking their LLM-apps and how the app is responding in production. With easy to augment traces with end-user feedback, LangSmith provides the observability needed for remediation and continual improvement. LangSmith offers teams peace of mind on
performance and quality, 
audibility of conversations, and 
explainability when interactions fall short of expectations. 
More complete testing coverage to improve application quality: LLM-apps are powerful, but have peculiar characteristics. The non-determinism, coupled with unpredictable, natural language inputs, make for countless ways the system can fail. LangSmith re-imagines traditional software engineering testing to be better suited for working with LLMs. With LangSmith’s Testing & Evaluation module, developers can build confidence in how their application will perform before shipping it to end users. LangSmith helps developers spot regressions and identify if changes to the application logic are moving key metrics in the right direction.
Improved application development velocity and collaboration with subject matter experts: LangSmith helps developers debug their application traces to pinpoint where an agent or chain is going off the rails. LangSmith also improves developer collaboration with subject matter experts (e.g. product managers or quality assurance teams) on prompt construction and labeling feedback that often need more end user or industry knowledge.
Clearer ROI analysis to make better business tradeoffs. When building LLM applications, you almost always are trading off amongst quality, cost, and latency. LangSmith helps teams run experiments to examine metrics related to these three, so that developers can back up their choices with data, helping them prioritize what matters and keep spend in check.
Benefits of procuring LangSmith through the Azure Marketplace
When you purchase LangSmith through the Azure Marketplace, you’ll keep data fully contained in your Azure VPC, get ease of deployment, and experience a smoother procurement process.

LangSmith will run in your Azure VPC so no data is shared with a 3rd-party. As a monitoring platform, LangSmith logs a tremendous amount of useful information about what end users are asking of your LLM-applications and how your app responds. When you purchase LangSmith as an Azure Kubernetes Application, we’ll deploy the entire platform in your environment, so no data leaves your network and you have full control over data management. Additionally, infosec teams will appreciate that the Microsoft team has already vetted and certified the LangSmith offering and will continually run security vulnerability scans on our images to keep customers’ data and environments safe.
Deploying LangSmith to Azure Kubernetes Service (AKS) has never been easier. We will provide you with a trial license and then production license, upon transaction, to deploy LangSmith and its dependencies to your AKS or OpenShift cluster. With a deep integration with Azure Resource Manager (ARM) APIs, LangSmith via the Azure Marketplace will be simple to set up and integrate. You’ll receive a minor release every six weeks and get white-glove support from our infra team to help with deployment, updates, and on-going scalability maintenance. 
You can retire credits from your Microsoft Azure Consumption Commitment (MACC). Many Azure customers rely on the full Microsoft suite of products to solve their infrastructure and development needs. LangSmith has met the requirements for IP co-sell, meaning you not only can use your Azure credits to purchase LangSmith, but also every dollar you spend on LangSmith will net against your MACC, making the process of budget approval easier on teams.
Furthering LangChain’s collaboration with Microsoft
We’re continuing to invest in LangChain’s technology collaboration with Azure AI services with deep integrations with Azure OpenAI, Azure AI Search, Microsoft Fabric, and more. Extending our product collaboration with a joint go-to-market effort for LangChain’s commercial offering, LangSmith, was a natural fit that benefits both our customers. 

If you’re looking for a platform that supports all phases of the LLM application lifecycle, consider LangSmith deployed in your Azure environment. Reach out directly in the Azure Marketplace or contact sales to start a conversation with one of our experts. We’re excited to work with you.

"""

twitter_output = generate_content(input_text, "twitter")
facebook_output = generate_content(input_text, "facebook")
linkedin_output = generate_content(input_text, "linkedin")
youtube_output = generate_content(input_text, "youtube")
instagram_output = generate_content(input_text, "instagram")

print("Twitter Thread:")
print(twitter_output["text"])

print("\nFacebook Post:")
print(facebook_output["text"])

print("\nLinkedIn Article:")
print(linkedin_output["text"])

print("\nYouTube Video Script:")
print(youtube_output["text"])

print("\nInstagram Caption:")
print(instagram_output["text"])