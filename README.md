
# Resource Statechart Code Extractor

Resource Statechart Code Extractor is a web application designed to facilitate the extraction of Business Units, generate their lifecycle, and visualize them through graphs based on an ODRL input.

## Technologies Used

-   **HTML/CSS/JavaScript:** Utilized for creating the user interface, structuring, styling, and interactivity.
-   **Mermaid:** A JavaScript library employed for rendering diagrams, enabling the lifecycle to be transformed into graphics.
-   **OpenAI API:** Integrated to leverage powerful language models, such as GPT, for automatic generation of responses from textual descriptions.
-   **Python:** The primary programming language for backend development.

## How to Use

1.  **Run the App:**
    
    -   Begin by executing `app.py`.
2.  **ODRL Input:**
    
    -   Access `/odlr` endpoint.
    -   Enter the ODRL input.
    -   Click on the button to generate the Business Unit (BU) specific to that input.
    -   Copy the generated BU.
3.  **Generate Lifecycle:**
    
    -   Navigate to `/lifecycle`.
    -   Paste the copied BU.
    -   Generate the lifecycle of this BU.
4.  **Graph Generation:**
    
    -   Proceed to `/graph`.
    -   Generate the graph for the lifecycle.

## Backend Operation

The backend of this application, developed in Python, integrates with the OpenAI API to process textual descriptions provided by the user and automatically generate appropriate responses.

### Workflow:

1.  **User Input:**
    
    -   The user submits textual descriptions through the web interface form.
2.  **OpenAI API Integration:**
    
    -   The backend integrates with the OpenAI API, utilizing the GPT language model to interpret the input and generate the corresponding response.
3.  **Response Delivery:**
    
    -   The generated response is then returned to the frontend.
4.  **Visualization:**
    
    -   The response is displayed on the user interface for visualization.

## How It Works

The backend receives the user's textual description sent via the web interface form. It then integrates with the OpenAI API to process the description, using the GPT language model to interpret the input and generate the corresponding response. After that it is returned to the frontend and displayed on the user interface for visualization.