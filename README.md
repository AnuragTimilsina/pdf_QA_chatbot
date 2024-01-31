# My PDF Q&A Bot Project

## Introduction

In my latest project, I developed a personalized Q&A app that extracts information from PDF documents using open-source Large Language Models (LLMs). This project capitalizes on the benefits of open-source LLMs, providing customization, autonomy, cost efficiency, enhanced data security, and lower latency compared to commercial offerings.

![image](https://github.com/AnuragTimilsina/pdf_QA_chatbot/assets/33256063/72fb1cbe-589d-4c76-b3e5-93333a8e376c)


## Top Open-Source LLMs

I chose Falcon-Instruct (40B) and Guanaco (65b) as my primary text generation models, and e5-large-v2 (0.3B) and Instructor-xl (1.3B) as text embedding models. These models offer a good balance of performance and versatility.

## Project Components

### LLM Setup
I configured my project to use SBERT for text embedding and FlanT5-Base for text generation. These models offer a robust combination for processing PDF documents.

### PDF Data Processing
I leveraged ChromaDB to create a vector store for efficient retrieval of information from PDFs.

### Q&A Processing
I implemented a retrieval mechanism to find relevant snippets and engineered prompts for LLM queries.

## User Interface

To interact with my PDF knowledge bot, I built a user-friendly interface that allows users to upload a PDF, select LLM and embedding models, and ask questions.

## Conclusion

This project not only enhances my understanding of open-source LLMs but also provides a practical solution for extracting insights from PDF documents. While the code details are omitted for simplicity, the GitHub repository contains the full implementation.

