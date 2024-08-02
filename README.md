# DocuChat 2.0

## Overview

**DocuChat 2.0** is a RAG-based (Retrieval-Augmented Generation) chatbot application that enables users to interact with their documents through a conversational interface. Built using Streamlit, this application allows users to upload text documents, ask questions, and receive responses based on the content of the uploaded files. The application also includes features for feedback collection and analysis to continually improve the chatbot's performance.

## Features

- **File Upload**: Upload PDF, DOCX, and TXT files to be processed and indexed.
- **Chat Interface**: Ask questions related to the uploaded documents and receive responses.
- **Feedback Collection**: Provide feedback on the responses and submit it for analysis.
- **Export Chat History**: Export the chat history as text or DOCX files.
- **Feedback Analysis**: Visualize feedback data through interactive bar graphs.

## Requirements

- Python 3.7 or higher
- Required libraries (listed in `requirements.txt`)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your_username/DocuChat-2.0.git
   cd DocuChat-2.0
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up API Key:**

   Create a file named `secrets.toml` in the root directory and add your Gemini API key:

   ```toml
   [gemini_api_key]
   api_key = "your_api_key_here"
   ```

5. **Run the Application:**

   ```bash
   streamlit run app.py
   ```

## Usage

1. **Upload Files:**
   - Go to the sidebar and use the file uploader to upload PDF, DOCX, or TXT files.

2. **Ask Questions:**
   - Use the chat input box to ask questions related to the content of the uploaded files.

3. **Provide Feedback:**
   - After receiving a response, rate it using the radio buttons and submit your feedback.

4. **Export Chat History:**
   - Click on the sidebar buttons to export the chat history as a text or DOCX file.

5. **View Feedback Analysis:**
   - Click on the "Show Feedback Analysis" button in the sidebar to view feedback analytics.

## File Structure

- **`app.py`**: Main application file containing the Streamlit app logic.
- **`file_handler.py`**: Handles file uploads and text extraction.
- **`processing.py`**: Contains functions for document chunking, vectorization, and FAISS indexing.
- **`retrieval_response.py`**: Manages chunking, vectorization, and FAISS storage.
- **`requirements.txt`**: Lists the required Python libraries.
- **`secrets.toml`**: Stores sensitive information such as API keys (not included in version control).

## Contributing

1. **Fork the Repository**
2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature
   ```
3. **Commit Your Changes**
   ```bash
   git commit -am 'Add some feature'
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/your-feature
   ```
5. **Create a New Pull Request**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please contact rahulmydur@gmail.com.
