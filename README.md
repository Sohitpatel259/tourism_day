# Interactive Personality Quiz Webpage & QR Code Generator

This project contains a Python script that dynamically generates a complete, self-contained HTML webpage featuring biographies and quizzes of 15 famous Mexican personalities. It then creates a QR code that links to this webpage.

The generated webpage is fully interactive, featuring a light/dark theme selector, collapsible accordion sections for each biography, and an integrated quiz with a live score counter.

![Project Demo](https://storage.googleapis.com/gemini-prod/images/05116773-f11a-464a-997f-df6c18151478.png)
*(Image: The generated interactive webpage and the corresponding QR code.)*

## ✨ Features

-   **Dynamic HTML Generation**: Creates a complete `.html` file from a Python script.
-   **Interactive Accordion UI**: Biographies are neatly organized in collapsible sections.
-   **Theme Selector**: Switch between a clean Light Mode ☀️ and a sleek Dark Mode 🌙.
-   **Embedded Quizzes**: Each personality has a multiple-choice quiz question.
-   **Live Score Tracking**: A score counter updates in real-time as you answer questions correctly.
-   **One-Attempt Questions**: Quiz questions can only be answered once and provide immediate feedback.
-   **QR Code Generation**: Automatically generates a QR code linking directly to the webpage.
-   **Self-Contained**: The final HTML file has no external CSS or JavaScript dependencies, making it highly portable.

## 🛠️ Tech Stack

-   **Backend**: Python 3
-   **Library**: `qrcode[pil]` for QR code generation
-   **Frontend**: Vanilla HTML5, CSS3, and JavaScript

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

You need to have Python 3 installed on your system. You can check this by running `python --version`.

You also need to install the required Python library. Open your terminal or command prompt and run:

```bash
pip install "qrcode[pil]"
```

### Usage

1.  Clone this repository or download the `generate_final_quiz.py` file.
2.  Open your terminal and navigate to the directory where the file is saved.
3.  Run the Python script:
    ```bash
    python generate_final_quiz.py
    ```
4.  After the script runs, two new files will be created in the same directory:
    -   `famous_mexicans_final_quiz.html` (the webpage)
    -   `webpage_final_quiz_qr.png` (the QR code image)
5.  Open the `.html` file in your browser to view and interact with the webpage and quizzes.

## 🌐 Making the QR Code Publicly Accessible

By default, the script generates a QR code that points to a **local file path** (e.g., `file:///C:/Users/YourUser/...`). This will only work on the computer that generated it.

To make the QR code scannable by anyone on any device, you must host the HTML file online.

**Steps:**

1.  **Host the HTML file**: Upload the `famous_mexicans_final_quiz.html` file to a web hosting service. Excellent free options include:
    -   [GitHub Pages](https://pages.github.com/)
    -   [Netlify](https://www.netlify.com/)
    -   [Vercel](https://vercel.com/)

2.  **Get the Public URL**: After uploading, the service will give you a public URL (e.g., `https://your-username.github.io/your-repo/famous_mexicans_final_quiz.html`).

3.  **Update the Python Script**: Open `generate_final_quiz.py` and find the `create_webpage_and_qr_code` function. Modify the section responsible for the URL.

    **REPLACE THIS:**
    ```python
    # 2. Get the absolute path to the HTML file and format it as a file URI
    file_path = os.path.abspath(html_filename)
    file_uri = pathlib.Path(file_path).as_uri()
    print(f"🔗 Webpage URI: {file_uri}")
    #...
    qr.add_data(file_uri)
    ```

    **WITH THIS:**
    ```python
    # 2. Set the public URL where your HTML file is hosted
    public_url = "[https://your-actual-url-goes-here.com/famous_mexicans_final_quiz.html](https://your-actual-url-goes-here.com/famous_mexicans_final_quiz.html)"
    print(f"🔗 Public URL: {public_url}")
    #...
    qr.add_data(public_url)
    ```

4.  **Re-run the script**: Execute `python generate_final_quiz.py` one more time. The newly generated `webpage_final_quiz_qr.png` will now point to your live website and will be scannable by anyone.

## 📄 License

This project is licensed under the MIT License.