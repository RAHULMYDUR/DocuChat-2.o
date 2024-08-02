Here’s a detailed README file for your project named **DocuChat 2.0**:

```markdown
# DocuChat 2.0

DocuChat 2.0 is a Retrieval-Augmented Generation (RAG) based chatbot application that allows users to upload documents and interactively ask questions. The application retrieves relevant information from the uploaded documents and generates contextually appropriate responses. Feedback from users is collected to improve the model's performance over time.

## Features

- **File Upload**: Supports uploading PDF, DOCX, and TXT files for processing.
- **Interactive Chat**: Users can ask questions related to the uploaded documents.
- **Feedback System**: Users can provide feedback on the responses, which is stored for analysis.
- **Feedback Analysis**: Visualize user feedback in the form of bar graphs to understand response effectiveness.
- **Export Options**: Users can export chat history in both text and DOCX formats.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Feedback Analysis](#feedback-analysis)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Steps to Install

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/DocuChat-2.0.git
   cd DocuChat-2.0
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API keys by creating a `secrets.toml` file in the root directory:
   ```toml
   [general]
   gemini_api_key = "YOUR_API_KEY"
   ```

## Usage

1. Run the application:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501` to access the application.

3. **Upload Files**: Use the file uploader on the sidebar to upload your documents (PDF, DOCX, or TXT).

4. **Ask Questions**: Enter your questions in the chat input area and hit enter.

5. **Provide Feedback**: After receiving a response, you can select "Yes" or "No" to indicate if the response was helpful. Click "Submit Feedback" to send your feedback.

6. **View Feedback Analysis**: Click the "Show Feedback Analysis" button in the sidebar to visualize the feedback data.

7. **Export Chat History**: Use the export options in the sidebar to download your chat history as a text file or a DOCX document.

## Feedback Analysis

The feedback analysis feature allows you to visualize user feedback through bar graphs. The graphs display the count of helpful and unhelpful responses, aiding in understanding the chatbot's performance.

## Code Structure

- **app.py**: The main application file containing the Streamlit app and core functionalities.
- **file_handler.py**: Handles file uploads and text extraction from documents.
- **processing.py**: Contains functions for chunking documents and vectorizing text for retrieval.
- **retrieval_response.py**: Implements the logic for retrieving relevant chunks from uploaded documents and generating responses.

## Contributing

Contributions are welcome! If you would like to contribute to DocuChat 2.0, please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add some feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

For any questions or inquiries, feel free to reach out to:

- **Your Name** - [your.email@example.com](mailto:your.email@example.com)
- **GitHub** - [yourusername](https://github.com/yourusername)

Thank you for using DocuChat 2.0!
```

### Notes:
- Replace placeholder values such as `https://github.com/yourusername/DocuChat-2.0.git`, `YOUR_API_KEY`, and your contact details with actual information.
- Feel free to adjust the content according to your specific project needs or add additional sections as necessary.
